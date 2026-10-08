import sqlite3
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import errors

#闭卷复习
load_dotenv()
def query(sql,conn,params: tuple = ()) -> pd.DataFrame:
    df = pd.read_sql_query(sql,conn,params = params or ())
    return df
data = [
    {"日期": "2025-01-15", "地区": "华东", "产品": "iPhone 15", "金额": 5999},
    {"日期": "2025-01-15", "地区": "华北", "产品": "MacBook Pro", "金额": 12999},
    {"日期": "2025-01-16", "地区": "华南", "产品": "AirPods Pro", "金额": 1899},
    {"日期": "2025-01-16", "地区": "华东", "产品": "iPad Air", "金额": 4599},
    {"日期": "2025-01-17", "地区": "西南", "产品": "显示器", "金额": 2999},
    {"日期": "2025-01-17", "地区": "华北", "产品": "iPhone 15", "金额": 5999},
    {"日期": "2025-01-18", "地区": "华南", "产品": "MacBook Pro", "金额": 12999},
    {"日期": "2025-01-18", "地区": "华中", "产品": "AirPods Pro", "金额": 1899},
    {"日期": "2025-01-19", "地区": "华东", "产品": "iPad Air", "金额": 4599},
    {"日期": "2025-01-19", "地区": "西北", "产品": "显示器", "金额": 2999},
    {"日期": "2025-01-20", "地区": "华北", "产品": "iPhone 15", "金额": 5999},
    {"日期": "2025-01-20", "地区": "华南", "产品": "MacBook Pro", "金额": 12999},
    {"日期": "2025-01-21", "地区": "华东", "产品": "AirPods Pro", "金额": 1899},
    {"日期": "2025-01-21", "地区": "西南", "产品": "iPad Air", "金额": 4599},
    {"日期": "2025-01-22", "地区": "华中", "产品": "显示器", "金额": 2999},
    {"日期": "2025-01-22", "地区": "华北", "产品": "iPhone 15", "金额": 5999},
    {"日期": "2025-01-23", "地区": "华南", "产品": "AirPods Pro", "金额": 1899},
    {"日期": "2025-01-23", "地区": "华东", "产品": "MacBook Pro", "金额": 12999},
    {"日期": "2025-01-24", "地区": "西南", "产品": "iPad Air", "金额": 4599},
    {"日期": "2025-01-24", "地区": "西北", "产品": "显示器", "金额": 2999},
]
df = pd.DataFrame(data)
df.to_csv("sales.csv",index = False,encoding = "utf-8")
df1 = pd.read_csv("sales.csv")
conn_sqlite = sqlite3.connect("sales.db")
cursor = conn_sqlite.cursor()
df1.to_sql("sales",conn_sqlite,if_exists = "replace",index = False)
df2 = query("SELECT * FROM sales WHERE 地区 = ?",conn_sqlite,('华北',))
print(df2)
df3 = query("SELECT * FROM sales",conn_sqlite,())
print(df3)
conn_sqlite.close()

conn_pg = psycopg2.connect(
    host = os.getenv("DB_HOST"),
    port = int(os.getenv("DB_PORT")),
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD")
)
print("PostgreSQL连接成功")
cursor_pg = conn_pg.cursor()
cursor_pg.execute("""
CREATE TABLE IF NOT EXISTS sales(
   id SERIAL PRIMARY KEY,
   日期 DATE NOT NULL,
   地区 VARCHAR(50) NOT NULL,
   产品 VARCHAR(50) NOT NULL,
   金额 NUMERIC(10,2) NOT NULL
)
""")
try:
   cursor_pg.execute("SELECT * FROM sales GROUP BY 地区")
   print(cursor_pg.fetchall())
except errors.GroupingError as e:
   print(f"分组错误: {e}")

#跟练项目
load_dotenv()
db_host = os.getenv("DB_HOST")
db_port = int(os.getenv("DB_PORT"))
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

user_data = [
    ("张三", "北京", 28),
    ("李四", "上海", 35),
    ("王五", "北京", 22),
    ("赵六", "广州", 35),   # 注意：李四和赵六同龄
    ("孙七", "上海", 40)
]

order_data = [
    (1, "笔记本电脑", 5999.00, "2026-10-01"),
    (1, "鼠标", 99.00, "2026-10-02"),
    (2, "显示器", 1299.00, "2026-10-01"),
    (2, "键盘", 299.00, "2026-10-03"),
    (3, "耳机", 199.00, "2026-10-02"),
    (4, "平板电脑", 3999.00, "2026-10-04"),
    (4, "保护壳", 49.00, "2026-10-04"),
    (5, "服务器", 19999.00, "2026-10-05")
]
conn1 = psycopg2.connect(
    host = db_host,
    port = db_port,
    dbname = db_name,
    user = db_user,
    password = db_password
)
print("连接成功")
cursor1 = conn1.cursor()

cursor1.execute("DROP TABLE IF EXISTS users CASCADE")
cursor1.execute("DROP TABLE IF EXISTS orders CASCADE")
cursor1.execute("""
CREATE TABLE IF NOT EXISTS users(
     id SERIAL PRIMARY KEY,
     name VARCHAR(50) NOT NULL,
     city VARCHAR(50) NOT NULL,
     age INTEGER NOT NULL
)
""")

