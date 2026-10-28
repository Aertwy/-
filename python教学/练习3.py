info=[]

#添加学员信息
def in_put():
    a_id = input("请输入学员学号")
    a_name = input("请输入学员姓名")
    a_tel = input("输入学员的手机号码")
    for student_dict in info:
        if a_name == student_dict["name"] :
            print(f"错误{a_name}重复,无法添加")
            return
    student_dict = {
            "id": a_id,
            "name": a_name,
            "tel": a_tel
        }

    info.append(student_dict)
    print("保存成功:"f"{student_dict}")
    input("按任意键继续：")
    infor()

#删除学员信息
def in_del():
    del_name = input("输入要删除的学员姓名：")
    for A1 in info:
        if del_name == A1["name"]:
            info.remove(A1)
            print(f"已删除{del_name}")
            input("删除完毕，按任意键继续：")
            infor()
            return                     # 找到就删，删完立刻结束
    print(f"错误：{del_name}不在该学员管理系统内")   # 循环完没找到才提示
    input("按任意键退出")

#修改学员信息
def in_change():
    in_name = input("输入学员姓名")
    for A1 in info:
        if in_name == A1["name"]:
            A1["id"]= input("请输入新的学号:")
            A1["tel"]= input("请输入新的电话号码:")
            print(f"修改完成，修改学生{A1["name"]}\n学号:{A1["id"]}\n电话号码:{A1["tel"]}")
            input("修改显示完毕，按任意键继续：")
            infor()
        else:
            print(f"错误学生{A1["name"]}不在学员信息系统内")
            input("按任意键退出")
            return

#查询学员信息
def in_query():
    in_name =input("输入学员姓名查询：")
    for A1 in info:
        if in_name == A1["name"]:
            print(f"学生姓名:{A1["name"]}\n学号:{A1["id"]}\n电话号码:{A1["tel"]}")
            input("查询显示完毕，按任意键继续：")
            infor()
        else:
            print(f"错误：{A1["name"]}不在学员查询系统中")
            input("按任意键退出")
            return

#显示所有学员信息
def in_all():
    if not info:
        print("错误；没有学员信息")
        input("所有学员显示完毕，按任意键退出：")
        return
    for A1 in info:
        print("---"*10)
        print(f"姓名{A1["name"]}\n学号:{A1["id"]}\n电话号码:{A1["tel"]}")
        print("---" * 10)
    input("所有学员显示完毕，按任意键继续：")
    infor()


#信息功能
def infor():
    print("="*30)
    print("\t\t学员管理系统V1.0")
    print("1.添加学员\n2.删除学员\n3.修改学员\n4.查询学员\n5.显示所有学员\n6.退出系统")
    print("=" * 30)

#接受用户输入功能序号
def info_put():
    while True:
        acc_output = int(input("输入功能序号1-6:"))
        if acc_output == 1:
            print("您选择了【添加学员】")
            in_put()
        elif acc_output == 2:
            print("您选择了【删除学员】")
            in_del()
        elif acc_output == 3:
            print("您选择了【修改学员】")
            in_change()
        elif acc_output == 4:
            print("您选择了【查询学员】")
            in_query()
        elif acc_output == 5:
            print("您选择了【显示所有学员】")
            in_all()
        elif acc_output == 6:
            print("您选择了【退出系统】")
            esc = input("确认退出请输入Yes 或 No:")
            if esc.lower() == "yes":
                print("退出成功")
                break
            elif esc == "no":
                info_put()
            else:
                print("退出成功")
                break
        else:
            print("选择错误，请重新选择")
            infor()


infor()
info_put()
















