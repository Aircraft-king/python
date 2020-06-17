# coding=utf-8
import pickle  # Python的标准模块，可以将纯Python对象存储在文件
from os import remove

user_dict = {}  # 存储信息字典，信息用字典存，再用列表存储字典
queue_num = 0  # 排队序号

# 选择序号的获得
def get_choice():
    selected_key = input("请输入选择的序号：")
    return selected_key

# 检查性别是否合法
def check_sex(new_sex):
    flag = True
    while flag:
        if new_sex == '男' or new_sex == '女':
            flag = False
        else:
            new_sex = input("输入性别有误，请重新输入(男/女)：")
    return new_sex

# 检查电话号码是否合法
def check_phone(new_phone):
    flag = True
    while flag:
        if new_phone.isdigit():
            if len(new_phone) != 11:
                new_phone = input("您输入的电话号码有误，请重新输入：")
            else:
                flag = False
        else:
            new_phone = input("您输入的电话号码有误，请重新输入：")
    return new_phone

# 检查身份证号码是否合法
def check_id(new_id):
    flag = True
    while flag:  # 先检查是不是纯数字再去考虑是否重复的事情，如果不是纯数字直接pass
        if new_id.isdigit():
            if len(new_id) != 18:
                new_id = input("您输入的身份证号有误，请重新输入：")
            else:
                if new_id in user_dict:
                    input("您已注册过，请直接预约：")
                flag = False
        else:
            new_id = input("您输入的身份证号有误，请重新输入：")
    return new_id

# 注册个人信息
def add_user():
    """注册信息，以身份证号作为字典的键，姓名、性别、电话、年龄作为值"""
    id = check_id(input("请输入18位的身份证号："))  # input函数可以接受一个字符串作为参数，等待用户输入后将返回用户输入的文本

    if id in user_dict:  # 运算符in来检查某一键值对是否存在于字典中
        print("用户已经存在")
    else:
        new_name = input("请输入姓名：")
        new_sex = check_sex(input("请输入性别(男/女)："))
        new_phone = check_phone(input("请输入11位电话号码："))
        new_age = input("请输入年龄：")

        label = {"name": new_name, "sex": new_sex, "phone": new_phone, "age": new_age,
                 "reservation_num": None, "doctor_num": None, "queue_num": None, "flag": False}
        user_dict[id] = label
        print("添加成功")
        print("用户姓名：", user_dict[id]["name"])
        print("用户性别：", user_dict[id]["sex"])
        print("用户电话：", user_dict[id]["phone"])
        print("用户年龄：", user_dict[id]["age"])

# 查询个人信息
def find_user():
    """根据身份证号查询用户"""
    id = input("请输入要查询的用户身份证号：")
    if id in user_dict:
        print("您查询的信息如下：")
        print("姓名：", user_dict[id]["name"])
        print("性别：", user_dict[id]["sex"])
        print("电话：", user_dict[id]["phone"])
        print("年龄：", user_dict[id]["age"])
    else:
        print("身份证为：{} 的用户不存在".format(id))

# 修改个人信息
def modify_user():
    """修改用户信息，注意，由于id是字典的键，所以id的值不可以修改"""
    id = input("请输入要修改的用户的身份证号：")
    if id in user_dict:
        modify_name = input("请输入修改后的姓名: ")
        modify_sex = input("请输入修改后的性别: ")
        modify_phone = input("请输入修改后的电话: ")
        modify_age = input("请输入修改后的年龄: ")
        modify_label = {"name": modify_name, "sex": modify_sex, "phone": modify_phone, "age": modify_age}
        user_dict[id] = modify_label
        print("修改后姓名：", user_dict[id]["name"])
        print("修改后性别：", user_dict[id]["sex"])
        print("修改后电话：", user_dict[id]["phone"])
        print("修改后年龄：", user_dict[id]["age"])
    else:
        print("身份证为：{} 的用户不存在".format(id))

# 删除个人信息
def delete_user():
    """根据身份证号删除用户"""
    id = input("请输入要删除的用户的身份证号：")
    if id in user_dict:
        del user_dict[id]  # del语句用来删除某一键值对
        print("删除成功")
    else:
        print("身份证为：{} 的用户不存在".format(id))

