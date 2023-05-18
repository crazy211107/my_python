"""
文件处理相关的工具模块
"""


def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        context = f.read()
        print("文件的全部内容如下:")
        print(context)
    except Exception as e:
        print(f"程序出现了异常，原因是:{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
#    f.write("\n")
    f.write(data)
    f.write("\n")
    f.flush()
    f.close()


if __name__ == '__main__':
    print_file_info("D:/bill.txt")
#   append_to_file("D:/bill.txt", "我好想爱你个")
