import  ui_common as ui
import tkinter as tk
#窗口
root = ui.create_window("我的程序", size=(600, 400))
#字符串
inp = tk.StringVar(root)
#输入框
account = ui.labeled_entry(root, text="账号", x=40, y=60, width=320, height=30,textvariable=inp)
#文字显示
result = ui.label(root, "这里显示账号", x=40, y=160, width=320, height=30)

inp1 = tk.StringVar(root)
result1 = ui.label(root, "这里显示账号",textvariable=inp1,x=40, y=160, width=320, height=30)
def read_account():
    uid = account.get()  # 也可以用 account.get()
    print(uid)
#按钮
register = ui.create_window(
    "注册账号",
    size=(300, 300),
    parent=root
)
ui.button(root, "读取账号", read_account, x=40, y=110)

root.mainloop()


