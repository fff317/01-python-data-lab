def load_task(filename: str) -> list:
    try:
       with open(filename,"r",encoding = "utf-8") as f:
           task = json.load(f)
           return task
    except FileNotFoundError:
        print("未找到对应的文件路径")
        with open("task.json","w",encoding = "utf-8") as f:
           json.dump([],f)
        return []


def save_file(a: list,filename: str) -> None:
    try:
       with open(filename,"w",encoding = "utf-8") as f:
           json.dump(a,f,ensure_ascii = False)
    except Exception:
        print("写入文件失败,请重新写入")

def create_task(work_id: str,work_name: str,work_status: str,a: list) -> list:
    a.append({"work_id": work_id,"work_name": work_name,"status": work_status})
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
            return a[i]
    else:
        print("未找到对应id,请重新输入")
    print(a)

def filter_task(a: list) -> list:
    new_a = []
    try:
       for i in range(len(a)):
           if a[i]['status'] == "已完成":
               new_a.append(a[i])
       return new_a
    except Exception as e:
        print("产生错误,请重试"+str(e))

print("1.创建新任务")
print("2.查看任务")
print("3.修改任务状态")
print("4.按状态过滤列表")
print("5.再次打印菜单")
print("6.退出")

access = True
while access:
    load_task("task.json")
    request = input("请输入你需要的业务:")
    if int(request) == 1:
        work_id = input("请输入你需要的创建的id")
        work_name = input("请输入你需要创建的任务名称")
        work_status = input("请输入你需要创建的任务状态")
        tasks = load_task("task.json")
        b = create_task(work_id,work_name,work_status,tasks)
        save_file(b,"task.json")
        print(b)
        continue
    if int(request) == 2:
        work_id = input("请输入需要查看的任务id")
        tasks = load_task("task.json")
        check_task(work_id,tasks)
        continue
    if int(request) == 3:
        work_id = input("请输入要修改状态的任务id")
        work_status = input("请输入要修改的状态")
        tasks = load_task("task.json")
        c = edit_task(work_id,work_status,tasks)
        save_file(c,"task.json")
        print(c)
        continue
    if int(request) == 4:
        tasks = load_task("task.json")
        d = filter_task(tasks)
        print(d)
        continue
    if int(request) == 5:
        print("1.创建新任务")
        print("2.查看任务")
        print("3.修改任务状态")
        print("4.按状态过滤列表")
        print("5.再次打印菜单")
        print("6.退出")
        continue
    if int(request) == 6:
        access = False
    if int(request) not in range(1,7):
        print("请输入1-6的数字")

def create_task(work_id: str,work_name: str,work_status: str,filename: str) -> list:
    try:
       with open(filename,"r",encoding = "utf-8"):
           tasks = f.load()
       tasks.append({"work_id": work_id,"work_name": work_name,"status": work_status})
    except FileNotFoundError:
        print("找不到文件路径")
    try:
       with open(filename,"w",encoding = "utf-8"):
           json.dump(tasks,f,ensure_ascii = False)
       return tasks
    except Exception as e:
        print("写入文件失败,请重试")