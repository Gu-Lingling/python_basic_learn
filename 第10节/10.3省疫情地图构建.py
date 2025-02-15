import json
from pyecharts.charts import Map
from pyecharts.options import*

f = open("C:/Users/THE KEY/Desktop/可视化案例数据/地图数据/疫情.txt","r",encoding="UTF-8")
data = f.read()
f.close()

data_dict = json.loads(data)

cities_data = data_dict["areaTree"][0]["children"][7]["children"]

data_list = []
for city_data in cities_data:
    city_name = city_data["name"]+"市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name,city_confirm)) #构建好元组，存放于列表之中

data_list.append(('云浮市',1))   # 手动添加一份数据，（txt里没有）
print(data_list)

map1 = Map()
map1.add("广东省疫情分布",data_list,"广东")

map1.set_global_opts(
    title_opts=TitleOpts(title="各市疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,       #是否显示
        is_piecewise=True,  #是否分段
        pieces=[
            {"min":1,"max":9,"label":"1~9人","color":"#FFE4C4"},
            {"min":10,"max":29,"label":"10~29人","color":"#6495ED"},
            {"min":30,"max":69,"label":"30~69人","color":"#EEB422"},
            {"min":70,"max":199,"label":"70~199人","color":"#CD5555"},
            {"min":200,"label":">200人","color":"#990033"}
        ]

    )
)

map1.render()