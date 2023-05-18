from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [("北京市", 99),
        ("上海市", 199),
        ("湖南省", 299),
        ("贵州省", 399),
        ("四川省", 499),
        ("广东省", 599),
        ("江西省", 699)
        ]
map.add("地图", data, "china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
            {"min": 100, "max": 499, "label": "99-499人", "color": "#FF9966"},
            {"min": 500, "max": 999, "label": "499-999人", "color": "#FF6666"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#CC3333"},
            {"min": 10000,  "label": "10000以上", "color": "#990033"}
        ]
    )

)

map.render()