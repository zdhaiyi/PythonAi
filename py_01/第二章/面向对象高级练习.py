"""
某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还功能。系统中有两种类型的会员：
普通会员和VIP会员，他们的借书权限不同。你需要使用面向对象编程的思想，设计并实现这个图书管理系统。
核心功能：
    1.会员登录：会员通过卡号和密码登录系统
    2.借书：会员可以借阅库存中有余量的图书
    3.还书：会员可以归还借阅的图书
    4.查看我的借阅：展示当前会员已经借阅的图书列表
    5.退出系统
借阅规则：
    1.普通会员最多可以借3本
    2.VIP会员最多可以借6+VIP等级本（VIP等级，默认为1）
注意：
    1.登录成功（卡号和密码均正确）后，才可以访问该系统
    2.图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书
"""
# 书籍类
from abc import ABC,abstractmethod
import json
class Book:
    def __init__(self, book_id,title, author, total_num):
        self.book_id = book_id          # 书籍编号
        self.title = title              # 书籍标题
        self.author = author            # 作者
        self.total_num = total_num      # 总数量
        self.__available_num = total_num  # 可用数量

    #借书方法
    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        else:
            return False

    #还书方法
    def return_book(self):
        self.__available_num += 1

    #获取可借数量
    def get_available_num(self):
        return self.__available_num


# 会员类
class Member:
    def __init__(self, member_id, name, password):
        self.member_id = member_id      # 会员编号
        self.name = name                # 姓名
        self.__password = password        # 密码
        self.__member_books = []        # 会员借阅的图书列表

    #会员借阅方法
    def borrow_book(self, book:Book):
       #先判断会员是否以达到最大借阅数量
        if len(self.__member_books) < self.max_member_boorrow_num():
            if book.borrow_book():
                self.__member_books.append(book)
                return True
            else:
                print("借阅失败,已达最大借阅数量")
                return False
        else:
            return False

    #会员归还图书方法
    def return_book(self, book:Book):
        if book in self.__member_books:
            self.__member_books.remove(book)
            book.return_book()
            return True
        else:
            print("还书失败,您没有借阅此书")
            return False

    #获取密码
    def get_password(self):
        return self.__password
    #获取会员图书列表
    def get_member_books(self):
        return self.__member_books

    #会员最多可借阅数量
    @abstractmethod
    def max_member_boorrow_num(self) -> int:
        pass

#普通会员
class NormalMember(Member):
    def max_member_boorrow_num(self) -> int:
        return 3

# VIP会员
class VIPMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level

    def max_member_boorrow_num(self) -> int:
        return 6 + self.vip_level

#图书管理系统
class LibrarySystem:
    def __init__(self):
        self.dictionary_books = {}     # 书籍列表
        self.dictionary_members = {}     # 会员列表
        self.current_member:Member | None = None
        self.load_books()
        self.load_members()

    #加载书籍数据
    def load_books(self):
        with open("data/books.json", "r", encoding="utf-8") as f:
            books = json.load(f)
        for book in books:
            self.dictionary_books[book["编号"]] = Book(book["编号"], book["标题"], book["作者"], book["数量"])
        print("已加载书籍数据")

    #加载会员数据
    def load_members(self):
        with open("data/members.json", "r", encoding="utf-8") as f:
            members = json.load(f)
            for member in members:
                if member["卡号"].startswith("N"):
                    self.dictionary_members[member["卡号"]] = NormalMember(member["卡号"], member["姓名"], member["密码"])
                elif member["卡号"].startswith("V"):
                    self.dictionary_members[member["卡号"]] = VIPMember(member["卡号"], member["姓名"], member["密码"], member["会员等级"])
            print("已加载会员数据")

    #登录系统
    def login(self):
        while True:
            print("【登录】")
            member_id = input("请输入会员卡号：")
            password = input("请输入密码：")
            if member_id not in self.dictionary_members:
                print("会员不存在,请重新输入")
                continue
            # 判断密码
            current_user = self.dictionary_members[member_id]
            if current_user.get_password() == password:
                print(f"登录成功,欢迎您{current_user.name}")
                self.current_member = current_user
                return True
            else:
                print("密码错误,请重新输入")

    #借阅图书
    def borrow_book(self):
        #1.展示图书数据
        print("【可借阅图书列表：】")
        for book in self.dictionary_books.values():
            print(f"编号：{book.book_id}, 标题：{book.title}, 作者：{book.author}, 可用数量：{book.get_available_num()}")
        # 2.输入图书编号
        book_id = input("请输入要借阅的图书编号：")
        if book_id in self.dictionary_books:
            book = self.dictionary_books[book_id]
            print(f"{self.current_member.name}已成功借阅图书：{book.title}")
            self.current_member.borrow_book(book)
        print("借阅失败,找不到该图书")

    #归还图书
    def return_book(self):
        print("【已借阅图书列表】")
        for book in self.current_member.get_member_books():
            print(f"编号：{book.book_id}, 标题：{book.title}, 作者：{book.author}")
        # 输入图书编号
        book_id = input("请输入要归还的图书编号：")
        if book_id in self.dictionary_books:
            book = self.dictionary_books[book_id]
            if self.current_member.return_book(book):
                print(f"{self.current_member.name}已成功归还图书：{book.title}")
            else:
                print("归还失败,请检查您是否已借阅此图书")
        else:
            print("归还失败,找不到该图书")

    #查看已借阅的图书
    def show_borrowed_books(self):
        print("【已借阅图书列表】")
        for book in self.current_member.get_member_books():
            print(f"编号：{book.book_id}, 标题：{book.title}, 作者：{book.author}")

    #图书管理菜单
    def book_management_menu(self):
        if self.login():
            while True:
                print("【图书管理】")
                print("1. 借阅图书")
                print("2. 归还书籍")
                print("3. 查看当前会员已借阅的图书")
                print("4. 退出系统")
                choice = input("请输入你的选择：")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统!")
                        break
                    case _:
                        print("无效的选择,请重新输入")


ls = LibrarySystem()
ls.book_management_menu()