import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
def test(e):    
    messagebox.showinfo("窗口名称","点击成功")


root=tk.Tk()
root.title("智能养殖系统管理器")
root.geometry("700x500+500+80")


#按钮一
font_1 = font.Font(family='Helvetica', size=30, weight='normal')
btn1 = tk.Button(root,text="设置",font=font_1,bg="LightSkyBlue",foreground="Orange")
btn1.grid(column=10,columnspan=10,row=20,rowspan=10,ipadx=20,ipady=10,padx=200,pady=50)



# btn1.pack()  # 按钮在窗口里面的定位
# btn1.grid(column=10,columnspan=100,row=20,rowspan=3)
btn1.bind("<Button-1>",test) #第一个参数为：按鼠标左键的事件 第二个参数为：要执行的方法的名字




root.mainloop()
