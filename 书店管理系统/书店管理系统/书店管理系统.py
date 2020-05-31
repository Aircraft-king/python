# 书的属性：书名，作者，状态，位置
# 管理系统：
class Book(object): #定义一个书类
  
     def __init__(self, name, author, status, bookindex):
         self.name = name
         self.author = author
         self.status = status
         self.bookindex = bookindex
  
def __str__(self):
    if self.status == 1:
        stats = '未借出'
    elif self.status == 0:
        stats = '已借出'
    else:
        stats = '状态异常'
        return '书名: 《%s》 作者: %s 状态: <%s> 位置: %s' % (self.name, self.author, stats, self.bookindex)
  
  
class BookManage(object):
    books = []
  
    def start(self):
 #添加图书
        self.books.append(Book('python', 'guido', 1, 'ISO9001'))
        self.books.append(Book('c', '谭浩强', 1, 'NFS8102'))
        self.books.append(Book('java', 'westos', 1, 'PKA7844'))
 
    def Menu(self):
        self.start()
        while True:
            print("""
        图书管理系统
        1.查询图书
        2.增加图书
        3.借阅图书
        4.归还图书
        5.退出系统
            """)
  
            choice = input('请选择：')
  
        if choice == '1':
            self.showAllBook() #调用显示所有书籍的函数
        elif choice == '2':
            self.addBook() #调用添加书籍的函数
        elif choice == '3':
            self.borrowBook() #调用借书的函数
        elif choice == '4':
            self.returnBook() #调用还书的函数
        elif choice == '5':
            print('欢迎下次使用...')
            exit()
        else:
            print('请输入正确选择')
            
    def showAllBook(self):
        for book in self.books:
            print(book)
  
    def addBook(self):
        name = input('图书名称:')
        self.books.append(Book(name, input('作者:'), 1, input('存储位置:')))
        print('图书《%s》增加成功' % name)
  
    def checkBook(self, name):
        for book in self.books:
            if book.name == name:
                return book
            else:
                return None
  
    def borrowBook(self):
        name = input('借阅图书名称: ')
        ret = self.checkBook(name)
        print(ret)
     #判断书是否存在，如果存在，判断书是否已借出，如果没有借出，借阅并将其状态改为0
        if ret != None:
            if ret.status == 0: 
                print('书籍《%s》已经借出' % name)
            else:
                ret.status = 0
                print('书籍《%s》借阅成功' % name)
        else:
            print('书籍《%s》不存在' % name)
  
    def returnBook(self):
        name = input('归还图书名称:')
        ret = self.checkBook(name)
  
        if ret != None:
            if ret.status == 0:
                ret.status = 1
                print('书籍《%s》归还成功' % name)
                print(ret)
            else:
                print('书籍《%s》未借出' % name)
        else:
            print('书籍《%s》不存在' % name)
  
  
manager = BookManage() #类的实例化
manager.Menu()
