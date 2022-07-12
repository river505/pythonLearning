class ChangeAbs(int):
    def __new__(cls, val):
        # 填入使用super()内建函数去捕获对应父类以调用它的__new__()方法来计算输入数值的绝对值的代码
        # 求一个数的绝对值的函数为abs()
        # 返回最后的结果
        ########## Begin ##########
        return super(ChangeAbs,cls).__new__(cls,abs(val))
        ########## End ##########

class SortedKeyDict(dict):
    def keys(self):
        # 填入使用super()内建函数去捕获对应父类使输入字典自动排序的代码
        # 返回最后的结果
        ########## Begin ##########
        return sorted(super(SortedKeyDict,self).keys())
        ########## End ##########



