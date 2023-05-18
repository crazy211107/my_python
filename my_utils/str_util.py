
def str_reverse(s):
    return s[::-1]


def sub_str(s, x, y):
    return s[x:y:1]


# 测试功能
if __name__ == '__main__':
    print(str_reverse("源小宝真可爱"))

    print(sub_str("源小宝真可爱", 1, 3))
