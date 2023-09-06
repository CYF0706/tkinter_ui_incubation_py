"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
"""
from tkinter import *
from tkinter.ttk import *
from typing import Dict
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_set_button = self.__tk_button_set_button(self)
        self.tk_button_reset_button = self.__tk_button_reset_button(self)
        self.tk_input_temp_input = self.__tk_input_temp_input(self)
        self.tk_input_light_input = self.__tk_input_light_input(self)
        self.tk_input_wet_input = self.__tk_input_wet_input(self)
        self.tk_table_time_table = self.__tk_table_time_table(self)
        self.tk_table_adc_table = self.__tk_table_adc_table(self)
        self.tk_label_tempword = self.__tk_label_tempword(self)
        self.tk_label_wetword = self.__tk_label_wetword(self)
        self.tk_label_lightword = self.__tk_label_lightword(self)
        self.tk_button_move_egg_button = self.__tk_button_move_egg_button(self)
        self.tk_label_sys_time = self.__tk_label_sys_time(self)
        self.tk_label_now_parameters = self.__tk_label_now_parameters(self)
        self.tk_button_get_more_wind = self.__tk_button_get_more_wind(self)
        self.tk_button_get_more_wet = self.__tk_button_get_more_wet(self)
        self.tk_button_get_more_hot = self.__tk_button_get_more_hot(self)
        self.tk_label_set_parament = self.__tk_label_set_parament(self)
        self.tk_button_get_more_cold = self.__tk_button_get_more_cold(self)
        self.tk_button_get_auto = self.__tk_button_get_auto(self)
        self.tk_button_using_reference = self.__tk_button_using_reference(self)
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 1200
        height = 800
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        # 自动隐藏滚动条
    def scrollbar_autohide(self,bar,widget):
        self.__scrollbar_hide(bar,widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
    
    def __scrollbar_show(self,bar,widget):
        bar.lift(widget)
    def __scrollbar_hide(self,bar,widget):
        bar.lower(widget)
    
    def vbar(self,ele, x, y, w, h, parent):
        sw = 15 # Scrollbar 宽度
        x = x + w - sw
        vbar = Scrollbar(parent)
        ele.configure(yscrollcommand=vbar.set)
        vbar.config(command=ele.yview)
        vbar.place(x=x, y=y, width=sw, height=h)
        self.scrollbar_autohide(vbar,ele)
    def __tk_button_set_button(self,parent):
        btn = Button(parent, text="设置", takefocus=False,)
        btn.place(x=60, y=570, width=195, height=69)
        return btn
    def __tk_button_reset_button(self,parent):
        btn = Button(parent, text="重置", takefocus=False,)
        btn.place(x=330, y=570, width=193, height=68)
        return btn
    def __tk_input_temp_input(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=210, y=470, width=175, height=58)
        return ipt
    def __tk_input_light_input(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=570, y=470, width=175, height=58)
        return ipt
    def __tk_input_wet_input(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=950, y=470, width=175, height=58)
        return ipt
    def __tk_table_time_table(self,parent):
        # 表头字段 表头宽度
        columns = {"年":180,"月":158,"日":180,"时":158,"分":180,"秒":158}
        tk_table = Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=60, y=80, width=1060, height=67)
        self.vbar(tk_table, 60, 80, 1060, 67,parent)
        return tk_table
    def __tk_table_adc_table(self,parent):
        # 表头字段 表头宽度
        columns = {"温度":158,"设定温度":158,"光照":158,"设定光照":158,"湿度":158,"设定湿度":158,"时间":105}
        tk_table = Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=60, y=220, width=1059, height=199)
        self.vbar(tk_table, 60, 220, 1059, 199,parent)
        return tk_table
    def __tk_label_tempword(self,parent):
        label = Label(parent,text="温度",anchor="center", )
        label.place(x=60, y=470, width=112, height=56)
        return label
    def __tk_label_wetword(self,parent):
        label = Label(parent,text="湿度",anchor="center", )
        label.place(x=790, y=470, width=112, height=56)
        return label
    def __tk_label_lightword(self,parent):
        label = Label(parent,text="光照",anchor="center", )
        label.place(x=430, y=470, width=112, height=56)
        return label
    def __tk_button_move_egg_button(self,parent):
        btn = Button(parent, text="翻蛋", takefocus=False,)
        btn.place(x=600, y=570, width=195, height=69)
        return btn
    def __tk_label_sys_time(self,parent):
        label = Label(parent,text="当前孵化时间",anchor="center", )
        label.place(x=40, y=20, width=101, height=30)
        return label
    def __tk_label_now_parameters(self,parent):
        label = Label(parent,text="当前相关参数",anchor="center", )
        label.place(x=40, y=180, width=100, height=30)
        return label
    def __tk_button_get_more_wind(self,parent):
        btn = Button(parent, text="通风", takefocus=False,)
        btn.place(x=60, y=670, width=195, height=69)
        return btn
    def __tk_button_get_more_wet(self,parent):
        btn = Button(parent, text="加湿", takefocus=False,)
        btn.place(x=330, y=670, width=195, height=69)
        return btn
    def __tk_button_get_more_hot(self,parent):
        btn = Button(parent, text="加热", takefocus=False,)
        btn.place(x=600, y=670, width=195, height=69)
        return btn
    def __tk_label_set_parament(self,parent):
        label = Label(parent,text="设置参数",anchor="center", )
        label.place(x=40, y=430, width=98, height=30)
        return label
    def __tk_button_get_more_cold(self,parent):
        btn = Button(parent, text="降温", takefocus=False,)
        btn.place(x=870, y=670, width=195, height=69)
        return btn
    def __tk_button_get_auto(self,parent):
        btn = Button(parent, text="AUTOSET", takefocus=False,)
        btn.place(x=870, y=570, width=195, height=69)
        return btn
    def __tk_button_using_reference(self,parent):
        btn = Button(parent, text="使用说明", takefocus=False,)
        btn.place(x=520, y=760, width=83, height=30)
        return btn
class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
    def set_info(self,evt):
        print("<Button-1>事件未处理:",evt)
    def reset_info(self,evt):
        print("<Button-1>事件未处理:",evt)
    def set_temp(self,evt):
        print("<Button-1>事件未处理:",evt)
    def set_light(self,evt):
        print("<Button-1>事件未处理:",evt)
    def set_wet(self,evt):
        print("<Button-1>事件未处理:",evt)
    def set_time_pc(self,evt):
        print("<<TreeviewSelect>>事件未处理:",evt)
    def set_adc_pc(self,evt):
        print("<<TreeviewSelect>>事件未处理:",evt)
    def move_egg(self,evt):
        print("<Button-1>事件未处理:",evt)
    def get_wind(self,evt):
        print("<Button-1>事件未处理:",evt)
    def get_wet(self,evt):
        print("<Button-1>事件未处理:",evt)
    def get_hot(self,evt):
        print("<Button-1>事件未处理:",evt)
    def get_cold(self,evt):
        print("<Button-1>事件未处理:",evt)
    def auto_set(self,evt):
        print("<Button-1>事件未处理:",evt)
    def get_using_ref(self,evt):
        print("<Button-1>事件未处理:",evt)
    def __event_bind(self):
        self.tk_button_set_button.bind('<Button-1>',self.set_info)
        self.tk_button_reset_button.bind('<Button-1>',self.reset_info)
        self.tk_input_temp_input.bind('<Button-1>',self.set_temp)
        self.tk_input_light_input.bind('<Button-1>',self.set_light)
        self.tk_input_wet_input.bind('<Button-1>',self.set_wet)
        self.tk_table_time_table.bind('<<TreeviewSelect>>',self.set_time_pc)
        self.tk_table_adc_table.bind('<<TreeviewSelect>>',self.set_adc_pc)
        self.tk_button_move_egg_button.bind('<Button-1>',self.move_egg)
        self.tk_button_get_more_wind.bind('<Button-1>',self.get_wind)
        self.tk_button_get_more_wet.bind('<Button-1>',self.get_wet)
        self.tk_button_get_more_hot.bind('<Button-1>',self.get_hot)
        self.tk_button_get_more_cold.bind('<Button-1>',self.get_cold)
        self.tk_button_get_auto.bind('<Button-1>',self.auto_set)
        self.tk_button_using_reference.bind('<Button-1>',self.get_using_ref)
        pass
if __name__ == "__main__":
    win = Win()
    win.mainloop()