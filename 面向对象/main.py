from file_define import *
from data_define import Record
from pyecharts.charts import Map, Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *
import json


text_file_reader = TextFileReader("D:\\python\\python\\2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:\\python\\python\\2011年2月销售数据JSON.txt")
jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 把两个月数据合二为一

all_data: list[Record] = jan_data + feb_data

# 进行数据计算   通过遍历all_list  使用字典 存储每一日的总的销售额  没有则新加  有则相加
# {"2011-01-01": 1234, "2011-01-02": 34}
data_list = {}

for record in all_data:
    if record.data in data_list.keys():
        data_list[record.data] += record.money
    else:
        data_list[record.data] = record.money
print(data_list)


bar = Bar(init_opts= InitOpts(theme=ThemeType.LIGHT))

bar.add_yaxis("销售额", list(data_list.values()), label_opts=LabelOpts(is_show=False))
bar.add_xaxis(list(data_list.keys()))

bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")


