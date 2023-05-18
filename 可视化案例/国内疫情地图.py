from pyecharts.charts import Map
from pyecharts.options import *
import json


# 读取文件数据
f = open("D:/疫情.txt", encoding="UTF-8")
data = f.read()

f.close()
# 取到各省的数据
# 将json数据 转换为python的基础字典数据
data_dict = json.loads(data)
# 取出 各省份的数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组() 作为列表[]的元素
data_list = []

for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name+"省", province_confirm))

print(data_list)

# 创建地图
virus_map = Map()
virus_map.add("各省份确诊人数", data_list, "china")
# 设置全局配置
virus_map.set_global_opts(
    title_opts= TitleOpts(title="全国疫情地图"),
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
# 绘图
virus_map.render("全国疫情地图.html")





