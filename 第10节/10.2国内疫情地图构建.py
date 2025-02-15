import json
from pyecharts.charts import Map
from pyecharts.options import*
f = open("C:/Users/THE KEY/Desktop/可视化案例数据/地图数据/疫情.txt","r",encoding="UTF-8")
data = f.read()
f.close()

data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]

data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
# 加后缀
    if province_name == "香港":
        province_name = province_name + '特别行政区'
    elif province_name == "澳门":
        province_name = province_name + '特别行政区'
    elif province_name == '北京':
        province_name = province_name + '市'
    elif province_name == '天津':
        province_name = province_name + '市'
    elif province_name == '上海':
        province_name = province_name + '市'
    elif province_name == '重庆':
        province_name = province_name + '市'
    elif province_name == '内蒙古':
        province_name = province_name + '自治区'
    elif province_name == '新疆':
        province_name = province_name + '维吾尔自治区'
    elif province_name == '广西':
        province_name = province_name + '壮族自治区'
    elif province_name == '西藏':
        province_name = province_name + '自治区'
    elif province_name == '宁夏':
        province_name = province_name + '回族自治区'
    else:
        province_name = province_name + '省'

    print(province_name)
    # print(type(province_name))
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))



map1 = Map()
#重要用法
map1.add("各省份确诊人数",data_list,"china")

map1.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,       #是否显示
        is_piecewise=True,  #是否分段
        pieces=[
            {"min":1,"max":99,"label":"1~99人","color":"#FDF5E6"},
            {"min":100,"max":499,"label":"100~499人","color":"#FFFFE0"},
            {"min":500,"max":999,"label":"500~999人","color":"#CDBE70"},
            {"min":1000,"max":4999,"label":"1000~4999人","color":"#FFB90F"},
            {"min":5000,"max":9999,"label":"5000~9999人","color":"#FF6A6A"},
            {"min":10000,"label":">10000人","color":"#B22222"}
        ]

    )
)

map1.render()