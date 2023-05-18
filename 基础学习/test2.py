# #
# # #
# # # # format () 里面的数据也是带有索引的从0 开始
# # # print('{} {}'.format('hello','python'))
# # # print('{0} {1}'.format('hello','world'))
# # # print('{1} {0} {1}'.format('hello','world'))
# # # str1 = 'Hello'
# # # str2 = 'python'
# # # print('{},{}'.format(str1,str2))
# # # print('{},{},{}'.format(str1,str2,str1))
# # #
# # #
# # # # format(key= value,key =value)
# # # print('ID:{id},Name:{name}'.format(id='001',name='hello'))
# # #
# # #
# # # class value():
# # # 	id = '001'
# # # 	name = 'hello'
# # # print('ID:{Value.id},Name{Value.name}'.format(Value = value))
# # #
# # # import math
# # #
# # # print(f'The answer is {math.log(math.pi)}')
# # #
# # # v1 = input("请输入一个字符串: ")
# # # v2 = input("请输入一个整数: ")
# # # v3 = input("请输入一个浮点数: ")
# # # v4 = input("请输入一个布尔类型: ")
# # # print(f"输入的是字符串，变量类型是{type(v1)},内容是: {v1}")
# # # print(f"输入的是整数，变量类型是{type(v2)},内容是: {v2}")
# # # print(f"输入的是浮点数，变量类型是{type(v3)},内容是: {v3}")
# # # print(f"输入的是布尔值，变量类型是{type(v4)},内容是: {v4}")
# # #
# # # v5 = False
# # # v6 = True
# # #
# # # print(v5)
# # # print(type(v5))
# # # age = 21
# # # vip_level = 4
# # # if age <= 18:
# # #     print("你可以去开房了")
# # # elif int(input("请输入您的vip等级: "))>4:
# # #     print("可以提供特殊服务哦亲")
# # # elif vip_level > 3:
# # #     print("可以提供特殊服务")
# # # # default
# # # else:
# # #     print("先去找一个女朋友")
# # #
# # #
# # # print("为什么")
# #
# # import random
# # import math
# # age = 21
# # if age >= 18:
# #     print("成年人")
# #     if age >= 35:
# #         print("可以退休了")
# #     elif 20 <= age <= 23:
# #         print("还可以刚")
# # else:
# #     print("打工去吧")
# # num = random.randint(1, 100)
# # count = math.pow(2, 3)
# # print(f"number = {num}")
# # print(f"number_pow = {count}")
# # i = 0
# # while i < 100:
# #     print(f"我爱你 {i+1}")
# #     i += 1
# # j = 1
# # sum = 0
# # while j <= 100:
# #     sum += j
# #     j += 1
# # print(f"sum = {sum}")
# #
# # # print输出不换行
# #
# # print("hello", end='')
# # print("world")
# # print("world\tworld")
# # print("wor\tworld")
# #
# # i = 1
# # while i <= 9:
# #     j = 1
# #     while j <= i:
# #         print(f"{i} * {j} = {i*j}\t", end='')
# #         j += 1
# #     i += 1
# #     print()
# #
# # name = "ithema is a brand of itcaset"
# # count2 = 0
# # for x in name:
# #     if x == 'a':
# #         count2 += 1
# # print(count2)
# #
# # for i in range(5, 20):
# #     print(f"i = {i}")
# #
# # # range(num1,num2)  左闭右开的
# # i = 1
# # for i in range(1, 10):
# #     j = 1
# #     for j in range(1, i+1):
# #         print(f"{i} * {j} = {i * j}\t", end='')
# #     print()
# #
# #
# # for i in range(1, 101):
# #     print(f"追求小明的第{i}天")
# #     print("给小明送饭")
# #     for j in range(1, 11):
# #         print(f"给小明送花的第{j}天")
# #         continue
# #         # 不会被执行
# #         print("我爱你")
# #     print("再见")
# #     print()
# #
# # for i in range(1, 101):
# #     print(f"追求小明的第{i}天")
# #     print("给小明送饭")
# #     for j in range(1, 11):
# #         print(f"给小明送花的第{j}天")
# #         # 直接退出内层循环   break所在的循环永久中断。
# #         break
# #         # 不会被执行
# #         print("我爱你")
# #     print("再见")
# #     print()
# #
# #
# #
# money = 10000
# for i in range(1, 20):
#     import random
#     score = random.randint(1,10)
#     if score < 5:
#         print(f"员工{i} 绩效为{score},低于5分，不发工资，下一位")
#         continue
#     else:
#         money -= 1000
#         print(f"向员工{i} 绩效为{score},发放了工资1000元,账户余额{money}")
#         if money == 0:
#             print("工资发放完毕，下一个月来领取吧")
#             break
#
#
# def check(x, y):
#     print("欢迎来到南昌火车站!\n请出示您的核酸检测证明")
#     print(f"x= {x} ,y= {y}\t x+y ={x+y}")
#     result = x + y
#     return result
#
#
# add = check(10, 90)
# print(f"add={add}")
#
#
# def say_hello():
#     print("hello")
#     return None
#
# res = say_hello()
# print(type(res))
#
#
def check_age(age):
    if age > 18:
        return True
    return None


my_res = check_age(12)
if not my_res:
    print("未成年")
else:
    print("已成年")


val = None

my_num = 100


def add_num(x, y):
    """
    使用多行注释可以对函数参数进行说明
    :param x: 第一个参数
    :param y: 第二个参数
    :return:
    """
    # 声明一个全局变量
    global my_num
    my_num = 900

    print("相加")


add_num(2, 4)
print(my_num)


def main():

    print("主函数")


main()


