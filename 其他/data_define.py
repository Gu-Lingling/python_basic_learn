import json
"""
数据定义的类
"""
class Record:
    def __init__(self,date,order_id,money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f"{self.date},{self.order_id},{self.money},{self.province}"
"""
和文件相关的类
"""
class FileReader:
    def read_data(self) ->list[Record]:
        # 读取文件的数据，把每一条数据都转换为Record对象，将它们封装到list内返回
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")

        record_list = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path
    def read_data(self) ->list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"],data_dict["order_id"],data_dict["money"],data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if  __name__ == '__main__':
    text_file_reader = TextFileReader("C:/Users/THE KEY/Desktop/可视化案例数据/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("C:/Users/THE KEY/Desktop/可视化案例数据/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

