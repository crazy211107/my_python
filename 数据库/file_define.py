import json

from data_define import Record

"""
关于文件操作的类
"""


# 先定义一个抽象类做顶层设计，确定有什么功能
class FileReader:

    def read_data(self) -> list[Record]:
        """
        读取文件数据  有.txt 和json文件  读取的每一条数据转换为Record数据，封装为list返回
        :return:
        """
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()  # 消除读取到的每一行数据的 \n
            data_list = (line.split(","))
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
            '''
            。 strip()该函数将从原始字符串的开头和结尾删除给定的字符。
            默认情况下，函数strip()将删除字符串开头和结尾的空格，并返回前后不带空格的相同字符串。
            '''
        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_list = json.loads(line)
            record = Record(data_list["date"], data_list["order_id"], int(data_list["money"]), data_list["province"])
            record_list.append(record)
            '''
            。 strip()该函数将从原始字符串的开头和结尾删除给定的字符。
            默认情况下，函数strip()将删除字符串开头和结尾的空格，并返回前后不带空格的相同字符串。
            '''
        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("D:\\python\\python\\2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("D:\\python\\python\\2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)
