from tkinter import *
from tkinter.ttk import *
from typing import Dict
import serial
import time
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image
import tkinter as tk
import time
import subprocess

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
        self.tk_select_box_select_com_face = self.__tk_select_box_select_com_face(self)
        self.tk_label_chose_com_word = self.__tk_label_chose_com_word(self)
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
    def __tk_select_box_select_com_face(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("com3","com4","com5","com6")
        cb.place(x=970, y=20, width=150, height=40)
        return cb
    def __tk_label_chose_com_word(self,parent):
        label = Label(parent,text="串口",anchor="center", )
        label.place(x=860, y=20, width=80, height=37)
        return label
class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.data_time_table = []  # 存储时间表格数据
        self.data_adc_table = []  # 存储ADC表格数据
        self.data_adc_table_last=[0,0,0,0,0,0] #储存过期ADC表格数据
        self.time_str="0:0:0:0:0:0"
        self.com = serial.Serial('com3', 9600)  # 初始化串口
        
        # 初始化 data_adc_table_last
        if len(self.data_adc_table) > 0:
            self.data_adc_table_last = self.data_adc_table[-1]

        # 创建定时器，每隔一段时间更新表格数据
        self.after(1000, self.update_tables)

        self.__event_bind()



    def update_time_table(self):
        # 获取最新一行的数据
        latest_row = self.data_time_table[-1]
        # 将时间列表中的元素转换为字符串，并使用":"连接起来
        self.time_str = ":".join([str(time_value) for time_value in latest_row])
        self.tk_table_time_table.delete(*self.tk_table_time_table.get_children())  # 清空表格内容
        self.tk_table_time_table.insert("", "end", values=self.data_time_table[-1])  # 直接插入最新的数据行

    def update_adc_table(self):
        # 取出最新的数据行和上一次数据行
        if len(self.data_adc_table) > 0:
            latest_row = self.data_adc_table[-1]
            last_row = self.data_adc_table_last
        else:
            return

        # 判断最近的一行是否与上一次的一行不同
        if latest_row != last_row:
            # 插入最新的那一行数据
            self.tk_table_adc_table.insert("", 0, values=latest_row + [self.time_str])

        # 插入其他数据行
        for i in range(len(self.data_adc_table) - 2, -1, -1):
            if self.data_adc_table[i] != last_row:
                self.tk_table_adc_table.insert("", "end", values=self.data_adc_table[i])
            else:
                break
        
        # 更新上一次的adc_table数据
        self.data_adc_table_last = latest_row

    def update_tables(self):
        # 获取最新数据
        data = self.get_data()

        # 添加数据到时间表格数据列表
        self.data_time_table.append(data[0:6])

        # 添加数据到ADC表格数据列表
        
        data_copy = [data[6], data[9], data[7], data[10], data[8], data[11]]
        self.data_adc_table.append(data_copy)

        # 如果数据表格为空，则将 data_adc_table_last 初始化为最后一行数据
        if len(self.data_adc_table) == 1:
            self.data_adc_table_last = self.data_adc_table[-1]

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

        #此处设置相关参数 不参与翻蛋等操作
        # 设置send_info中的信息
        temp_time=self.data_time_table;
        send_info = [temp, light,wet,0,0,0,0,0]

        # 进行设置板子的各种信息，将send_info中的数据发送至电脑
        self.set_time_temp_light_wet(send_info)
        print("SET SUCCESS")
        

    def set_time_temp_light_wet(self, send_info):
        write_byte = self.com.write((send_info))

    def get_data(self):
        data = []
        cnt = 0
        
        while cnt != 12:
            byte_data = self.com.read()
            if len(byte_data) > 0:
                data.append(ord(byte_data))
                cnt += 1
        
        return data
    
 

    def reset_info(self,evt):
        self.tk_input_temp_input.delete(0, 'end')
        self.tk_input_light_input.delete(0, 'end')
        self.tk_input_wet_input.delete(0, 'end')
        self.tk_table_time_table.delete(*self.tk_table_time_table.get_children())
        self.tk_table_adc_table.delete(*self.tk_table_adc_table.get_children())
        self.set_time_temp_light_wet([0, 0, 0,2,2,2,2,2])
        print("RESET SUCCESS")
        
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
    
    # 以下几个操作都需要明天把板子返回来的数据加上设定的温度 进行判断
    #翻蛋  1表示翻蛋

    def move_egg(self,evt):
        data=self.get_data()
        data_copy=[data[9],data[10],data[11],1,0,0,0,0]
        self.set_time_temp_light_wet(data_copy)
        print("MOVE EGG SUCCESS")
        
    def get_wind(self,evt):
        data=self.get_data()
        data_copy=[data[9],data[10],data[11],0,1,0,0,0]
        self.set_time_temp_light_wet(data_copy)
        print("GET WIND SUCCESS")
    
    def get_wet(self,evt):
        data=self.get_data()
        data_copy=[data[9],data[10],data[11],0,0,1,0,0]
        self.set_time_temp_light_wet(data_copy)
        print("GET WET SUCCESS")

    def get_hot(self,evt):
        data=self.get_data()
        data_copy=[data[9],data[10],data[11],0,0,0,1,0]
        self.set_time_temp_light_wet(data_copy)
        print("GET HOT SUCCESS")
    
    def get_cold(self,evt):
        data=self.get_data()
        data_copy=[data[9],data[10],data[11],0,0,0,0,1]
        self.set_time_temp_light_wet(data_copy)
        print("GET COLD SUCCESS")

    def auto_set(self,evt):
        data=self.get_data()
        data_copy=[data[9],data[10],data[11],3,0,0,0,0]
        self.set_time_temp_light_wet(data_copy)
        print("AUTOSET SUCCESS")
        
    def get_using_ref(self,evt):
        # 弹出消息框，显示信息
        messagebox.showinfo("详细说明", "即将跳转至PDF")
        # 打开PDF文件，注意将 `your_pdf_file.pdf` 替换为你自己的文件路径
        subprocess.Popen(["start", "", "https://gitee.com/cyf-0706/Intelligent_incubation_management_system/blob/master/final_ref/readme_final%20copy.md"], shell=True)

    def select_com(self,evt):
        selected_port = self.tk_select_box_select_com_face.get()  # 获取选择的串口
        if not selected_port:  # 如果没有选择串口，默认选择com3
            selected_port = 'com3'
        self.com.port = selected_port  # 将选择的串口赋值给self.com的port属性
        try:
            if self.com.is_open:  # 如果串口已经打开，则先关闭它
                self.com.close()
            self.com.open()  # 打开新的串口
            print(f"成功打开串口{selected_port}")
            messagebox.showinfo("串口打开成功", f"成功打开串口{selected_port}")
            # 重新启动更新数据的定时器
            self.after(1000, self.update_tables)
        except serial.SerialException as e:
            messagebox.showerror("串口错误", str(e))

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
        self.tk_select_box_select_com_face.bind('<<ComboboxSelected>>',self.select_com)
        pass
if __name__ == "__main__":
    win = Win()
    win.mainloop()