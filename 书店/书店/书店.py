
def books_browse():#图书浏览
    print("********************************************")
    print("*      书名    *   作者  * 单价 * 数量*")
    with open('books.txt','r+',encoding='utf-8') as f:
        print("********************************************")
        for line in f.readlines():
            print(line[:-1].split(':'))
            s = [i[:-1].split(':') for i in f.readlines()]
        print("********************************************")
    f.close()
    pass

def books_select_name():#图书查询
    s = input("请输入要找的书籍：")
    a = False
    with open('books.txt','r+',encoding='utf-8') as f:
        for line in f.readlines():
            if line.find(s)!=-1:
                a = True
                print("*  书名  *  作者 *单价 *数量*")
                print('*'+line+'*')               
    if a == False:
        print("对不起，没有你想查询的书籍")
    f.close()
    pass

def books_select_author():
    s = input("请输入要找的作者：")
    a = False
    with open('books.txt','r+',encoding='utf-8') as f:
        for line in f.readlines():
            if line.find(s)!=-1:
                a = True
                print("   书名    作者  单价 数量")
                print(line)
    if a == False:
        print("对不起，没有你想查询的作者")
    f.close()
    pass

def books_select():
    while 1:
        print("********************************************")
        print("*  大  *        1.书名查询                 *")
        print("*      *        2.作者查询                 *")
        print("*  华  *        3.返回上一级               *")
        print("********************************************")
        ss = input("尊敬的用户，请选择你的操作:")
        if int(ss) == 1:
            books_select_name()
        elif int(ss) == 2:
            books_select_author()
        elif int(ss) == 3:
            user()
            break
        else:
            print("输入错误！！！请重新输入")

def user_login():#用户登录
    name_list = open('user_pass.txt','r+',encoding='utf-8')
    name_text = dict(line.strip().split(":") for line in name_list if line)
    #验证三次登陆
    number = 3
    for i in range(3):
        username = input("请输入姓名:")
        password = input("请输入密码:")
        lock_name = open('locked.txt', 'r+',encoding='utf-8')
    # 检测用户是否被锁定
        for j in lock_name.readlines():
            if username == j.strip():
                print("因尝试过多导致{}用户锁定".format(username))
                exit(1)
   # 验证用户名密码是否正确
        if password == name_text.get(username):
           print("欢迎用户 {name} 登陆...".format(name=username))
           user()
           break
   # 输入两次后用户被锁定，将锁定用户写入locked文件中
        elif i == 2:
            lock_name = open('locked.txt','a+',encoding='utf-8')
            lock_name.write(username+'\n')
            lock_name.close()
            print("因尝试过多导致{}用户锁定".format(username))
            exit(2)
        else:
            print('''无效的用户名或密码！！！\n
            ---------剩余尝试次数:{}---------'''.format(2-i))
            number -= 1
            if number == 0:
                begin()
    pass
     
def user_update_password():#修改密码
    username = input("请输入您的姓名:")
    password = input("请输入你的原密码:")
    a = False   
    fp = open('user_pass.txt', 'r', encoding='utf-8')
    lines = []
    for line in fp.readlines():
        if line != '\n':
            lines.append(line)
    fp.close()
    _password = input("请输入你的新密码:")
    fp = open('user_pass.txt', 'w', encoding='utf-8')
    for line in lines:
        if username in line:
            line = username+":"+_password
            fp.write('%s\n' % line)
            print("修改成功")
            a = True
        else:
            fp.write('%s' % line)
    if a == False:
        print("修改密码失败，用户名或者密码输入有误，请重新输入")
        user_update_password()
    fp.close()
    pass

def user():
    while 1:
        print("******************************************")
        print("* 大  *         1.图书浏览               *")
        print("* 华  *         2.图书查询               *")
        print("* 书  *         3.修改密码               *")
        print("* 店  *         0.返回主页面             *")
        print("******************************************")
        ss = input("尊敬的用户，请选择你的操作:")
        if int(ss) == 1:
            books_browse()
        elif int(ss) == 2:
            books_select()
        elif int(ss) == 3:
            user_update_password()
        else:
            begin()
    pass

def admin():  # 管理员使用界面
    a = 1
    while a == 1:
        print("*******************************************")
        print("*  大  *          欢迎光临大华书店        *")
        print("*      ************************************")
        print("*  华  *            1.库存管理            *")
        print("*      *            2.更新图书            *")
        print("*  书  *            3.用户管理            *")
        print("*      *            4.支付管理            *")
        print("*  店  *            5.退    出            *")
        print("*******************************************")
        s = input("请选择您的操作:")

        if int(s) == 1:
            print("0.浏览库存")
            print("1.入库")
            print("2.出库")
            t = input("请输入您的选择：")
            if int(t) == 0:
                books_browse()
            elif int(t) == 1:
                put()
            elif int(t) == 2:
                book = input("请输入要出库的书：")
                num = int(input("请输入出库的数量："))
                out(book, num)
        elif int(s) == 2:
            update_book()
        elif int(s) == 3:
            user_control()
        elif int(s) == 4:
            print("管理员询问客户要购买书和数量，并查看数量是否足够！")
            books_select_name()
            print("请管理员自行判断是否支付成功！")
            print("1.成功")
            print("2.失败")
            t = input("请输入您的判断：")
            if int(t) == 1:
                book = input("请输入要购买的书：")
                num = int(input("请输入购买的数量："))
                out(book, num)
                print("支付成功，已出库")
            else:
                print("支付失败，请重新选择")
        elif int(s) == 5:
            print("成功退出图书管理信息系统！")
            exit()
        else:
            print("输入错误,请重新输入！")

