# if条件判断练习
# score = 620
# if score > 680:
#     print("优秀")
# else:
#     print("良好")
# print("结束")

# 案例：根据用户输入的年份，判断这一年是闰年还是平年。闰年的条件是：能被4整除，但不能被100整除，或者能被400整除
# year = int(input("请输入年份："))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year} 是闰年")
# else:
#     print(f"{year} 是平年")

# 需求1：根据用户输入的数字，判断该数字是奇数还是偶数
# num = int(input("请输入数字："))
# if num % 2 == 0:
#     print(f"{num} 是偶数")
# else:
#     print(f"{num} 是奇数")

# 需求2：根据用户输入的年龄，判断该用户是否已经成年（>=18，成年；否则，未成年）
# age = int(input("请输入年龄："))
# if age >= 18:
#     print(f"{age} 成年")
# else:
#     print(f"{age} 未成年")

# 需求3：根据用户输入的数字，判断该数字是正数还是负数（不考虑0）
# num = int(input("请输入数字："))
# if num > 0:
#     print(f"{num} 是正数")
# elif num < 0:
#     print(f"{num} 是负数")

# 需要4：根据用户输入的考试分数，判断该分数是否及格了（大于等于60就是及格了）
# score = float(input("请输入考试分数："))
# if score >= 60:
#     print(f"{score} 及格")
# else:
#     print(f"{score} 不及格")

# 1.根据输入的考试成绩，判断成绩等级，大于等85分为优秀，60-85分为良好，否则不及格
# score = float(input("请输入考试成绩："))
# if score >= 85:
#     print(f"{score} 优秀")
# elif score >= 60:
#     print(f"{score} 良好")
# else:
#     print(f"{score} 不及格")

# 2.购物折扣计算：根据输入的购物车的商品总额，以及如下的折扣规则，计算实际的金额
# 金额 >= 5000 ： 8折，300<=金额< 500: 9折，100<=金额<300:95折， 金额<100：无折扣
total = float(input("请输入购物车商品总额："))
if total >= 5000:
    print(f"您消费了{total}元，可享受8折优惠，实际支付金额为：{total * 0.8}元，已优惠{(total - total * 0.8)}元")
elif total >= 300:
    print(f"您消费了{total}元，可享受9折优惠，实际支付金额为：{total * 0.9}元，已优惠{(total - total * 0.9)}元")
elif total >= 100:
    print(f"您消费了{total}元，可享受95折优惠，实际支付金额为：{total * 0.95}元，已优惠{(total - total * 0.95)}元")
else:
    print(f"您本次消费了{total}元，抱歉没有享受到优惠，欢迎下次惠顾")