#项目
a = [{"work_id": "001","work_name": "读文档","status": "已完成"},{"work_id": "002","work_name": "跟练","status": "已完成"},{"work_id": "003","work_name": "写项目","status": "进行中"}]
print("1.创建任务")
print("2.查看任务")
print("3.修改状态")
print("4.按状态过滤")
print("5.再次打印菜单")

access = True
while access:
    request = input("请选择你需要的业务:")

    if int(request) == 1:
        work_id = input("请输入创建的任务id:")
        work_name = input("请输入任务的名字:")
        work_status = input("请输入当前的任务状态:")
        a.append({"work_id": work_id,"work_name": work_name,"status": work_status})
        continue
    if int(request) == 2:
        mark = input("请输入需要查看的任务id")
        for i in range(len(a)):
            if mark == a[i]['work_id']:
                print(a[i])
                break
        else:       
            print(a)
                    
    if int(request) == 3:
        mark = input("请输入需要修改状态的任务id")
        for i in range(len(a)):
            if mark == a[i]['work_id']:
                new_status = input("请输入修改后的任务状态")
                a[i]['status'] = new_status
                break
        else:
            print("未找到对应的id,请重新输入")
            
    if int(request) == 4:
        finish = []
        for i in range(len(a)):
            if a[i]['status'] == "已完成":
                finish.append(a[i])
        print("已完成的任务对象有:" + str(finish))
        continue
    if int(request) == 5:
        print("1.创建任务")
        print("2.查看任务")
        print("3.修改状态")
        print("4.按状态过滤")
        print("5.再次打印菜单")
    if int(request) == 6:
        access = False
    if int(request) not in range(1,7):
        print("请输入1-5的数字")