# 挂号预约
def registered_appointment():
    id = input("请输入用户的身份证号: ")
    if id in user_dict:
        print("登录成功！")
        if user_dict[id]["flag"] == True:
            print("您已有预约")
        else:
            print("请选择要预约的科室：")
            reservation_num = input("1.外科 2.内科 3.五官科 4.急诊科 5.其他科室 6.健康体检\n 请选择要预约的科室的序号：")
            doctor_num = input("1.专家号 2.普通号\n 请选择要挂会诊号的序号： ")
            global queue_num
            queue_num += 1
            user_dict[id]["reservation_num"] = reservation_num
            user_dict[id]["doctor_num"] = doctor_num
            user_dict[id]["queue_num"] = queue_num
            user_dict[id]["flag"] = True
            print("挂号预约成功")
    else:
        print("身份证为：{} 的用户不存在, 请先注册 ".format(id))

# 取消挂号
def cancel_registration():
    id = input("请输入要取消用户的身份证号: ")
    if id in user_dict:
        if user_dict[id]["flag"] == False:
            print("您未有预约，无需取消   ")
        else:
            user_dict[id]["reservation_num"] = None
            user_dict[id]["doctor_num"] = None
            user_dict[id]["queue_num"] = None
            user_dict[id]["flag"] = False

            print("挂号取消成功   ")
    else:
        print("身份证为：{} 的用户不存在".format(id))

# 查看预约
def view_registration():
    id = input("请输入要查看用户的身份证号: ")
    if id in user_dict:
        if user_dict[id]["flag"] == False:
            print("您还未有预约")
        else:
            print("姓名：", user_dict[id]["name"])
            print("性别：", user_dict[id]["sex"])
            print("电话：", user_dict[id]["phone"])
            print("年龄：", user_dict[id]["age"])
            if user_dict[id]["reservation_num"] == '1':
                print("您预约科室为外科")
            elif user_dict[id]["reservation_num"] == '2':
                print("您预约科室为内科")
            elif user_dict[id]["reservation_num"] == '3':
                print("您预约科室为五官科")
            elif user_dict[id]["reservation_num"] == '4':
                print("您预约科室为急诊科")
            elif user_dict[id]["reservation_num"] == '5':
                print("您预约科室为其他科室")
            else:
                print("您的预约为健康体检")
            if user_dict[id]["doctor_num"] == '1':
                print("您的预约为专家号")
            else:
                print("您的预约为普通号")
            print("排队号：", user_dict[id]["queue_num"])
    else:
        print("身份证为：{} 的用户不存在".format(id))

def write():
    """将用户写入文件"""
    # 写入的方式打开文件
    # f = open(r'C:\Users\asus\Desktop\text.txt', 'wb')
    try:
        f = open("text.txt", "w")
    except Exception as e:
        f = open("text.txt", "x")
    for info in user_dict:
        strInfo =info+','+user_dict[info]['name']+','+user_dict[info]['sex']+','+\
            user_dict[info]['phone']+','+user_dict[info]['age']+','+str(user_dict[info]['reservation_num'])\
            +','+str(user_dict[info]['doctor_num'])+','+str(user_dict[info]['queue_num'])+','+str(user_dict[info]['flag'])
        f.write(str(strInfo)+'\n')
    f.close()
    pass



def menu():
    print("-" * 50)
    print("       **********   医院挂号系统   **********")
    print("       **********  1.注册个人信息  **********")
    print("       **********  2.个人信息查询  **********")
    print("       **********  3.个人信息修改  **********")
    print("       **********  4.个人信息删除  **********")
    print("       **********  5.  挂号预约   **********")
    print("       **********  6.  取消预约   **********")
    print("       **********  7.  查看预约   **********")
    print("       **********  8.  退出系统   **********")
    print("-" * 50)

def main():
    flag = 1
    while flag:
        try:
            menu()
            choice = int(input("请选择功能：输入对应的数字： "))
            if choice == 1:  # 注册个人信息
                add_user()
            elif choice == 2:  # 个人信息查询
                find_user()
            elif choice == 3:  # 个人信息修改
                modify_user()
            elif choice == 4:  # 个人信息删除
                delete_user()
            elif choice == 5:  # 挂号预约
                registered_appointment()
            elif choice == 6:  # 取消预约
                cancel_registration()
            elif choice == 7:  # 查看预约
                view_registration()
            elif choice == 8:  # 退出
                write()  # 字典中数据重写写到文件中
                flag = 0
            else:
                print("输入不合法，请重新输入")
        except ValueError:
            print("请输入相应的数字")

main()