from tkinter import *
from tkinter.ttk import *
from typing import Dict
import serial
import time
import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image

# 创建窗口对象
root = tk.Tk()
# 加载背景图片
image = Image.open("1151675.jpg")
photo = ImageTk.PhotoImage(image)

# 设置画布背景图片
canvas = tk.Canvas(root, width=1200, height=800)
canvas.create_image(0, 0, image=photo, anchor=tk.NW)
canvas.pack()

# 设置窗口大小为背景图片大小
root.geometry("%dx%d" % (1200, 800))
root.mainloop()
