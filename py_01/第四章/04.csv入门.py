#写入
import csv
# with open("./csv_data/csv01.csv","w",encoding="utf-8",newline="") as f:
#     witer = csv.writer(f)
#     #写入表头
#     witer.writerow(["姓名","年龄","城市"])
#     #写入数据
#     witer.writerows([["张三",18,"北京"],["李四",19,"上海"],["王五",20,"广州"]])
#     witer.writerows([["张三",18,"北京"],["李四",19,"上海"],["王五",20,"广州"]])


#字典写入
# with open("./csv_data/csv02.csv","w",encoding="utf-8",newline="") as f:
#     fieldnames = ["姓名","年龄","城市"]
#     writer = csv.DictWriter(f,fieldnames=fieldnames)
#     writer.writeheader() #写入表头
#     writer.writerow({"姓名":"赵六","年龄":22,"城市":"深圳"})
#     writer.writerow({"姓名": "孙七", "年龄": 35, "城市": "杭州"})

#读取
# with open("./csv_data/csv01.csv","r",encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

with open("./csv_data/csv02.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["姓名"], row["年龄"], row["城市"])

with open("./csv_data/csv01.csv", "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["钱八", 26, "成都"])