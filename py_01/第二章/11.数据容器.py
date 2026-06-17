# 案例3：生成1-20的平方列表
# num_list = []
# for i in range(1, 21):
#     num_list.append(i**2)

# num_list = [i**2 for i in range(1,21)]
# print(num_list)

# 案例4：从一个数字列表忠提取所有偶数，并计算其平方，组成一个新的列表
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,41541,52,56,46,655,546,26,46,26,4346,42]
# even_list= [i**2 for i in num_list if i % 2 == 0]
# print(even_list)

# 1.将如下多个列表合并为一个列表，并去重复元素，排好序（升序）后输出到控制台
# list1 = ['M','A','C','E','G','H','L','N','I','J','K','O']
# list2 = ['X','Z','T','Y','D','E','F','G']
# list3 = ['W','A','S','D']
#
# new_list = []
# num_list = []
# new_list = list1 + list2 + list3
#
# # num_list = [i for i in new_list if i not in ]
# for i in new_list:
#     if i not in num_list:
#         num_list.append(i)

# num_list.sort()
# print(num_list)

# 2.将如下列表中能被3 或 5 整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表
# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# num_list = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0 ]
# print(num_list)

# 3.将如下列表中的正数提取出来，封装为一个新的列表
list1 = [1,2,-3,4,5,-6,7,8,-9,10,11,12,13,14,-15,16,-17,18,19,-20,21,-22,23,-24,-25,26,27,-28,29,30]
num_list = [i for i in list1 if i > 0]
print(num_list)
