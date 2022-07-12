class A(object):
    def test(self):
        print("this is A.test()")
class B(object):
    def test(self):
        print("this is B.test()")
    def check(self):
        print("this is B.check()")
# 请在下面填入定义类C的代码
########## Begin ##########
class C(A,B):
########## End ##########
    pass
# 请在下面填入定义类D的代码
########## Begin ##########
class D(A,B):
########## End ##########
    def check(self):
        print("this is D.check()")
class E(C,D):
    pass




