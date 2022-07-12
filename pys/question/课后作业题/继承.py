import animalstest
# 请在下面填入定义fish类的代码，fish类继承自animals类
########## Begin ##########
class fish(animalstest.animals):
########## End ##########
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("%s会游泳" %self.name)

# 请在下面填入定义leopard类的代码，leopard类继承自animals类
########## Begin ##########
class leopard(animalstest.animals):
########## End ##########
    def __init__(self,name):
        self.name = name
    def climb(self):
        print("%s会爬树" %self.name)

fName = input()
lName = input()
f = fish(fName)
f.breath()
f.swim()
f.foraging()
l = leopard(lName)
l.breath()
l.run()
l.foraging()


