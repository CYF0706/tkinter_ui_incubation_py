import serial
import numpy as np

com=serial.Serial('com3',9600)

get_data=[]
send_info=[10,10,10,10,10,10,25,35]
cnt=0

#从串口获取信息 储存至get_data
def get_data_pc(c,data):
    if c!=8:
        get_data.append(data)

#清空储存区 get_data
def clear_data_pc(cnt,my_data):
    if cnt==8:
        my_data.clear()

# 设置send_info中的信息
def set_send_info(chosen_number):
    #chosen_number 表示需要执行的操作
    if chosen_number==1:
        #对所有信息进行设置 后续将各个函数进行集合
        pass

    if chosen_number==2:
        #将信息进行重置

        pass

    if chosen_number==3:
        pass

#进行设置板子的各种信息 将send_info中的数据发送至电脑 
def set_time_temp_light_wet(send_info):
    write_byte=com.write(send_info)

def add_send_info(send_info,number):
    for i in range(8):
        send_info[i]+=number


# #发送数据
# while True:
#     print("请输入需要发送的值：")
#     number=eval(input())
#     add_send_info(send_info,number)
#     set_time_temp_light_wet(send_info)



#接收数据
while True:
    while cnt!=8:
        data=ord(com.read())
        get_data_pc(cnt,data)
        cnt+=1
        
        # print(data,end=' ')
        
    for i in get_data:
            print(i,end=" ")
    clear_data_pc(cnt,get_data)
    cnt=0
    print()

    