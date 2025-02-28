# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 得到折线对象
line = Line()
#添加x轴数据
line.add_xaxis(['中国','美国','法国','英国'])
#添加y轴数据
line.add_yaxis('power',[87,80,60,65])

# 全局配置选项
line.set_global_opts(
    title_opts = TitleOpts(title = '力量对比',pos_left='center',pos_bottom='1%'),
    legend_opts = LegendOpts(is_show=True),
    toolbox_opts = ToolboxOpts(is_show=True),
    visualmap_opts = VisualMapOpts(is_show=True)
)

# 通过render方法，将代码生成图像
line.render()