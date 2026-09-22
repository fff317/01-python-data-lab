print("Hello world")
print("我正在学习python")

name = "小明"
age = 18
print("我的名字是"+name)
print("我的年龄是"+str(age))

if age >= 18:
    print("已经成年")
else:
    print("还未成年")

#项目
print("请回答以下问题")
question1 = input("你的姓名是:")
question2 = input("你的职业是:")
question3 = input("你的学习目标是:")

if not question1 or not question3 :
    print("不能为空")
else:
    print("完整资料:")
    print(question1)
    print(question2)
    print(question3)
    print("学习目标共" + str(len(question3)) + "个字")