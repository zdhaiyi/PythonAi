"""1.定义一个函数，根据传入的分数，计算对应的分数等级并返回
    分数 >= 90: A
    分数 >= 75: B
    分数 >= 60: C
    分数 < 60: D
"""


# def get_grade(score):
#     """
#     根据传入的分数评定等级
#     :param score: 分数
#     :return: 输出等级
#     """
#     if score >= 90:
#         return print(f"根据{score}分,等级为A")
#     elif score >= 75:
#         return print(f"根据{score}分,等级为B")
#     elif score >= 60:
#         return print(f"根据{score}分,等级为C")
#     else:
#         return print(f"根据{score}分,等级为D")
#
# scor_text = float(input('请输入分数：'))
# get_grade(scor_text)


"""
   定义一个函数，用于判断一个字符串是否是回文，返回bool值
    把字符串反转，如果和原来字符串相同，就是回文串。（如：“level”，“radar”，“黄山落叶松叶落山黄”）
"""
# def is_palindrome(text):
#     """
#     判断字符串是否是回文
#     :param text: 字符串
#     :return: bool值
#     """
#     return text == text[::-1]
#
# text1 = input('请输入字符串：')
# print(is_palindrome(text1))

# 3.定义一个函数，完成时间转换功能，将传入的秒转换为小时、分钟、秒

# def itmeseconds(items):
#     """
#     将传入的秒转换为小时、分钟、秒
#     :param items: 传入时间
#     :return: 返回小时、分钟、秒
#     """
#     hour = items //3600
#     minute = (items - hour * 3600) // 60
#     second = items - (hour * 3600 + minute * 60)
#     return print(f"{hour}时{minute}分{second}秒")
#
#
# items = int(input('请输入秒数：'))
# itmeseconds(items)

# 4.定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）

def triangle(a, b, c):
    """
    根据传入的三角形三个边的边长，判定三角形的类型
    :param a: 三角形第一个边
    :param b: 三角形第二个边
    :param c: 三角形第三个边
    :return: 三角形的类型
    """
    if a + b > c and a + c > b and b + c > a :
        if a == b == c:
            return print("等边三角形")
        elif a == b or a == c or b == c:
            return print("等腰三角形")
        else:
            return print("普通三角形")
    else:
        return print("不能构成三角形")

a = float(input('请输入三角形第一个边：'))
b = float(input('请输入三角形第二个边：'))
c = float(input('请输入三角形第三个边：'))

triangle(a,b,c)