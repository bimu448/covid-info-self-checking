import tkinter
from mapper import*
from test import*

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("1600x400+200+50")

def updata():
 if hobby1.get() ==True:
     #message += "money\n"
     s = sqlMapper()
     s.insert_locations()
     s.close_connection()       
 if hobby2.get() == True:
     #message += "power\n"
     s = sqlMapper()
     result = s.get_locations()
     s.close_connection()
     message = ""
     for x in result:
         message += str(x) + "\n"
 if hobby3.get() == True:
     #message += "people\n"
     message = ""
     s = statementData()
     result = s.get_cases()
     for x in result:

         message += x + " ; " + str(result[x]) + "\n"
        
 # 清空text中所有内容
 text.delete(0.0, tkinter.END)
 text.insert(tkinter.INSERT, message)

# 要绑定的变量
hobby1 = tkinter.BooleanVar()
# 多选框
check1 = tkinter.Checkbutton(win, text="refresh", variable=hobby1, command=updata)
check1.pack()
hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text="locations", variable=hobby2, command=updata)
check2.pack()
hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text="cases", variable=hobby3, command=updata)
check3.pack()

text = tkinter.Text(win, width=400, height=5)
text.pack()

win.mainloop()
