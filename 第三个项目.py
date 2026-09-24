#项目
def create_task(work_id: str,work_name: str,work_status: str,a: list) -> list:
    a.append([{"work_id": work_id,"work_name": work_name,"status": work_status}])
    print(a)
    return a

def check_task(work_id: str,a: list):
    for i in range(len(a)):
        if work_id == a[i]['work_id']:
            print(a[i])
            break
    else:
        print("未找到对应的id,请重新输入")

def edit_task(work_id: str,work_status: str,a: list) -> dict:
    for i in range(len(a)):
        if work_id == a[i]['work_id']:
            a[i]['status'] = work_status
            print(a[i])
            break
    else:
        print("未找到对应id,请重新输入")
    print(a)

def filter_task(a: list) -> list:
    new_a = []
    for i in range(len(a)):
        if a[i]['status'] == "已完成":
            new_a.append(a[i])
            print(new_a)
    return new_a

print("1.创建新任务")
print("2.查看任务")
print("3.修改任务状态")
print("4.按状态过滤列表")
print("5.再次打印菜单")
print("6.退出")

access = True
a = [{"work_id": "001","work_name": "读文档","status": "已完成"},{"work_id": "002","work_name": "写项目","status": "进行中"},{"work_id": "003","work_name": "错题本","status": "待开始"}]

while access:
    request = input("请输入你需要的业务:")
    if int(request) == 1:
        work_id = input("请输入你需要的创建的id")
        work_name = input("请输入你需要创建的任务名称")
        work_status = input("请输入你需要创建的任务状态")
        create_task(work_id,work_name,work_status,a)
        continue
    if int(request) == 2:
        work_id = input("请输入需要查看的任务id")
        check_task(work_id,a)
        continue
    if int(request) == 3:
        work_id = input("请输入要修改状态的任务id")
        work_status = input("请输入要修改的状态")
        edit_task(work_id,work_status,a)
        continue
    if int(request) == 4:
        filter_task(a)
    if int(request) == 5:
        print("1.创建新任务")
        print("2.查看任务")
        print("3.修改任务状态")
        print("4.按状态过滤列表")
        print("5.再次打印菜单")
        print("6.退出")
    if int(request) == 6:
        access = False
    if int(request) not in range(1,7):
        print("请输入1-6的数字")