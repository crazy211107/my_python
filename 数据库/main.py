from file_define import *
from data_define import Record
from pyecharts.charts import Map, Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *
import json
from pymysql import Connection

text_file_reader = TextFileReader("D:\\python\\python\\2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:\\python\\python\\2011年2月销售数据JSON.txt")
jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 把两个月数据合二为一

all_data: list[Record] = jan_data + feb_data

# 获取到mysql数据库的的链接对象
conn = Connection(
    host='localhost',  # 主机名 或者IP地址
    port=3306,
    user='root',
    password='1234',
    autocommit=True  # 设置自动commit

)
cursor = conn.cursor()
conn.select_db("py_sql")

my_file = open("D:\\date.txt", 'w', encoding="UTF-8")

# for record in all_data:
#     sql = f"insert into orders(order_date, order_id, money, province)" \
#           f"values('{record.data}','{record.order_id}',{record.money},'{record.province}')"
#     # 执行sql语句
#     cursor.execute(sql)
sql2 = f"select * from orders "

cursor.execute(sql2)
result: tuple = cursor.fetchall()

for line in result:
    my_dic: dict = {'date': line[0].strftime("%Y-%m-%d"), 'order_id': line[1], 'money': line[2], 'province': line[3]}
    my_json = json.dumps(my_dic, ensure_ascii=False)
    my_file.write(my_json)
    my_file.write('\n')
    # my_str = f"'{line[0]}','{line[1]}','{line[2]}','{line[3]}'\n"
    # print(my_dic)

conn.close()
my_file.flush()
my_file.close()