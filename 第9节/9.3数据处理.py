import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts, LegendOpts, ToolboxOpts, VisualMapOpts

f_us = open("C:/Users/THE KEY/Desktop/可视化案例数据/折线图数据/美国.txt","r",encoding="UTF-8")
us_data = f_us.read()
f_jp = open("C:/Users/THE KEY/Desktop/可视化案例数据/折线图数据/日本.txt","r",encoding="UTF-8")
jp_data = f_jp.read()
f_in = open("C:/Users/THE KEY/Desktop/可视化案例数据/折线图数据/印度.txt","r",encoding="UTF-8")
in_data = f_in.read()

us_data = us_data.replace("jsonp_1629344292311_69436(","")
jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
in_data = in_data.replace("jsonp_1629350745930_63180(","")
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

us_x_data = us_trend_data['updateDate'][0:314]
jp_x_data = jp_trend_data['updateDate'][0:314]
in_x_data = in_trend_data['updateDate'][0:314]

us_y_data = us_trend_data['list'][0]['data'][0:314]
jp_y_data = jp_trend_data['list'][0]['data'][0:314]
in_y_data = in_trend_data['list'][0]['data'][0:314]

line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts = TitleOpts(title="三国确诊人数折线图",pos_left='center',pos_bottom='1%'),
    legend_opts = LegendOpts(is_show=True),
    toolbox_opts = ToolboxOpts(is_show=True),
    # visualmap_opts = VisualMapOpts(is_show=True)
)

line.render()

f_us.close()
f_jp.close()
f_in.close()