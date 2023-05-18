# # # # # # name_list = ['ithema', 'itcast', 'python']
# # # # # # name_list1 = ['ithema', 190, True]
# # # # # # print(name_list)
# # # # # # print(name_list1)
# # # # # # print(type(name_list))
# # # # # #
# # # # # # my_list = [[1, 2, 3], [5, 6, 7]]
# # # # # # print(my_list)
# # # # # #
# # # # # #
# # # # # # print(name_list[1])
# # # # # # print(my_list[1][2])
# # # # # #
# # # # # # # 反向索引从-1开始 正向索引从0开始
# # # # # # print(name_list1[-1])
# # # # # #
# # # # # # # 查索引
# # # # # # print(my_list.index([1,2,3]))
# # # # # #
# # # # # # name_list[1] = '翁涛涛'
# # # # # # name_list[-1]= '源宝宝'
# # # # # # print(name_list)
# # # # # #
# # # # # #
# # # # # # my_numlist = [1, 2, 3]
# # # # # # my_numlist.insert(1,'ithema')
# # # # # # print(my_numlist)
# # # # # #
# # # # # # my_numlist.append("大宝贝")
# # # # # # print(my_numlist)
# # # # # #
# # # # # # my_numlist.append([1, 4, 5])
# # # # # # print(my_numlist)
# # # # # #
# # # # # # my_numlist.extend(["ithema", "love", "mahoupao"])
# # # # # # print(my_numlist)
# # # # # # del my_numlist[0]
# # # # # #
# # # # # # my_numlist.pop(2)
# # # # # #
# # # # # # print(my_numlist)
# # # # # #
# # # # # # my_numlist.remove(2)
# # # # # # print(my_numlist.count("ithema"))
# # # # # # print(len(my_numlist))
# # # # # #
# # # # # #
# # # # # # index = 0
# # # # # # while index < len(my_numlist):
# # # # # #     print(my_numlist[index])
# # # # # #     index += 1
# # # # # # print("--------------")
# # # # # # for i in my_numlist:
# # # # # #     print(i)
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # t1 = (1, "ithema", True, "ithema", 12)
# # # # # print(t1)
# # # # # t2 = ('hello',)
# # # # # print(t2)
# # # # # print(type(t2))
# # # # # t3 = ('world')
# # # # # print(type(t3))
# # # # # t4 = (1,)
# # # # # print(type(t4))
# # # # #
# # # # # print(t1[1])
# # # # #
# # # # # print(t1.index('ithema'))
# # # # # print(t1.count("ithema"))
# # # # # print(len(t1))
# # # # #
# # # # # index = 0
# # # # # while index < len(t1):
# # # # #     print(t1[index])
# # # # #     index += 1
# # # # # print("----------------")
# # # # # for t1item in t1:
# # # # #     print(t1item)
# # # # #
# # # #
# # # # name = "12ithema is a company ithema21"
# # # # # del name[0]
# # # # # name[0] = 'a'
# # # # # print(name)
# # # # #
# # # # print(name.index("is"))
# # # #
# # # # new_name = name.replace("it", "传值")
# # # # print(name)
# # # # print(new_name)
# # # #
# # # # name_list = name.split(" ")
# # # # print(name)
# # # # print(name_list)
# # # #
# # # # print(name.strip())
# # # # print(name.strip("12"))
# # # # 正向
# # # my_list = [1, 2, 3, 4, 5]
# # # new_list = my_list[1:4:]
# # # print(new_list)
# # #
# # # my_tuple = (1, 2, 3, 4, 5)
# # # #                                      左闭右开
# # # new_tuple = my_tuple[1:4:2]
# # # print(new_tuple)
# # # # 反向
# # # my_str = "12345"
# # # new_str = my_str[::-1]
# # # print(my_str)
# # # print(new_str)
# # #
# # # # 从下标三开始 下标1结束 步长-1 不含1的元素   左开右闭
# # # new_list2 = my_list[3:1:-1]
# # # print(new_list2)
# # #
# # #
# # #
# # #
# # #
# #
# # names = {"盒马程序员", 123, "盒马程序员", "ithema", True, 123}
# # print(names)
# # names.add("你好")
# # print(names)
# # names.remove(123)
# # print(names)
# #
# # set1 = {1, 3, 5, 7, 9}
# # set2 = {5, 7, 9, 10, 17}
# # set3 = set1.difference(set2)
# # print(set3)  # {1 , 3}
# # set4 = set1.union(set2)
# # print(set4)
# # print(len(set4))
# # for item in set4:
# #     print(f"item : {item}")
# #
# stu_score = {"王力宏": 99, "周杰伦": 100, "张惠妹": True}
#
# print(stu_score["张惠妹"])
# print(stu_score["周杰伦"])
#
# stu_scores = {"王力宏": {"语文": 99, "数学": 100, "英语": 99}, "周杰伦": {"语文": 99, "数学": 100, "英语": 99}}
# print(stu_scores["周杰伦"])
# stu_score["林俊杰"]= 66
# print(stu_score)
#
# keys = stu_score.keys()
# for key in keys:
#     print(f"学生：{key},分数：{stu_score[key]}")
#
# print(len(stu_score))
#
# print(max(stu_score))
# print(min(stu_score))
# my_list = list(stu_score)
# print(my_list)
# my_str = str(my_list)
# print(my_str)
# my_sort = {1, 4, 7, 3, 2, 9}
# a = sorted(my_sort, reverse=True)
# print(my_sort)
# print(*a)
#
# print("abc" < "ad")
#
# from operator import itemgetter
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# # 按名字排序
# L2 = sorted(L, key=itemgetter(0))
# # 按成绩排序
# L3 = sorted(L, key=itemgetter(1))
# print("按名字排序: ")
# print(L2)
# print("按成绩排序: ")
# print(L3)
# # >>>按名字排序:
# # [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
# # # 按成绩排序:
# # [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]
#
#
# def test_return():
#     return 10, True
#
#
# x, y = test_return()
# print(x)
# print(y)
#
#
# def user_info(name, age, gender):
#     print(f"您的名字是：{name},年龄是：{age},性别是：{gender}")
#
#
# # 关键字传参
# user_info(name="小明", age=20, gender="男")
# # 可以不按照固定顺序
# user_info(age=20, name="小明", gender="男")
#
# # 可以和位置参数混用，位置参数需要在前面并且匹配顺序
# user_info("小明",age=20, gender="男")
#
#
# def user_plus(*args):
#     print(args)
#
#
# user_plus("Tom", True)
#
#
# def user_plusplus(**kwargs):
#     print(kwargs)
#
#
# user_plusplus(name="Tom", age=19, id=100)
#
#
# def compute(x, y):
#     return x + y
#
#
# def test_func(compute):
#     result = compute(3, 4)
#     print(result)
#
#
# test_func(compute)
#
#
# # 使用lambda表达式
# test_func(lambda x, y: x+y)
#
# a = [(1, 2), (4, 1), (9, 10), (13, -3)]
# a.sort(key=lambda x: x[1], reverse=True)  # key表示自定义排序规则
#
# print(a)
# # Output: [(13, -3), (4, 1), (1, 2), (9, 10)]
#
# # 列表 元素为元组
# x = [(1, 2), (4, 1), (9, 10), (13, -3)]
# x.sort(key=lambda y: y[0])
# print(x)
#
# my_file = open("D:\\python.txt", 'a', encoding="UTF-8")
# context = my_file.read()
# print(context)