cursor1.execute("""
CREATE TABLE IF NOT EXISTS orders(
     id SERIAL PRIMARY KEY,
     user_id INTEGER NOT NULL,  
     product VARCHAR(50) NOT NULL,
     amount NUMERIC(10,2) NOT NULL,
     order_date DATE
)
""")
conn1.commit()

cursor1.executemany("INSERT INTO users (name,city,age) VALUES (%s,%s,%s)",user_data)
cursor1.executemany("INSERT INTO orders (user_id,product,amount,order_date) VALUES (%s,%s,%s,%s)",order_data)
conn1.commit()

cursor1.execute("SELECT * FROM users")
while True:
    row = cursor1.fetchone()
    if row is None:
        break
    print(row)
    
cursor1.execute("SELECT * FROM orders WHERE order_date > %s AND amount > %s",('2026-10-03',3000))
print(cursor1.fetchall())

cursor1.execute("""
     SELECT u.id,u.name,SUM(o.amount) AS 总金额
     FROM users u
     JOIN orders o ON u.id = o.user_id
     GROUP BY u.id,u.name
     ORDER BY 总金额 DESC
""")
print(cursor1.fetchall())
conn1.close()
cursor1.close()
#项目
users_data = [
    (1, '张三'),
    (2, '李四'),
    (3, '王五'),
    (4, '赵六'),
]

products_data = [
    (1, 'iPhone 15', 5999.0, 50),
    (2, 'MacBook Pro', 12999.0, 20),
    (3, 'iPad Air', 3999.0, 30),
    (4, 'AirPods', 999.0, 100),
]

orders_data = [
    # (id, date, user_id, product_id, amount, quantity)
    (1, '2024-01-15', 1, 1, 5999.0 * 2, 2),     # 张三买2个iPhone
    (2, '2024-01-16', 1, 3, 3999.0 * 1, 1),     # 张三买1个iPad
    (3, '2024-01-17', 2, 2, 12999.0 * 1, 1),    # 李四买1个MacBook
    (4, '2024-01-18', 3, 4, 999.0 * 3, 3),      # 王五买3个AirPods
    (5, '2024-01-19', 2, 1, 5999.0 * 1, 1),     # 李四买1个iPhone
    (6, '2024-01-20', 4, 3, 3999.0 * 2, 2),     # 赵六买2个iPad
]

def get_connection(host: str,port:int,dbname: str,user: str,password: str) -> psycopg2.extensions.connection:
    conn = psycopg2.connect(
        host = host,
        port = port,
        dbname = dbname,
        user = user,
        password = password
    )
    return conn

def query_sales(sql: str,conn,params: tuple = ()) -> list:
    with conn.cursor() as cur:
       cur.execute(sql,params or ())
       rows = cur.fetchall()
    return rows if rows else []

def get_customer(sql: str,conn,params: tuple = ()) -> tuple|None:
    with conn.cursor() as cur:
       cur.execute(sql,params or ())
       return cur.fetchone()

def get_order(sql: str,conn,params: tuple = ()) -> tuple|None:
    with conn.cursor() as cur:
       cur.execute(sql,params or ())
       return cur.fetchone
    
conn2 = get_connection(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)
cursor2 = conn2.cursor()

cursor2.execute("DROP TABLE IF EXISTS proj_orders CASCADE")
cursor2.execute("DROP TABLE IF EXISTS proj_products CASCADE")
cursor2.execute("DROP TABLE IF EXISTS proj_users CASCADE")
conn2.commit()

cursor2.execute("""
CREATE TABLE IF NOT EXISTS proj_users(
   id SERIAL PRIMARY KEY,
   name VARCHAR(50) NOT NULL
)
""")

cursor2.execute("""
CREATE TABLE IF NOT EXISTS proj_products(
   id SERIAL PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   prize NUMERIC(10,2) NOT NULL,
   stock INTEGER NOT NULL
)
""")

cursor2.execute("""
CREATE TABLE IF NOT EXISTS proj_orders(
   id SERIAL PRIMARY KEY,
   date DATE NOT NULL,
   user_id INTEGER REFERENCES proj_users(id),
   product_id INTEGER REFERENCES proj_products(id),
   amount NUMERIC(10,2) NOT NULL,
   quantity INTEGER NOT NULL
)
""")
conn2.commit()

cursor2.executemany("INSERT INTO proj_users (id,name) VALUES (%s,%s)",users_data)
cursor2.executemany("INSERT INTO proj_products (id,name,prize,stock) VALUES (%s,%s,%s,%s)",products_data)
cursor2.executemany("INSERT INTO proj_orders (id,date,user_id,product_id,amount,quantity) VALUES (%s,%s,%s,%s,%s,%s)",orders_data)
conn2.commit()

result = query_sales("SELECT u.name,u.id,COUNT(o.id),SUM(o.amount) FROM proj_users u JOIN proj_orders o ON u.id = o.user_id GROUP BY u.name,u.id",conn2,())
print(f"查询1: {result}")
result1 = query_sales("SELECT p.id,SUM(o.quantity),AVG(o.amount) FROM proj_products p JOIN proj_orders o ON p.id = o.product_id GROUP BY p.id ORDER BY AVG(o.amount) DESC",conn2,())
print(result1)
result2 = get_customer("SELECT * FROM proj_users WHERE id = %s",conn2,(1,))
print(result2)
result3 = get_order("SELECT * FROM proj_orders WHERE id = %s",conn2,(2,))
print(result3)
conn2.close()
cursor2.close()
