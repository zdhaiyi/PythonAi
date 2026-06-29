import requests

tiobe_url = "https://www.tiobe.com/tiobe-index/"

req_get = requests.get(tiobe_url)
print(req_get.text)

#写入文件里
with open("./resourcefile/tiobe.html", "w", encoding="utf-8") as f:
    f.write(req_get.text)
print("文件写入完成")
