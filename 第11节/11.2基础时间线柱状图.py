from pyecharts.charts import Bar
from pyecharts.charts import Timeline
from pyecharts.options import*
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国","美国","法国"])
bar1.add_yaxis("GDP",[60,80,70],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国","美国","法国"])
bar2.add_yaxis("GDP",[75,85,75],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国","美国","法国"])
bar3.add_yaxis("GDP",[88,93,80],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 创建时间线对象
timeline = Timeline({"theme":ThemeType.WONDERLAND})

# 本质是生成了一个x轴
timeline.add(bar1,"2021年GDP")
timeline.add(bar2,"2022年GDP")
timeline.add(bar3,"2023年GDP")

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render()