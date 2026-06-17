# 创建对象
class Car:
    def __init__(self ,name,color,price):
        self.name = name
        self.color = color
        self.price = price
        print("执行一个对象")
    def ruuing(self):
        print(f"{self.name}正在运行")

    def buy(self,discount,rate = 0.1):
        total_cost = self.price * discount + self.price * rate
        return total_cost

c1 = Car("保时捷","黑色",1000000)
c1.ruuing()
buycost = c1.buy(0.85)
print(f"{c1.name}的购买价格是{buycost}")