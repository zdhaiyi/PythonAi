# 根据提供的学生成绩单，完成如下需求：
# 1.计算每个学生的总分、各科平均分、然后一并输出出来
# 2.统计各科成绩的最低分、最高分、平均分，并输出
# 3.查找成绩优秀（平均分大于90）的学生，并输出

transcription = (
    ("s001","王林",85,9.5,78),
    ("s002","李慕婉",92,88,95),
    ("s003","王伟",65,75,68),
    ("s004","曾牛",85,85,85),
    ("s005","十三",65,95,85),
    ("s006","周易",85,95,85),
    ("s007","红蝶",85,90,85),
    ("s008","遁天",67,95,75),
    ("s009","徐立国",99,95,90),
    ("s010","许木",66,59,72),
)
# 1.计算每个学生的总分、各科平均分、然后一并输出出来
# for s in transcription:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     # print("学号：%s 姓名：%s 总分：%d 平均分：%.2f" % (s[0], s[1], total, avg))
#     # print("学号：{} 姓名：{} 总分：{} 平均分：{:.2f}".format(s[0], s[1], total, avg))
#     print(f"学号：{s[0]} 姓名：{s[1]} 总分：{total} 平均分：{avg:.1f}")

for id,name,chines,math,english in transcription:
    total = chines + math + english
    avg = total / 3
    print(f"学号：{id} 姓名：{name} 总分：{total} 平均分：{avg:.1f}")

print()

# 2.统计各科成绩的最低分、最高分、平均分，并输出
chinese_scores = [s[2] for s in transcription]
math_scores = [s[3] for s in transcription]
english_scores = [s[4] for s in transcription]
# print(type(chinese_scores))
print(f"语文最低分：{min(chinese_scores)}, 最高分：{max(chinese_scores)}，平均分：{sum(chinese_scores) / len(chinese_scores):.1f}")
print(f"数学最低分：{min(math_scores)}, 最高分：{max(math_scores)}，平均分：{sum(math_scores) / len(math_scores):.1f}")
print(f"英语最低分：{min(english_scores)}, 最高分：{max(english_scores)}，平均分：{sum(english_scores) / len(english_scores):.1f}")
print()
# 查找成绩优秀（平均分大于90）的学生，并输出

for id,name,chines,math,english in transcription:
    total = chines + math + english
    avg = total / 3
    if avg > 90:
        print(f"学号：{id} 姓名：{name} 总分：{total} 平均分：{avg:.1f}")