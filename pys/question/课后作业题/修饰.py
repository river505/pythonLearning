class BookSell:
    static_var = 100

    def sell(self, name, author, version, price):
        print("%s的销售价格为%d" % (name, int(price)))

    # 请在下面填入函数修饰符将printStatic()方法声明为静态方法
    ########## Begin ##########
    @staticmethod
    ########## End ##########
    def printStatic():
        print(BookSell.static_var)

    # 请在下面填入函数修饰符将printVersion(cls)方法声明为类方法
    ########## Begin ##########
    @classmethod
    ########## End ##########
    def printVersion(cls):
        print(cls)




