from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()

bar.add_xaxis(["中国","美国","法国"])
bar.add_yaxis("GDP",[80,90,60],label_opts=LabelOpts(position="right"))

# x，y轴反转
bar.reversal_axis()

#添加数据


bar.render()
