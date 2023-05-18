import json
from pyecharts.charts import Line
from pyecharts.options import AxisOpts, InitOpts, LabelOpts, TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, \
    TooltipOpts

# 处理数据
f_us = open("D:\\python\\python\\美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
f_jp = open("D:\\python\\python\\日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()
f_in = open("D:\\python\\python\\印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()

# 去掉不符合json规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

# 去掉不符合json规范的结尾 默认从-2开始截，到文件开头  默认步长为1
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# json 转python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend key

us_trend_key = us_dict['data'][0]['trend']
jp_trend_key = jp_dict['data'][0]['trend']
in_trend_key = in_dict['data'][0]['trend']

# 获取日期信息 用于x轴，取2020 到314下标为止
us_x_data = us_trend_key['updateDate'][:314]
jp_x_data = jp_trend_key['updateDate'][:314]
in_x_data = in_trend_key['updateDate'][:314]

# 获取确认信息 用于y轴，取2020 到314下标为止

us_y_date = us_trend_key['list'][0]['data'][:314]
jp_y_date = jp_trend_key['list'][0]['data'][:314]
in_y_date = in_trend_key['list'][0]['data'][:314]

line = Line(init_opts=InitOpts(width="1400px", height="800px"))

# 添加x轴信息  x轴是共用的 使用一个国家即可
line.add_xaxis(us_x_data)
# 添加y轴信息                                            不显示标签信息
line.add_yaxis("美国确诊人数", us_y_date, label_opts=LabelOpts(is_show=False), symbol_size=10)
line.add_yaxis("日本确诊人数", jp_y_date, label_opts=LabelOpts(is_show=False), symbol_size=10)
line.add_yaxis("印度确诊人数", in_y_date, label_opts=LabelOpts(is_show=False), symbol_size=10)
# 设置全局配置项
line.set_global_opts(
    # 设置图标题和位置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    xaxis_opts=AxisOpts(name="时间"),  # 轴标题
    yaxis_opts=AxisOpts(name="累计确诊人数")
)

# render()生成图表
line.render()
f_us.close()
f_jp.close()
f_in.close()
