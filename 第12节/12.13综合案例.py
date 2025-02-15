from data_define import Record, FileReader, TextFileReader, JsonFileReader
from pyecharts.charts import Bar
from pyecharts.options import *

text_file_reader = TextFileReader("C:/Users/THE KEY/Desktop/可视化案例数据/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("C:/Users/THE KEY/Desktop/可视化案例数据/2011年2月销售数据JSON.txt")

jan_data:list[Record] = text_file_reader.read_data()
feb_data:list[Record] = json_file_reader.read_data()

# 合并存储
all_data: list[Record] = jan_data + feb_data

# 开始进行数据计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date]  += record.money
    else:
        data_dict[record.date] = record.money

print(data_dict)

# 可视化图标开发
bar = Bar(init_opts=InitOpts())

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()),label_opts=LabelOpts(is_show= False))
bar.set_global_opts(
    title_opts = TitleOpts(title="每日销售额")
)

bar.render()