#项目
import pandas as pd
from pandas import DataFrame,Series

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
df.to_csv("data.csv",index = False,encoding = "utf-8")
df1 = pd.read_csv("data.csv")
def area_sale(df: DataFrame) -> str:
    df1 = df.groupby("地区")["金额"].sum().idxmax()
    return df1

def product_sale(df: DataFrame) -> str:
    df1 = df.groupby("产品")["金额"].sum().idxmax()
    return df1

def total_income(df: DataFrame) -> int:
    df1 = df["金额"].sum()
    return df1

def check(df: DataFrame) -> Series:
    df1 = df.isnull().sum()

    return df1

df2 = area_sale(df)
print("销售金额最高的地区:\n" + str(df2))
df3 = product_sale(df)
print("销售金额最高的产品:\n" + str(df3))
df4 = total_income(df)
print("总收入:\n" + str(df4))
df5 = check(df)
print("具体缺失情况\n" + str(df5))