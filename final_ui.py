import tkinter as tk

class ButtonDisplay(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="white")  # 设置背景色为白色
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # 创建按钮控件
        button_frame = tk.Frame(self, bg="white")
        button_frame.pack(side=tk.BOTTOM, pady=100)

        self.set_button = tk.Button(button_frame, text="设置", command=self.set_action, bg="#55b3c0", fg="white",
                                    font=("Helvetica", 24), width=10, height=2)
        self.set_button.pack(side=tk.RIGHT, padx=50)

        self.reset_button = tk.Button(button_frame, text="重置", command=self.reset_action, bg="#55b3c0", fg="white",
                                      font=("Helvetica", 24), width=10, height=2)
        self.reset_button.pack(side=tk.LEFT, padx=50)

    def set_action(self):
        # 设置按钮的操作（示例功能）
        print("执行设置的操作")

    def reset_action(self):
        # 重置按钮的操作（示例功能）
        print("执行重置的操作")

# 创建窗口并设置标题
root = tk.Tk()
root.title("按钮界面")

# 创建按钮显示控件并添加到窗口
button_display = ButtonDisplay(master=root)
button_display.pack(expand=True)

# 获取屏幕大小
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 计算窗口居中的位置
x = int((screen_width - 1920) / 2)
y = int((screen_height - 1500) / 2)

# 设置窗口大小和位置
root.geometry("1920x1500")

# 运行主循环
root.mainloop()
