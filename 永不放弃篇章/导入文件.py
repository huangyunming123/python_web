#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
京东商品导入脚本
读取Excel文件中的SKU编码，分批发送HTTP请求导入商品
"""

import pandas as pd
import requests
import json
import time
from typing import List


class JdProductImporter:
    def __init__(self, base_url: str, auth_token: str, shop_id: int):
        self.base_url = base_url
        self.auth_token = auth_token
        self.shop_id = shop_id
        self.batch_size = 50  # 每批处理1000条
        self.failed_skus = []  # 收集失败的SKU
        self.failed_details = []  # 收集失败的详细信息

        # 使用Session复用连接，保持长连接
        self.session = requests.Session()

        # 配置连接池参数
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=10,  # 连接池大小
            pool_maxsize=10,  # 连接池最大连接数
            max_retries=0  # 不自动重试，避免重复添加
        )
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

        # 设置请求头
        self.session.headers.update({
            'authorization': auth_token,
            'platform': '0',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'shopfullpath': 'claus-test.beeselectcloud.com',
            'usertype': '1',
            'content-type': 'application/json',
            'Cookie': f'Himall-User={auth_token}; Himall-User-Beehivemanage={auth_token}',
            'Connection': 'keep-alive'  # 保持长连接
        })

    def read_excel_skus(self, file_path: str, column_name: str = None) -> List[int]:
        """
        从Excel文件中读取SKU编码
        :param file_path: Excel文件路径
        :param column_name: 列名，如果为None则读取第二列
        :return: SKU编码列表
        """
        try:
            # 读取Excel文件
            df = pd.read_excel(file_path)

            # 获取第二列数据（索引为1）
            if column_name:
                sku_column = df[column_name]
            else:
                sku_column = df.iloc[:, 1]  # 第二列（索引从0开始）

            # 转换为整数列表并过滤空值
            sku_list = []
            for sku in sku_column:
                if pd.notna(sku):
                    try:
                        sku_list.append(int(sku))
                    except (ValueError, TypeError):
                        print(f"警告: 无法转换SKU值 '{sku}' 为整数，已跳过")

            print(f"成功读取 {len(sku_list)} 个SKU编码")
            return sku_list

        except FileNotFoundError:
            print(f"错误: 找不到文件 {file_path}")
            return []
        except Exception as e:
            print(f"读取Excel文件时发生错误: {str(e)}")
            return []

    def send_batch_request(self, sku_ids: List[int]) -> bool:
        """
        发送批量导入请求
        :param sku_ids: SKU ID列表
        :return: 请求是否成功
        """
        url = f"{self.base_url}/crm/product/importJdProductV2"  # 使用V2接口

        payload = {
            "skuIds": sku_ids,
            "shopId": self.shop_id
        }

        try:
            response = self.session.post(
                url,
                json=payload,
                timeout=(30, 600)  # 连接超时30秒，读取超时600秒（10分钟）
            )

            if response.status_code == 200:
                print(f"✓ 成功导入 {len(sku_ids)} 个SKU")
                # 打印并分析响应结果
                try:
                    result = response.json()
                    # 收集失败的SKU（根据实际响应结构调整）
                    self._collect_failed_skus(result, sku_ids)
                except:
                    print(f"响应内容: {response.text}")
                return True
            else:
                print(f"✗ 请求失败，状态码: {response.status_code}")
                print(f"响应内容: {response.text}")
                # 整个批次失败，记录所有SKU
                self.failed_skus.extend(sku_ids)
                self.failed_details.append({
                    'skus': sku_ids,
                    'error': f'HTTP {response.status_code}',
                    'response': response.text
                })
                return False

        except requests.exceptions.RequestException as e:
            print(f"✗ 网络请求异常: {str(e)}")
            # 网络异常，记录所有SKU
            self.failed_skus.extend(sku_ids)
            self.failed_details.append({
                'skus': sku_ids,
                'error': str(e)
            })
            return False

    def _collect_failed_skus(self, result: dict, original_skus: List[int]):
        """
        从importJdProductV2接口响应结果中收集失败的SKU
        根据ImportThirdDataDTO对象结构解析：
        - productIds: 批量导入成功返回的商品id
        - successSkuIdList: 批量导入成功的skuId
        - errorSkuIdList: 批量导入失败的skuId

        :param result: 响应结果
        :param original_skus: 原始请求的SKU列表
        """
        # 获取data字段
        data = result.get('data')
        if not data:
            # 如果没有data字段，尝试直接从result中获取
            data = result

        # 获取失败的SKU列表
        error_sku_list = data.get('errorSkuIdList')
        if error_sku_list and isinstance(error_sku_list, list):
            for sku_id in error_sku_list:
                if sku_id:
                    try:
                        self.failed_skus.append(int(sku_id))
                        self.failed_details.append({
                            'sku': int(sku_id),
                            'reason': '导入失败'
                        })
                    except (ValueError, TypeError):
                        self.failed_skus.append(sku_id)
                        self.failed_details.append({
                            'sku': sku_id,
                            'reason': '导入失败'
                        })
            print(f"⚠ 从响应中收集到 {len(error_sku_list)} 个失败SKU")
            print(self.failed_skus)

        # 获取成功的SKU列表（用于日志）
        success_sku_list = data.get('successSkuIdList')
        if success_sku_list and isinstance(success_sku_list, list):
            print(f"✓ 成功导入 {len(success_sku_list)} 个SKU")

        # 获取商品ID列表（用于日志）
        product_ids = data.get('productIds')
        if product_ids and isinstance(product_ids, list):
            print(f"✓ 生成商品ID: {len(product_ids)} 个")

    def process_all_skus(self, file_path: str):
        """
        处理所有SKU，分批发送请求
        :param file_path: Excel文件路径
        """
        # 读取所有SKU
        all_skus = self.read_excel_skus(file_path)

        if not all_skus:
            print("没有找到有效的SKU编码，退出程序")
            return

        # 分批处理
        total_batches = (len(all_skus) + self.batch_size - 1) // self.batch_size
        print(f"总共 {len(all_skus)} 个SKU，分为 {total_batches} 批处理")

        success_count = 0
        fail_count = 0

        for i in range(0, len(all_skus), self.batch_size):
            batch_skus = all_skus[i:i + self.batch_size]
            batch_num = (i // self.batch_size) + 1

            print(f"\n--- 处理第 {batch_num}/{total_batches} 批 ({len(batch_skus)} 个SKU) ---")

            success = self.send_batch_request(batch_skus)
            if success:
                success_count += len(batch_skus)
            else:
                fail_count += len(batch_skus)

            # 如果不是最后一批，等待一段时间避免请求过于频繁
            if i + self.batch_size < len(all_skus):
                print("等待5秒后继续下一批...")
                time.sleep(5)

        # 输出统计信息
        print("\n" + "=" * 60)
        print("处理完成!")
        print(f"总计: {len(all_skus)} 个SKU")
        print(f"成功: {success_count} 个")
        print(f"失败: {fail_count} 个")

        # 输出失败的SKU信息
        if self.failed_skus:
            print(f"\n失败的SKU数量: {len(self.failed_skus)}")
            print("=" * 60)

            # 去重
            unique_failed_skus = list(set(self.failed_skus))
            print(f"去重后失败SKU数: {len(unique_failed_skus)}")

            # 保存失败SKU到文件
            failed_file = "failed_skus.txt"
            with open(failed_file, 'w', encoding='utf-8') as f:
                f.write("失败的SKU编码列表:\n")
                f.write("=" * 60 + "\n")
                for i, sku in enumerate(unique_failed_skus, 1):
                    f.write(f"{i}. {sku}\n")
                f.write("\n" + "=" * 60 + "\n")
                f.write(f"总计: {len(unique_failed_skus)} 个\n")

            print(f"\n失败的SKU已保存到: {failed_file}")

            # 打印前20个失败SKU
            print(f"\n失败SKU列表（前20个）:")
            for i, sku in enumerate(unique_failed_skus[:20], 1):
                print(f"  {i}. {sku}")
            if len(unique_failed_skus) > 20:
                print(f"  ... 还有 {len(unique_failed_skus) - 20} 个")

            # 保存详细失败信息
            if self.failed_details:
                detail_file = "failed_skus_detail.json"
                with open(detail_file, 'w', encoding='utf-8') as f:
                    json.dump(self.failed_details, f, ensure_ascii=False, indent=2)
                print(f"\n详细失败信息已保存到: {detail_file}")

            # 再次打印所有失败的SKU（完整列表）
            print("\n" + "=" * 60)
            print("所有失败的SKU完整列表:")
            print("=" * 60)
            for i, sku in enumerate(unique_failed_skus, 1):
                print(f"{i}. {sku}")
            print("=" * 60)
            print(f"总计: {len(unique_failed_skus)} 个失败SKU")
            print("=" * 60)

        print("=" * 60)


def main():
    # 配置参数
    BASE_URL = "http://localhost:8202"  # 根据实际情况修改
    AUTH_TOKEN = "59hK4WsuV1TR8haZPHfsze2BE9m/fGCUB3P1BnPa/hjEWM066k+VTr1lmztVCjOMoMYfm08Mcqxus/Vlw10TYv6tOm0UdZk6ztaXh9jHI1GIDq8Hp7LJdRU2X1UYMuVbIPtomzJXagI4rsz18FpFzb5Y1uUocfsErJ49BAuUuq8y8fyca1EScZuuEeV3k4JveCprZQMZe+8b/H7wRLQGSm3NXLv1fmLYMtBJMOU1FzdPP88w2TdyYjcYN2pIboJy"
    SHOP_ID = 728
    EXCEL_FILE = "京东商品导出.xlsx"  # Excel文件路径

    # 创建导入器实例
    importer = JdProductImporter(BASE_URL, AUTH_TOKEN, SHOP_ID)

    # 处理所有SKU
    importer.process_all_skus(EXCEL_FILE)


if __name__ == "__main__":
    main()