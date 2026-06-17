# 算数运算符的优先级
# print("0.1+10/4**2", (0.1+10)/4**2)

# 案例：要求输入两个数x与y,分别输出x+y的结果和x-y的结果
# x = float(input("请输入x："))
# y = float(input("请输入y："))
# print("x+y=", x+y)
# print("x-y=", x-y)
# print("x*y=", x*y)
# print("x/y=", x/y)

# 案例1：计算输入的三个整数的平均值
# a = int(input("请输入第一个整数："))
# b = int(input("请输入第二个整数："))
# c = int(input("请输入第三个整数："))
# print("三个整数的平均值为：", (a+b+c)/3)

# 案例2：要求输入梯形的上底、下底、高，然后计算梯形的面积
# a = float(input("请输入梯形的上底："))
# b = float(input("请输入梯形的下底："))
# h = float(input("请输入梯形的高："))
# print("梯形的面积为",(a+b) *h/2)

# 案例3：要求输入园的半径，然后计算园的周长和面积（周长：2Πr，面积：兀r²）
# r = float(input("请输入圆的半径："))
# print("园的周长为：",2*3.14*r)
# print("园的面积为：",3.14*r**2)

# 案例4：身体质量指数BMI的计算（BMI = 体重（kg）/身高（m）²）
# 1.输入体重（单位kg）
# 2.输入身高（单位m）
# 3.计算身高质量指数BMI并输出
weight = float(input("请输入体重（KG）："))
height = float(input("请输入升高（m）:"))
print("BMI身体质量指数为：",weight/height ** 2)