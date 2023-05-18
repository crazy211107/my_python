from pyecharts.charts import Map, Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *
import json


def chooser_sort_key(element):
    return element[1]


f = open("D:/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
lines = f.readlines()
lines.pop(0)  # 删除第一行数据
# 将数据转为字典存储
#  { 年份: [[国家, gdp], [国家, gdp], ...],年份: [[国家, gdp], [国家, gdp], ...], ...}
#  {1960: [[美国, 123], [中国,1234]], 1971:[[美国, 123], [中国,1234]]}

data_dict = {}

for line in lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    try:
        data_dict[year].append((country, gdp))
    except KeyError:
        data_dict[year] = []
        data_dict[year].append((country, gdp))

# print(data_dict)

# 排序年份
sorted_year_list = sorted(data_dict.keys())
# print(data_dict.keys())

timeline = Timeline({"theme": ThemeType.LIGHT})
# 对每个年份内的国家的gdp进行排序
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8]  # 取前八个年份
    print(year_data)
    countrys = []
    gdps = []
    for country_gdp in year_data:
        countrys.append(country_gdp[0])
        # 以亿元作为单位
        gdps.append(int(country_gdp[1] / 100000000))
    bar = Bar()
    countrys.reverse()
    gdps.reverse()
    # 设置标题
    bar.set_global_opts(title_opts=TitleOpts(title=f"{year}年全球前8 GDP国家"))
    bar.add_xaxis(countrys)
    bar.add_yaxis("GDP(亿)", gdps, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    timeline.add(bar, str(year))
# 设置自动播放
timeline.add_schema(
    play_interval=1000,  # 自动播放时间间隔
    is_timeline_show=True,  # 是否在自动播放时 显示时间线
    is_auto_play=True,   # 是否自动播放
    is_loop_play=True    # 是否循环播放
)
timeline.render("1960-2019全球GDP前8国家.html")














