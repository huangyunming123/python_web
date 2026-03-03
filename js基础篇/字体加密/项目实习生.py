import re

import requests
from fontTools.ttLib import TTFont

from lxml import etree


class SXS():
    def __init__(self):
        self.url = "https://www.shixiseng.com/interns?page={}&type=intern&keyword=&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend="
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }

    def request_data(self):
        res = requests.get(self.url.format('3'), headers=self.headers)
        # (/ interns / iconfonts / file_1.woff?rand=0.5448859277028812)   .一个字符  *任意多  ？可有可无匹配1个  （.*？） 比.*? 精确 前者还具有捕获匹配内容的能力
        # .*？ 匹配字符串最短的一个数据
        findall = 'https://www.shixiseng.com' + \
                  re.findall('css">@font-face {    font-family: myFont;    src: url\((.*?)\);}', res.text)[0]
        print(findall)
        fontRes = requests.get(findall)
        with open('file.woff', 'wb') as f:
            f.write(fontRes.content)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(res.text)

    '''
          解题总结

          # 首先先去网页找到字体文件 然后下载为file_1.woff  
          # 用TTFont 打开后分析其编码 为 uni
          # 遍历后通过 分析网页的字体发现是&#X 开头  而我们十六进制是0x开头
          
          直接去网页分析 来获取字体 @font-face
          
          根据格式 \\u  \\u00 将k 重新编译  得到汉字   因为此时是字符串模拟的编码 所以要用unicode_escape解码 而不是utf-8
          然后将&#X 与汉字匹配起来即可得到 网页上的加密字与汉字匹配


        str = '\\u0048'
        print(str) \u0048
        original_char = '\u0048'
        print("Original character:", original_char) H


      '''

    def get_font(self):
        font_dict = {}
        font = TTFont('file.woff')
        # print(font.getBestCmap().items())
        # k是字符 v是编码格式
        for k, v in font.getBestCmap().items():
            if v[3:]:  ## v[3:] 3后面是否还有数  此处等价于len（）
                # 十六进制
                # print(k, hex(k))
                # print(hex(k).replace('0x', '&#X'))
                #  示例 uni 编码 第三位开始 后面如果是2位 则 \u00  如果是2位以上 则\u
                # aa = '\u5DE5'
                # print(aa.encode('utf-8').decode())
                con = '\\u00' + v[3:] if len(v[3:]) == 2 else '\\u' + v[3:]
                val = con.encode('utf-8').decode('unicode_escape')
                key = hex(k).replace('0x', '&#x')
                font_dict[key] = val
        return font_dict

    def parse_data(self, font_dict):
        with open('index.html', encoding='utf-8') as f:
            data = f.read()
            for k, v in font_dict.items():
                data = data.replace(k, v)
            print(data)
            html_data = etree.HTML(data)
            div_list = html_data.xpath('//div[@class="clearfix intern-detail"]')
            print(div_list)
            for i in div_list:
                comp = i.xpath('./div/p/a[@class="title ellipsis"]/text()')[0]
                price = i.xpath('//div[@class="f-l intern-detail__job"]/p/span[@class="day font"]/text()')[0]
                title = i.xpath('.//div[@class="f-l intern-detail__job"]/p/a[1]/text()')[0]
                print(comp, price, title)

    def main(self):
        self.request_data()
        font_dict = self.get_font()
        self.parse_data(font_dict)


if __name__ == '__main__':
    aa = SXS()
    aa.main()