# context2 = my_file.readlines()
# print(context2)

# context = my_file.readline()
# print(context)
#
# context = my_file.readline()
# print(context)
#
# context = my_file.readline()
# print(context)

# 循环读取
# for line in my_file:
#     print(line)
#
# my_file.close()
# 写入缓冲器
# my_file.write("\nyuan bao bao")
# # 刷新缓冲器
# my_file.flush()

# my_bill = open("D:\\bill.txt", 'r', encoding="UTF-8")
# my_bak = open("D:\\bill.txt.bak", 'a', encoding="UTF-8")
#
# for line in my_bill:
#     if line.count("测试") == 0:
#         my_bak.write(line)
#         my_bak.flush()
# my_bak.close()
# my_bill.close()

# try:
#     f = open('linux.txt', 'r')
# except:
#     print("打开的文件不存在")

# try:
#     print(1 / 0)
# except (NameError, ZeroDivisionError) as e:
#     print("ZeroDivisionError错误")
#     print(e)
#
# try:
#     print(1 / 0)
# except Exception as e:
#     print(e)
# else:
#     print("我是else,是没有异常的时候执行的代码")
# finally:
#     print("无论如何都要执行的代码")
#
#
# # 异常的传递
# def func01():
#     print("这是func01开始")
#     num = 1 / 0
#     print("这是func01结束")
#
#
# def func02():
#     print("这是func02开始")
#     func01()
#     print("这是func02结束")
#
#
# def main():  # 异常最终在这里捕获
#     try:
#         func02()
#     except Exception as e:
#         print(e)
#
#
# main()

# import time as tt
# from random import randint as ran
# from my_package import my_module1
# import my_package.my_module2
# import numpy
# print("开始")
# tt.sleep(1)
# print("结束")
#
# print(f"随机数：{ran(10, 99)}")
# my_module1.test(10, 20)
#
# print(f"test3的__name__ 是{__name__}")

# import my_utils.str_util
# from my_utils import file_util
# print(my_utils.str_util.str_reverse("黑马程序员"))
# print(my_utils.str_util.sub_str("黑马程序员", 1, 4))
# file_util.append_to_file("D:/bill.txt", "大学生都是成年人了")
#

# 导入json模块
import json

# 准备符合json格式的
# 1、 一个单独的字典 {"name": "admin", "age": 18}
# 2、 内部元素是字典的集合 [ {"name": "admin", "age": 18} ,{"name": "root", "age": 20}]

# 将python数据转换为json数据
data = [{"name": "管理员", "age": 18} ,{"name": "root", "age": 20}]
print(type(data))
data = json.dumps(data, ensure_ascii=False)
print(type(data))
print(data)
# json转换为python数据
my_data = json.loads(data)
print(my_data)
















