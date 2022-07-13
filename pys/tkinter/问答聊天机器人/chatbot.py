from question_classifier import *
from question_parser import *
from answer_search import *
import pandas as pd
import tkinter as tk
import  collections as cl
'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()#调用问题分类子函数，可以链接追踪
        self.parser = QuestionPaser()#调用问题解析子函数
        self.searcher = AnswerSearcher()#调用问题搜索子函数

    def chat_main(self, sent):
        answer = '没能理解您的问题，我的词汇量有限，请输入更加标准的词语'#这是初始答案
        res_classify = self.classifier.classify(sent)#'sent'是用户的输入内容，利用classify函数先对其进行分类
        if not res_classify:
            return answer#没有找到对应分类内容，返回初始答案
        res_sql = self.parser.parser_main(res_classify)#调用parser_main对内容进行解析
        final_answers = self.searcher.search_main(res_sql)#对内容搜索合适的答案
        if not final_answers:
            return answer#如果没有找到合适的最终答案，返回初始答案
        else:
            return '\n'.join(final_answers)#连接字符
q=cl.deque(maxlen=10)#近十条历史记录
qq=cl.deque()#所有历史记录
listqq=[]#辅助项
mainq=cl.deque()#重点关注记录
handler = ChatBotGraph()#构建类
window=tk.Tk()#创建窗口
window.title('医疗问答机器人')
window.geometry('800x300')
e=tk.Entry(window,width=100)#查询栏
e.pack()
num=1#历史记录编号
numout=1#导出文件编号
def ddd():#整句查询功能
    global num
    t.delete("0.0", "end")
    question=e.get()
    answer = handler.chat_main(question)
    asd=answer+'\n\n'
    t.insert('end',asd)
    q.append('   '+str(num)+'    '+question+':'+answer+'   ')
    qq.append('   '+str(num)+'    '+question+':'+answer+'   ')
    listqq.append('   '+str(num)+'    '+question+':'+answer+'   ')
    num +=1
def dd():#近十条历史记录查询
    t.delete("0.0", "end")
    t.insert('end', '近十条历史记录\n')
    t.insert('end',q)
def d():#历史记录
    t.delete("0.0", "end")
    t.insert('end','历史记录\n')
    t.insert('end', qq)
def ddddd():#重点关注添加
    t.delete("0.0", "end")
    number = int(e.get())
    for i in qq:
        if int(i[0:7])==number:
            t.insert('end',i)
            t.insert('end', '\n添加成功！')
            mainq.append(i)
def dddddd():#重点关注展示
    t.delete("0.0", "end")
    t.insert('end', '重点关注\n')
    t.insert('end', mainq)
def ddddddd():#导出
    global numout
    with open('./output{}.txt'.format(numout),'w') as file:
        file.write(t.get('0.0',"end"))
    t.delete("0.0", "end")
    t.insert('end', '导出成功\n')
    numout+=1
def sym():#症状功能
    global num
    t.delete("0.0", "end")
    question = e.get()+'症状'
    answer = handler.chat_main(question)
    asd = answer + '\n\n'
    t.insert('end', asd)
    q.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    qq.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    num += 1
def food():#饮食查询功能
    global num
    t.delete("0.0", "end")
    question = e.get()+'吃什么'
    answer = handler.chat_main(question)
    asd = answer + '\n\n'
    t.insert('end', asd)
    q.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    qq.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    try:
        question = e.get() + '不能吃什么'
        answer = handler.chat_main(question)
        asd = answer + '\n\n'
        t.insert('end', asd)
        q.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
        qq.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    except:
        pass
    num += 1
def complication():#并发症查询
    global num
    t.delete("0.0", "end")
    question = e.get()+'并发症'
    answer = handler.chat_main(question)
    asd = answer + '\n\n'
    t.insert('end', asd)
    q.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    qq.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    num += 1
