from lxml import html
import requests

# tiobe_url = "https://admin.netseas.net/index/"
# req_get = requests.get(tiobe_url)

# with open("./resourcefile/xianni.html", "w", encoding="utf-8") as f:
#     f.write(req_get.text)
with open("./resourcefile/xianni.html", "r", encoding="utf-8") as f:
    html_content = f.read()
doc = html.fromstring(html_content)
# print(doc)
doc_text = doc.xpath("//div/text()")
print(doc_text)

