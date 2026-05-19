#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
订单导出脚本
从数据库查询订单数据并导出到Excel
"""

import pymysql
import pandas as pd
from datetime import datetime


# ============ 数据库配置（请修改为实际配置） ============
DB_CONFIG = {
    'host': 'mysqlprod01.internal.cn-north-4.mysql.rds.myhuaweicloud.com',
    'port': 3306,
    'user': 'developer',
    'password': 'Prod@RDS2023#',
    'database': 'crm_saas',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}
# ========================================================


def get_connection():
    """获取数据库连接"""
    return pymysql.connect(**DB_CONFIG)


def query_orders(conn):
    """
    查询所有非取消状态的订单，按创建时间倒序
    关联 t_order（子单） 和 t_order_main（主单）
    """
    sql = """
    SELECT
        o.id AS `订单编号`,
        om.user_name AS `用户姓名`,
        o.product_total_amount AS `商品总额`,
        o.sku_real_sale_price AS `采购价`,
        o.quantity AS `采购数量`,
        IFNULL(o.order_remark, '') AS `买家留言`,
        om.ship_to AS `收货人`,
        om.cell_phone AS `手机号码`,
        om.full_address AS `收货地址`,
        o.product_name AS `商品名称`,
        CONCAT_WS(';',
            IFNULL(o.color, ''),
            IFNULL(o.version, ''),
            IFNULL(o.`size`, '')
        ) AS `规格信息`,
        IFNULL(o.seller_remark, '') AS `商家备注`,
        CASE o.order_status
            WHEN 1 THEN '待付款'
            WHEN 2 THEN '待发货'
            WHEN 31 THEN '部分发货'
            WHEN 3 THEN '待收货'
            WHEN 4 THEN '已取消'
            WHEN 5 THEN '已完成'
            WHEN 6 THEN '待自提'
            WHEN 7 THEN '未评价'
            WHEN 8 THEN '待消费'
            WHEN 9 THEN '待收款'
            WHEN 10 THEN '退款中'
            WHEN 11 THEN '待商家确认'
            WHEN 12 THEN '商家已拒绝'
            WHEN 15 THEN '待审批'
            WHEN 51 THEN '未评价'
            ELSE CONCAT('未知状态(', o.order_status, ')')
        END AS `订单状态`
    FROM t_order o
    LEFT JOIN t_order_main om ON o.parent_order_id = om.order_main_id
    WHERE o.order_status != 4
    ORDER BY o.create_time DESC
    """
    with conn.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()


def export_to_excel(data, output_path):
    """将数据导出到Excel"""
    df = pd.DataFrame(data)

    # 确保列顺序与Excel模板一致
    columns = [
        '订单编号', '用户姓名', '商品总额', '采购价', '采购数量',
        '买家留言', '收货人', '手机号码', '收货地址',
        '商品名称', '规格信息', '商家备注', '订单状态'
    ]
    df = df[columns]

    # 订单编号转为字符串，避免科学计数法
    df['订单编号'] = df['订单编号'].astype(str)

    # 采购数量转为整数
    df['采购数量'] = df['采购数量'].apply(lambda x: int(x) if pd.notna(x) else x)

    # 金额字段保留两位小数
    for col in ['商品总额', '采购价']:
        df[col] = df[col].apply(lambda x: round(float(x), 2) if pd.notna(x) else x)

    df.to_excel(output_path, index=False, sheet_name='订单')
    print(f"导出完成，共 {len(df)} 条记录")
    print(f"文件路径: {output_path}")


def main():
    # 生成带时间戳的输出文件名
    now = datetime.now().strftime('%Y-%m-%d %H_%M_  %S')
    output_path = f"商城订单-{now}.xlsx"

    print("正在连接数据库...")
    conn = get_connection()

    try:
        print("正在查询订单数据...")
        data = query_orders(conn)
        print(f"查询到 {len(data)} 条记录")

        if data:
            print("正在导出Excel...")
            export_to_excel(data, output_path)
        else:
            print("没有查询到数据")
    finally:
        conn.close()
        print("数据库连接已关闭")


if __name__ == '__main__':
    main()
