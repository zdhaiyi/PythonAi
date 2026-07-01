# D:\pycharm_demo\py_01\第四章\debug_page.py
import requests
from lxml import html

url = "https://www.themoviedb.org/movie/278-the-shawshank-redemption"
response = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}, timeout=60)

doc = html.fromstring(response.text)

# 打印页面中所有带 id 的关键元素，帮助定位
print("=== 页面中带 id 属性的主要元素 ===")
for el in doc.xpath("//*[@id]"):
    tag = el.tag
    eid = el.get("id", "")
    text = el.text_content().strip()[:80] if el.text_content() else ""
    if eid and len(eid) > 1:
        print(f"  <{tag} id='{eid}'> => {text}")

print("\n=== 页面 title ===")
print(doc.xpath("//title/text()"))

print("\n=== h2 标签内容 ===")
for h2 in doc.xpath("//h2"):
    print(f"  h2: {h2.text_content().strip()[:100]}")

print("\n=== h3 标签内容 ===")
for h3 in doc.xpath("//h3"):
    print(f"  h3: {h3.text_content().strip()[:100]}")

print("\n=== h4 标签内容 ===")
for h4 in doc.xpath("//h4"):
    print(f"  h4: {h4.text_content().strip()[:100]}")

print("\n=== 包含 class 含 movie/genre/overview/tagline/cast/crew 的元素 ===")
for el in doc.xpath("//*[contains(@class,'movie') or contains(@class,'genre') or contains(@class,'overview') or contains(@class,'tagline') or contains(@class,'cast') or contains(@class,'crew') or contains(@class,'fact') or contains(@class,'header')]"):
    tag = el.tag
    cls = el.get("class", "")
    text = el.text_content().strip()[:100]
    print(f"  <{tag} class='{cls}'> => {text}")
