from fontTools.ttLib import TTFont

# 加载字体文件
font = TTFont('file_1.woff')
# 还原成源代码 生产file.xml   字体轮廓  字符映射  xml形式
font.saveXML('file_1.woff.XML')

res = font.getBestCmap()
print(res)