def medicine():#药物查询
    global num
    t.delete("0.0", "end")
    question = e.get()+'药物'
    answer = handler.chat_main(question)
    asd = answer + '\n\n'
    t.insert('end', asd)
    q.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    qq.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    num += 1
def howtoq():#治疗方法查询
    global num
    t.delete("0.0", "end")
    question = e.get()+'治疗'
    answer = handler.chat_main(question)
    asd = answer + '\n\n'
    t.insert('end', asd)
    q.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    qq.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    num += 1
def season():#病因查询
    global num
    t.delete("0.0", "end")
    question = e.get()+'原因'
    answer = handler.chat_main(question)
    asd = answer + '\n\n'
    t.insert('end', asd)
    q.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    qq.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    num += 1
def group():#易感人群查询
    global num
    t.delete("0.0", "end")
    question = e.get()+'易感人群'
    answer = handler.chat_main(question)
    asd = answer + '\n\n'
    t.insert('end', asd)
    q.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    qq.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    num += 1
def howtofind():#检查方法查询
    global num
    t.delete("0.0", "end")
    question = e.get()+'检查'
    answer = handler.chat_main(question)
    asd = answer + '\n\n'
    t.insert('end', asd)
    q.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    qq.append('   ' + str(num) + '    ' + question + ':' + answer + '   ')
    num += 1
      # 页面布局
fm =tk.Frame(window)
fm.pack()
fmmm=tk.Frame(window)
fmmm.pack()
fm2 =tk.Frame(fmmm)
fm2.pack(side="left")
fm21=tk.Frame(fm2)
fm21.pack()
fm22=tk.Frame(fm2)
fm22.pack()
fm222=tk.Frame(fmmm)
fm222.pack(side="left")
tt=tk.Label(fm222,height=2,width=8,text='python\n程序设计',fg='#7CCD7C')
tt.pack(side="top")
fmm=tk.Frame(fmmm)
fmm.pack()
fm3 =tk.Frame(fmm)
fm3.pack()
fm4 =tk.Frame(fmm)
fm4.pack()
    #按键
b=tk.Button(fm,width=4,bg='lightsteelblue',text='查询',command=ddd)
b2=tk.Button(fm21,width=16,bg='lightslategray',text='近十条历史记录',command=dd)
b3=tk.Button(fm21,width=12,bg='lightslategray',text='全部历史记录',command=d)
b5=tk.Button(fm22,width=25,bg='lightslategray',text='加入重点关注（输入历史序号）',command=ddddd)
b6=tk.Button(fm22,width=8,bg='lightslategray',text='重点关注',command=dddddd)
b7=tk.Button(fm21,width=8,bg='lightslategray',text='导出当前',command=ddddddd)
b8=tk.Button(fm3,width=8,bg='lightslategray',text='症状',command=sym)
b9=tk.Button(fm3,width=8,bg='lightslategray',text='食物',command=food)
b10=tk.Button(fm3,width=8,bg='lightslategray',text='并发症',command=complication)
b11=tk.Button(fm3,width=8,bg='lightslategray',text='药品',command= medicine)
b12=tk.Button(fm4,width=8,bg='lightslategray',text='治疗方法',command=howtoq)
b13=tk.Button(fm4,width=8,bg='lightslategray',text='病因',command=season)
b14=tk.Button(fm4,width=8,bg='lightslategray',text='易感人群',command=group)
b15=tk.Button(fm4,width=8,bg='lightslategray',text='检查',command=howtofind)
b.pack()
b3.pack(side="left")
b2.pack(side="left")
b5.pack(side="left")
b6.pack(side="left")
b7.pack(side="left")
b8.pack(side="left")
b9.pack(side="left")
b10.pack(side="left")
b11.pack(side="left")
b12.pack(side="left")
b13.pack(side="left")
b14.pack(side="left")
b15.pack(side="left")
#回答区
t=tk.Text(window,height=300,width=200)
t.pack(side="top")
#循环
window.mainloop()


