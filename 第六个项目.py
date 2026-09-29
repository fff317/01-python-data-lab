#项目
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

def get_connection(db_path):
    conn = sqlite3.connect(db_path)
    return conn

conn = get_connection("sales_db")
cursor = conn.cursor()
df1.to_sql("sales",conn,if_exists = "replace",index = False)

def query(sql,conn,params = None):
    df = pd.read_sql_query(sql,conn,params = params or ())
    return df
#按条件筛选
df2 = query("SELECT * FROM sales LIMIT 5",conn)
print(df2)
df3 = query("SELECT * FROM sales WHERE 金额 > ?",conn,(3000,))
print(df3)
df4 = query("SELECT 地区,产品 FROM sales WHERE 地区 = ? AND 金额 > ?",conn,("华东",3000))
print(df4)
#排序
df5 = query("SELECT * FROM sales ORDER BY 金额 DESC",conn)
print(df5)
df6 = query("SELECT * FROM sales ORDER BY 日期 ASC",conn)
print(df6)
#分组统计
df7 = query("SELECT 地区 FROM sales GROUP BY 地区",conn)
print(df7)
df8 = query("SELECT 地区,产品,AVG(金额) AS 平均金额 FROM sales GROUP BY 地区,产品 HAVING AVG(金额) > ? ORDER BY AVG(金额)",conn,(3000,))
print(df8)
#聚合函数
df9 = query("SELECT COUNT(*) AS 总记录数,SUM(金额) AS 总金额,AVG(金额) AS 平均金额",conn)
print(df9)
#条件筛选
df10 = query("SELECT SUM(CASE WHEN 地区 = ? THEN 金额 ELSE 0 END)",conn,('华南',))
print(df10)
df11 = query("SELECT COUNT(CASE WHEN 地区 = ? AND 金额 > ? THEN 1 END)",conn,('华北',3000))
print(df11)