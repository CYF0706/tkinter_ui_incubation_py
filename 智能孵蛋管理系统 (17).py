from tkinter import *
from tkinter.ttk import *
from typing import Dict
import serial
import time
import tkinter.messagebox as messagebox

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
        btn.place(x=280, y=570, width=195, height=69)
        return btn
    def __tk_button_reset_button(self,parent):
        btn = Button(parent, text="重置", takefocus=False,)
        btn.place(x=770, y=570, width=198, height=68)
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
        columns = {"温度":179,"设定温度":179,"光照":179,"设定光照":179,"湿度":179,"设定湿度":179}
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
        btn.place(x=100, y=670, width=195, height=69)
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
        btn.place(x=380, y=670, width=195, height=69)
        return btn
    def __tk_button_get_more_wet(self,parent):
        btn = Button(parent, text="加湿", takefocus=False,)
        btn.place(x=660, y=670, width=195, height=69)
        return btn
    def __tk_button_get_more_hot(self,parent):
        btn = Button(parent, text="加热", takefocus=False,)
        btn.place(x=950, y=670, width=195, height=69)
        return btn
    def __tk_label_set_parament(self,parent):
        label = Label(parent,text="设置参数",anchor="center", )
        label.place(x=40, y=430, width=98, height=30)
        return label
class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.data_time_table = []  # 存储时间表格数据
        self.data_adc_table = []  # 存储ADC表格数据
        self.com = serial.Serial('com3', 9600)  # 初始化串口

        # 创建定时器，每隔一段时间更新表格数据
        self.after(1000, self.update_tables)

        self.__event_bind()

    def update_time_table(self):
        self.tk_table_time_table.delete(*self.tk_table_time_table.get_children())  # 清空表格内容
        self.tk_table_time_table.insert("", "end", values=self.data_time_table[-1])  # 直接插入最新的数据行

    def update_adc_table(self):

        self.tk_table_adc_table.delete(*self.tk_table_adc_table.get_children())  # 清空表格内容
        if len(self.data_adc_table) > 0:
            self.tk_table_adc_table.insert("", 0, values=self.data_adc_table[-1])  # 插入最新的数据行
        for i in range(len(self.data_adc_table) - 2, -1, -1):
            self.tk_table_adc_table.insert("", "end", values=self.data_adc_table[i])  # 插入其他数据行

    def update_tables(self):
        # 获取最新数据
        data = self.get_data()
        
        # 添加数据到时间表格数据列表
        self.data_time_table.append(data[0:6])

        # 添加数据到ADC表格数据列表
        data_copy=[data[6],0,data[7],0,0,0]
        if(data_copy[0]!=0):
            self.data_adc_table.append(data_copy)
        else:
            print("跳过")
        
        

        # 更新表格数据
        self.update_time_table()
        self.update_adc_table()

        # 继续下一次定时器更新
        self.after(1000, self.update_tables)

    def set_info(self, evt):
        temp_input = self.tk_input_temp_input.get()
        wet_input = self.tk_input_wet_input.get()
        light_input = self.tk_input_light_input.get()

        # 将输入框内的值转换为整数，如果没有输入则默认为0
        temp = int(temp_input) if temp_input else 0
        wet = int(wet_input) if wet_input else 0
        light = int(light_input) if light_input else 0

        # 设置send_info中的信息
        temp_time=self.data_time_table;
        send_info = [temp, light,wet,0,0]

        # 进行设置板子的各种信息，将send_info中的数据发送至电脑
        self.set_time_temp_light_wet(send_info)
        print("SUCCESS")
        

    def set_time_temp_light_wet(self, send_info):
        write_byte = self.com.write((send_info))

    def get_data(self):
        data = []
        cnt = 0
        
        while cnt != 8:
            byte_data = self.com.read()
            if len(byte_data) > 0:
                data.append(ord(byte_data))
                cnt += 1
        
        return data
    
    '''
    # def check_reset(self):
    #     # 向设备请求当前状态
    #     self.serial.write(b'get_status\n')
    #     time.sleep(0.1)
    #     data = self.serial.read_all().decode("utf-8").strip()
    #     # 如果当前状态为"0;0;0;0"，则表示重置成功
    #     if data == '0;0;0;0':
    #         return True
    #     else:
    #         return False
    '''

    def reset_info(self,evt):
        self.tk_input_temp_input.delete(0, 'end')
        self.tk_input_light_input.delete(0, 'end')
        self.tk_input_wet_input.delete(0, 'end')
        self.tk_table_time_table.delete(*self.tk_table_time_table.get_children())
        self.tk_table_adc_table.delete(*self.tk_table_adc_table.get_children())
        self.set_time_temp_light_wet([0, 0, 0,2,2])
        
        # reset_sum=0
        # for i in range(6):
        #     reset_sum+=self.data_time_table[i];
        # if(reset_sum==1 and self.data_time_table[5]==1):
        #     messagebox.showinfo("提示", "重置成功！")
        # else:
        #     messagebox.showerror("错误", "重置失败，请重试！")
    
    # # 检测重置是否成功
    #     if self.check_reset():
    #         messagebox.showinfo("提示", "重置成功！")
    #     else:
    #         messagebox.showerror("错误", "重置失败，请重试！")

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
        pass
if __name__ == "__main__":
    win = Win()
    win.mainloop()