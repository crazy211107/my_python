row = 1
while row <= 9:
    column = 1
    while column <= row:
        print('{}*{}={}'.format(column, row, row*column), end='\t')
        column += 1
    print()
    row += 1
string_type = type("黑马程序员")
int_type = type(190)

print(string_type , int_type,"\n")
print(string_type)

test = """
This is the third maintenance release of Python 3.11
Python 3.11.3 is the newest major release of the Python programming language, and it contains many new features and optimizations.
"""
print(test)
my_str = '123456'
print(my_str)
my_int=int(my_str)
print(my_int)
# 复数
a = 4+3j
b = 5-2j
print(a*b)

print("9*4= %d 不是" % (9*4))
print("9/4= %d" % (9/4))
print("9**4= %d" % (9**4))

name = "源宝宝"
set_up_year = 2002
stock_price = 19.789

message = "我是: %s 我的出生年份是 : %d, 今天我花了: %f" % (name , set_up_year ,stock_price)
message1 = "我是: %s 我的出生年份是 : %7d, 今天我花了: %7.2f" % (name , set_up_year ,stock_price)
message2 = "我是: %s 我的出生年份是 : %3d, 今天我花了: %.1f" % (name , set_up_year ,stock_price)
print(message)
print(message1)
print(message2)

print(f"我是: {name} 我的出生年份是 : {set_up_year}, 今天我花了: {stock_price}")






