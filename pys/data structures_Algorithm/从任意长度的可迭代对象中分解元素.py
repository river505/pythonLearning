#部分连续的分解, *表达式
#1.去头尾


def dropFirstLast (grades):
    sorted(grades)
    f,*middles,l=grades
    return sum(middles)/len(middles)
# asd=input()
# num = [int(n) for n in asd.split()]
# print(dropFirstLast(num))


# asd=asd.split()
# print(asd)            #split()字符串分割为列表，列表元素仍为字符串


#2.姓名 电邮 若干电话号码
record=('Dave','123456789@qq.com','123-4567-8900','010-1234-5678')
name,email,*tel=record
# print(tel)

