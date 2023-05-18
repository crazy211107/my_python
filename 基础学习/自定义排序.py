
"""
当列表有了 列表作为元素  就要指定排序方法 指定是按照谁来排序


"""
# 带名形式
my_list = [["e", 33], ["a", 55], ["c", 11]]


def chooser_sort_key(element):
    return element[1]


# my_list.sort(key=chooser_sort_key, reverse=True) # True为降序
print(my_list)

# 匿名函数 lambda函数
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)

