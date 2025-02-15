from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map1 = Map()

data = [
    ("北京市",5),   # 省份加相关数值
    ("上海市",18),
    ("湖南省",85),
    ("台湾省",1),
    ("广东省",188)
]
map1.add("测试地图", data, "china")

map1.set_global_opts(
    visualmap_opts = VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#FF0000"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#0000CD"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#00EE00"}


        ]
    )

)

map1.render()