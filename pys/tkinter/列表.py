import tkinter as tk
window=tk.Tk()
window.title('index')
window.geometry('200x200')
var1=tk.StringVar()

l=tk.Label(window, bg='yellow', width=40, textvariable=var1)

l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)
b1 = tk.Button(window, text='print selection', width=15, height=2, command = print_selection )
b1.pack()

var2=tk.StringVar()
var2.set((11,22,33,44))
lb=tk.Listbox(window,listvariable=var2)

lb.insert('end',55)
lb.insert(0,'asd')
lb.pack()

window.mainloop()
