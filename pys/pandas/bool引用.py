import pandas as pd
import numpy as np
#整体上有四个索引：行、列的位置索引（0，1，2，…）、行的标签索引（index）、列标签（columns）
asd=np.array(range(15)).reshape(3,5)
df = pd.DataFrame(asd,index=['小李','小王','小张'],columns=['小张','b','c','d',7] )
#方括号：列标签、只能使用位置索引的多行不限列索引 禁止使用行标签索引和单独的行位置索引
#print(df[1]) # 1 报错
print(df[1:10]) # 2 多行引用
#print(df[1:3][5])#2.2想要区域索引 报错
print(df[1:2]['b']) #2.3区域索引 行索引中[1:2]当作1
#print(df[[1,2]]) #3 想要 多行应用 报错
#print(df['1']) #4 想要尝试行引用 报错
print(df['b']) # 5单列引用
print(df[['b','c']]) # 6多列引用
#print(df['小王']) #6.2想要单行索引 报错


#loc ：只能出现行列标签、行标签 除非行、列标签名是数字 禁止使用任何位置索引
#print(df.loc[1]) #7想要引用行 报错
#print(df.loc[1:2]) # 8想要 多行引用 报错
#print(df.loc[[1,2]]) #9 想要 多行应用 报错
#print(df.loc['1']) #10想要尝试行引用 报错
#print(df.loc['b']) #11想要单列引用 报错
#print(df.loc[['b','c']]) #12想要多列引用 报错
print('检查',df.loc['小张']) # 13行引用 行列同名 因无逗号行在前
print(df.loc[:,'b']) #14列引用
print(df.loc['小张','c']) #15单元素引用
print(df.loc['小王',7]) #16单元素引用 前行后列
print(df.loc['小李':'小张'])#17多行引用、切片、包含结束索引
print(df.loc['小李':'小张','b':7])#区域索引
#print(df.loc['b':'c'])#18想要多列索引报错
print(df.loc[:,'b':'c']) #19多列索引\切片
#print(df.loc[['b','c']])#20想要多列索引 报错
'''
去掉loc时是可以的 见第六条：
print(df[['b','c']]) #多列引用
'''
#iloc 列标签、行位置索引用法同loc
print(df.iloc[1,2])#21单元素索引
print(df.iloc[[1,2]])#22多行索引
print(df.iloc[[1,2],:])
print(df.iloc[1,1]) #23列引用
print(df.iloc[1:2])#24多行引用、切片 不包含结束索引
print(df.iloc[1:2,[3,4]])#25区域引用
print(df.iloc[1])#行  26
print(df.iloc[:,1])#列 27
#总结：
#列表多选的位置 若可以执行，则换为 冒号切片 也可执行
#用标签名切片时包含结束项 位置索引不包含
#在书写舒适性及记忆角度：若想使用纯坐标定位推荐iloc、纯标签名推荐loc
#混用记忆方法 行位置列标签 ：方括号法（见2.3）  行标签列索引：未知、或许用到其他搜索方法
#Series 应看作竖向显示的一行DataFrame 其‘行’的标签其实为列标签

df.index=[1,2,3] #修改行标签
df.columns=[1,2,3,4,5]