def user_control():  # 用户管理
    while 1:
        print("*************************************")
        print("*  大  *        1.添加用户          *")
        print("*      *        2.删除用户          *")
        print("*  华  *        3.返回上一级        *")
        print("*************************************")
        ss = input("尊敬的用户，请选择你的操作:")
        if int(ss) == 1:
            name = input("请输入要添加的用户名：")
            password = input("请输入要添加的用户密码：")
            fp = open('user_pass.txt', 'r+', encoding='utf-8')
            x = 1
            lines = []
            for line in fp.readlines():
                if line != '\n':
                    lines.append(line)
            fp.close()
            for line in lines:
                if name in line:
                    x = 0
            if x == 1:
                fp = open('user_pass.txt', 'a', encoding='utf-8')
                print(name + ":" + password, file=fp)
                print("添加完成")
                fp.close()
            else:
                print("用户名重复，添加失败！")
        elif int(ss) == 2:
            user_name = input("请输入要删除的用户名：")
            fp = open('user_pass.txt', 'r', encoding='utf-8')
            lines = fp.readlines()
            fp.close()
            fp = open('user_pass.txt', 'w', encoding='utf-8')
            for line in lines:
                if user_name not in line:
                    fp.write(line)
            fp.close()
            print("删除成功！")
        elif int(ss) == 3:
            break
        else:
            print("输入错误！！！请重新输入")

def put():  # 书籍入库操作
    fp = open('books.txt', 'a', encoding='utf-8')
    book_name = input("请输入要入库的书名：")
    book_author = input("请输入书的作者：")
    book_price = input("请输入书的价格：")
    book_amount = input("请输入书的数量：")
    print(book_name + ":" + book_author + ":" + book_price + ":" + book_amount, file=fp)
    fp.close()

def out(book, num):  # 书籍出库操作
    fp = open('books.txt', 'r', encoding='utf-8')
    lines = []
    for line in fp.readlines():
        if line != '\n':
            lines.append(line)
    fp.close()
    fp = open('books.txt', 'w', encoding='utf-8')
    x = 0
    for line in lines:
        if book in line:
            x = 1
            line1 = line[0:len(line) - 3]
            line2 = line[len(line) - 3:len(line)]
            line3 = ''
            line4 = ''
            for i in line2:
                if i.isnumeric():
                    line3 = line3 + i
                elif i == ":":
                    line4 = ":"
            line2 = int(line3)
            if line2 >= num:
                line2 = line2 - num
            else:
                print("出库失败，库存不足!")
            line = line1 + line4 + str(line2)
            fp.write('%s\n' % line)
        else:
            fp.write('%s' % line)
    fp.close()
    if x == 0:
        print("出库失败，该书籍不存在!")
    pass

def update_book():  # 更新图书信息
    book_name = input("请输入要更新的书名：")
    book_author = input("请输入书的作者：")
    book_price = input("请输入书的价格：")
    book_amount = input("请输入书的数量：")
    a = False
    fp = open('books.txt', 'r', encoding='utf-8')
    lines = []
    for line in fp.readlines():
        if line != '\n':
            lines.append(line)
    fp.close()
    fp = open('books.txt', 'w', encoding='utf-8')
    for line in lines:
        if book_name in line:
            line = book_name + ":" + book_author + ":" + book_price + ":" + book_amount
            fp.write('%s\n' % line)
            a = True
            print("更新成功")
        else:
            fp.write('%s' % line)
    if a == False:
        print("更新有误,请重新选择")
        admin()
    fp.close()

def admin_login():
    a = 1
    while a == 1:
        d1 = input("请输入用户名:")
        d2 = input("请输入密码:")
        if d1 == "admin" and d2 == '123456':
            admin()
            a = 0
        else:
            print("输入错误！")
            print("*************************************")
            print("* 大 *           1.重新输入          *")
            print("* 华 *           2.退回上一层        *")
            print("*************************************")
            ss = input("请选择您的操作:")
            if int(ss) != 1:
                a = 0
    pass


def begin():  # 最先开始的函数
    while 1:
        print("*******************************************")
        print("*  大 *         欢迎光临大华书店          *")
        print("*  华 *************************************")
        print("*     *           1.用户入口              *")
        print("*  书 *           2.管理员入口            *")
        print("*  店 *           3.退出                  *")
        print("*******************************************")
        ss = input("请选择您的操作:")
        if int(ss) == 1:
            user_login()
        elif int(ss) == 2:
            admin_login()
        else:
            exit()


begin()