from pyecharts.charts import Map, Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *
import json
# 读取文件数据
f = open("D:/疫情.txt", encoding="UTF-8")
data = f.read()

f.close()

# 取到各省的数据
# 将json数据 转换为python的基础字典数据
data_dict = json.loads(data)
# 取出 河南省份的数据
cities_data_list = data_dict["areaTree"][0]["children"][3]["children"]
# 组装每个省份和确诊人数为元组() 作为列表[]的元素
data_list = []

for city_data in cities_data_list:
    city_name = city_data["name"]+"市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))

# 手动添加济源市数据
data_list.append(("济源市", 5))

virus_map = Map()
virus_map.add("河南省疫情分布", data_list, "河南")


# 设置全局配置
virus_map.set_global_opts(
    title_opts= TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,  # 是否分段
        pieces=[  # 自定义分段
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "99-499人", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "499-999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
            {"min": 10000, "label": "10000以上", "color": "#990033"}
        ]

    )

)

bar = Bar()

# 添加x轴数据
bar.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(
    position="right"  # 设置在右侧显示
))
# 反转xy轴
bar.reversal_axis()


bar1 = Bar()

# 添加x轴数据
bar1.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
bar1.add_yaxis("GDP", [50, 30, 20], label_opts=LabelOpts(
    position="right"  # 设置在右侧显示
))
# 反转xy轴
bar1.reversal_axis()

# 创建时间线对象
timeline = Timeline(
    {"theme": ThemeType.LIGHT}
)
# 添加bar柱状图

timeline.add(bar, "2021年GPT")
timeline.add(bar1, "2022年GPT")
timeline.add(virus_map, "全国疫情地图")
# 设置自动播放
timeline.add_schema(
    play_interval=3000,  # 自动播放时间间隔
    is_timeline_show=True,  # 是否在自动播放时 显示时间线
    is_auto_play=True,   # 是否自动播放
    is_loop_play=True    # 是否循环播放
)

# 通过时间线绘图
timeline.render("基础时间线.html")

