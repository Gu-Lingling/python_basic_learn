from pyecharts.charts import Bar,Timeline
from pyecharts.options import*
from pyecharts.globals import ThemeType

f = open("C:/Users/THE KEY/Desktop/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines = f.read()
f.close()

#print(data_lines)
# data_lines.pop(0) #删除第一行数据

# 将数据转为字典存储
data_dict = {}
#print(data_lines)\
data_lines = data_lines.split('\n')
for line in data_lines:
    #print(line)
    line = line.split(",")
    # print(line)
    # print(line,end='')
    # year = int(line.split(",")[0])
    year = int(line[0])
    # print(year)
    country = line[1]
    # print(country)
    gdp = float(line[2])
    # print(type(gdp))
    # print(gdp)

    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country,gdp])

# print(data_dict)

# 导入时间线
timeline = Timeline({"theme": ThemeType.DARK})
# 排序年份
sorted_year_list = sorted(data_dict.keys())
#print(sorted_year_list)

for year in sorted_year_list:
    # print(year)
    data_dict[year].sort(key=lambda element:element[1],reverse=True)
    # 取出本年份前十名
    year_data = data_dict[year][0:10]
    # print(year_data)
    x_data = []
    y_data = []
    for country_gdp in year_data:

        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/100000000)

    bar = Bar()
    #print(x_data)
    #x_data = x_data[10::-1]
    #y_data = y_data[10::-1]

    x_data.reverse()
    # print(x_data)
    y_data.reverse()


    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))

    bar.reversal_axis()

    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球GDP前十国家数据")
        )

    timeline.add(bar,str(year))

# 时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render("1960-2019全球GDP前十国家一览.html")