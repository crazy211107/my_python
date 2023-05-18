from pymysql import Connection

# 获取到mysql数据库的的链接对象
conn = Connection(
    host='localhost',  # 主机名 或者IP地址
    port=3306,
    user='root',
    password='1234',
    autocommit=True # 设置自动commit

)
# 打印mysql的软件信息
print(conn.get_server_info())
# 获取游标对象
cursor = conn.cursor()
conn.select_db("mybatis") # 选择数据库
# 使用游标对象执行sql语句

cursor.execute("insert into tb_brand (brand_name,company_name,ordered,description,status) values('新东方', "
               "'新东方是学习厨艺和英语的地方',13,'快来看看',1)")
cursor.execute("select * from tb_brand order by ordered limit 5, 10")
result: tuple = cursor.fetchall()
for r in result:
    print(r)
# 关闭数据库您的链接
conn.close()





