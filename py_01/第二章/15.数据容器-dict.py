"""
开发一个购物车管理系统，实现商品信息的增删改查功能
1.添加购物车：用户根据提示录入商品名称、以及商品的价格、数量，保存该商品信息到购物车
2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量、输入完成后修改该商品信息
3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车的商品
4.查询购物车：查询购物车所有商品信息
5.退出系统：退出系统
"""

shopping_cart = {}
menu = """
######## 购物车系统 ##########
#        1.添加购物车        #
#        2.修改购物车        #
#        3.删除购物车        #
#        4.查询购物车        #
#        5.退出购物车        #
############################
"""
# while True :
#     print("欢迎使用购物车管理系统")
#     print(menu)
#     choice = int(input("请输入你的选择："))
#     match choice:
#         case 1:
#             goods_name = str(input("请输入商品名称："))
#             goods_price = float(input("请输入商品价格："))
#             goods_num = int(input("请输入商品数量："))
#             # 判断购物车中是否有该商品
#             if goods_name in shopping_cart:
#                 print("购物车中已存在该商品，请重新选择")
#                 continue
#             else:
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#         case 2:
#             goods_name = str(input("请输入修改商品名称："))
#             if goods_name not in shopping_cart:
#                 print("购物车中没有该商品，请重新选择")
#                 continue
#             else:
#                 goods_price = float(input("请输入修改商品价格："))
#                 goods_num = int(input("请输入修改商品数量："))
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#                 print("成功修改商品")
#         case 3:
#             goods_name = str(input("请输入删除商品名称："))
#             if goods_name not in shopping_cart:
#                 print("购物车中没有该商品，请重新选择")
#                 continue
#             else:
#                 del shopping_cart[goods_name]
#                 print("成功删除商品")
#         case 4:
#             for k, v in shopping_cart.items():
#                 print(f"商品名称：{k}，商品价格：{v['price']}，商品数量：{v['num']}")
#         case 5:
#             print("退出系统")
#             break
#         case _:
#             print("输入格式错误,请重新输入")


# 基于现有知识开发一个教务管理系统
# 开发一个教育管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1.添加学生信息：根据提示录入学生姓名、数学、英语成绩，录入完成保存到系统中
# 2.修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息
# 3.删除学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出
# 4.查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出
# 5.列出所有学生：遍历所有学生信息并输出
# 6.统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文

