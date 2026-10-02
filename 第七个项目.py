import sqlite3
import pandas as pd
#闭卷复习
def get_connection(db_path: str):
    conn = sqlite3.connect(db_path)
    return conn

def query(sql,conn,parameters: tuple):
    df = pd.read_sql_query(sql,conn,parameters)
    return df

#跟练项目
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON;")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY,
     name TEXT NOT NULL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
     id INTEGER PRIMARY KEY,
     price REAL NOT NULL,
     stock INTEGER NOT NULL,
     name TEXT NOT NULL 
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
     id INTEGER PRIMARY KEY,
     user_id INTEGER NOT NULL,
     product_id INTEGER NOT NULL,
     amount REAL NOT NULL,
     date TEXT NOT NULL,
     FOREIGN KEY(product_id) REFERENCES products(id),
     FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

#项目
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON;")

cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS products")

users_data = [
    (1, '张三'),
    (2, '李四'),
    (3, '王五'),
    (4, '赵六'),
]

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL
)
""")
cursor.executemany("INSERT OR IGNORE INTO users (id,name) VALUES(?,?)",users_data)
conn.commit()

products_data = [
    (1, 'iPhone 15', 5999.0, 50),
    (2, 'MacBook Pro', 12999.0, 20),
    (3, 'iPad Air', 3999.0, 30),
    (4, 'AirPods', 999.0, 100),
]

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      price REAL NOT NULL,
      stock INTEGER NOT NULL
)
""")
cursor.executemany("INSERT OR IGNORE INTO products (id,name,price,stock) VALUES (?,?,?,?)",products_data)
conn.commit()

orders_data = [
    # (id, date, user_id, product_id, amount, quantity)
    (1, '2024-01-15', 1, 1, 5999.0 * 2, 2),     # 张三买2个iPhone
    (2, '2024-01-16', 1, 3, 3999.0 * 1, 1),     # 张三买1个iPad
    (3, '2024-01-17', 2, 2, 12999.0 * 1, 1),    # 李四买1个MacBook
    (4, '2024-01-18', 3, 4, 999.0 * 3, 3),      # 王五买3个AirPods
    (5, '2024-01-19', 2, 1, 5999.0 * 1, 1),     # 李四买1个iPhone
    (6, '2024-01-20', 4, 3, 3999.0 * 2, 2),     # 赵六买2个iPad
]

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
      id INTEGER PRIMARY KEY,
      date TEXT NOT NULL,
      user_id INTEGER NOT NULL,
      product_id INTEGER NOT NULL,
      amount REAL NOT NULL,
      quantity INTEGER NOT NULL,
      FOREIGN KEY(user_id) REFERENCES users(id),
      FOREIGN KEY(product_id) REFERENCES products(id)
)
""")
cursor.executemany("INSERT OR IGNORE INTO orders (id,date,user_id,product_id,amount,quantity) VALUES (?,?,?,?,?,?)",orders_data)
conn.commit()

#客户的订单以及花的钱
df = pd.read_sql_query("""
    SELECT u.name,o.id,o.amount
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id
""",conn)
print(df)
#哪个商品卖的最好
df1 = pd.read_sql_query("""
     SELECT p.name,SUM(o.quantity) AS 总销量
     FROM products p
     INNER JOIN orders o ON p.id = o.product_id
     GROUP BY p.id,p.name
     ORDER BY 总销量 DESC 
""",conn)
print(df1)
#UPDATE一条数据
cursor.execute("SELECT * FROM products WHERE stock > 30")
print("即将更新的信息")
for row in cursor.fetchall():
    print(f" {row}")

cursor.execute("UPDATE products SET price = price * 0.9 WHERE stock > 30")
print(f"实际更新了{cursor.rowcount}行数据")
conn.commit()

cursor.execute("SELECT price FROM products WHERE stock > 30")
print("更新后的数据")
for row in cursor.fetchall():
    print(row)
#DELECT一条数据
cursor.execute("SELECT * FROM orders WHERE quantity < 2")
print("即将删除的信息")
for row in cursor.fetchall():
    print(row)

cursor.execute("DELETE FROM orders WHERE quantity < 2")
print(f"实际删除了{cursor.rowcount}行数据")
conn.commit()

cursor.execute("SELECT * FROM orders WHERE quantity < 2")
print("删除后的数据")
for row in cursor.fetchall():
    print(row)