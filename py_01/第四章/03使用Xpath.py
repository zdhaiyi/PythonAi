from lxml import html

#读取html文件
with open("./resourcefile/仙逆人物志.html", "r", encoding="utf-8") as f:
    html_content = f.read()

document = html.fromstring(html_content)

# print(document)
print(document.xpath(" //tbody/tr/td[1]/text()"))
