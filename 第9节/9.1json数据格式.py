import json
# 列表转json
data = [{"name":"萧","age":"16"},{"name":"林","age":"14"},{"name":"牧","age":"18"}]

# 把列表转化为json字符串
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

json_str = json.dumps(data,ensure_ascii=False)  # 中文转换编码问题的解决
print(json_str)
print(type(json_str))

# 字典转json
dict = {"name":'石',"age":5000}
json_str1 = json.dumps(dict,ensure_ascii=False)
print(json_str1)
print(type(json_str1))

# json字符串转python
data1 = '[{"name":"萧","age":"16"},{"name":"林","age":"14"},{"name":"牧","age":"18"}]'
py_list = json.loads(data1)
print(py_list)
print(type(py_list))

dict2 = '{"name":"石","age":5000}'
py_dict = json.loads(dict2)
print(py_dict)
print(type(py_dict))