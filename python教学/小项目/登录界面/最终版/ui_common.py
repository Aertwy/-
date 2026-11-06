"""薄荷青 Tkinter 工具模块。直接运行看演示，导入时只提供函数。

把本文件和自己的主程序放在同一目录，就能用 import ui_common as ui。
控件的 x、y 是相对于父容器左上角的像素坐标，向右、向下为正。
固定尺寸窗口适合用这些函数精确摆放控件。需要随窗口缩放时，
可以在一个独立的面板里用 Tkinter 自带的 grid 或 pack。
"""

import tkinter as tk


# 改这里可以统一更换配色。深色文字配浅底，提示同时有文字和颜色。
PALETTE = {
    "background": "#39C5BB",    # 窗口主色，薄荷青
    "surface": "#EFFBF8",       # 面板浅底
    "input": "#FFFFFF",         # 输入框
    "border": "#ADCDC6",        # 输入框边线
    "text": "#123F3C",          # 正文
    "muted": "#405D57",         # 说明文字
    "primary": "#11645D",       # 主按钮
    "primary_active": "#0D4D48",
    "secondary": "#D9F3EE",     # 次按钮
    "secondary_active": "#C3E8E0",
    "success": "#17634B",       # 成功提示
    "error": "#A52D42",         # 错误提示、危险按钮
    "error_active": "#842236",
    "on_dark": "#FFFFFF",       # 深底按钮的文字
}


def center_window(window, *, parent=None):
    """根据窗口当前的大小居中。传入 parent 时，以它的位置为基准。"""
    window.update_idletasks()  # 先让 Tk 计算好控件和窗口的尺寸。
    width, height = window.winfo_width(), window.winfo_height()
    # 尚未显示的窗口可能还没有实际尺寸，此时用 Tk 算出的请求尺寸。
    if width == 1 and height == 1:
        width, height = window.winfo_reqwidth(), window.winfo_reqheight()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    if parent is None:
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
    else:
        owner = parent.winfo_toplevel()
        x = owner.winfo_rootx() + (owner.winfo_width() - width) // 2
        y = owner.winfo_rooty() + (owner.winfo_height() - height) // 2

    # 靠近屏幕边缘时，把窗口往里移，尽量露出完整内容。
    x = max(0, min(x, screen_width - width))
    y = max(0, min(y, screen_height - height))
    window.geometry(f"+{x}+{y}")  # 只移动窗口，保留原先设定的宽和高。


def create_window(title, size=(640, 420), *, parent=None, resizable=False):
    """创建薄荷青窗口。主程序调用一次创建主窗口，子窗口传入 parent。"""
    width, height = size
    if width <= 0 or height <= 0:
        raise ValueError("窗口的宽和高必须大于 0")

    if parent is None:
        window = tk.Tk()
    else:
        # 即使传入的是面板，也把弹窗挂到面板所属的窗口。
        parent = parent.winfo_toplevel()
        window = tk.Toplevel(parent)

    window.title(title)
    window.configure(background=PALETTE["background"])
    window.geometry(f"{width}x{height}")
    window.resizable(resizable, resizable)
    center_window(window, parent=parent)
    # 把窗口交给调用者继续添加控件，最后由主程序调用 mainloop()。
    return window


def place(widget, *, x, y, width=None, height=None):
    """用绝对坐标放置任意 Tkinter 控件。尺寸省略时采用控件自身大小。"""
    position = {"x": x, "y": y}
    if width is not None:
        position["width"] = width
    if height is not None:
        position["height"] = height
    widget.place(**position)
    return widget


def panel(parent, *, x, y, width, height, **options):
    """创建浅色面板。面板内控件从面板自己的左上角开始定位。"""
    style = {"background": PALETTE["surface"], "borderwidth": 0}
    style.update(options)
    return place(tk.Frame(parent, **style), x=x, y=y, width=width, height=height)


def label(parent, text="", *, x, y, width=None, height=None, **options):
    """创建左对齐的标签。可以额外传入 font、wraplength 等 Tkinter 选项。"""
    background = PALETTE["surface"]
    if "background" in parent.keys():
        background = parent.cget("background")
    style = {"background": background, "foreground": PALETTE["text"], "anchor": "w"}
    style.update(options)
    return place(tk.Label(parent, text=text, **style), x=x, y=y, width=width, height=height)


def entry(parent, *, x, y, width=200, height=34, masked=False, **options):
    """创建单行输入框并返回 Entry。用 .get() 取值，masked=True 遮住输入。"""
    style = {
        "background": PALETTE["input"],
        "foreground": PALETTE["text"],
        "insertbackground": PALETTE["text"],
        "selectbackground": PALETTE["primary"],
        "selectforeground": PALETTE["on_dark"],
        "highlightbackground": PALETTE["border"],
        "highlightcolor": PALETTE["primary"],
        "highlightthickness": 1,
        "borderwidth": 0,
        "relief": "flat",
        "show": "*" if masked else "",
    }
    style.update(options)  # 比如传入 textvariable=自己的 StringVar。
    return place(tk.Entry(parent, **style), x=x, y=y, width=width, height=height)


def labeled_entry(parent, text, *, x, y, width=280, height=34,
                  label_width=64, gap=12,
                  masked=False ,label_font=("微软雅黑", 12),**options):
    """一行创建标签与输入框。width 是整行宽度，返回右侧的 Entry。"""
    input_width = width - label_width - gap
    if input_width <= 0:
        raise ValueError("整行宽度必须大于标签宽度与间距之和")
    label(parent, text, x=x, y=y,
          width=label_width, height=height,
          font=label_font)
    return entry(parent, x=x + label_width + gap, y=y, width=input_width,
                 height=height, masked=masked, **options)


def button(parent, text, command, *, x, y, width=108, height=36,
           variant="primary", **options):
    """创建按钮。command 传函数名，点击时 Tkinter 才执行它。"""
    variants = {
        "primary": ("primary", "primary_active", "on_dark"),
        "secondary": ("secondary", "secondary_active", "text"),
        "danger": ("error", "error_active", "on_dark"),
    }
    if variant not in variants:
        raise ValueError("按钮样式可选 primary、secondary 或 danger")
    background, active, foreground = variants[variant]
    style = {
        "background": PALETTE[background],
        "foreground": PALETTE[foreground],
        "activebackground": PALETTE[active],
        "activeforeground": PALETTE[foreground],
        "borderwidth": 0,
        "relief": "flat",
        "cursor": "hand2",
    }
    style.update(options)
    widget = tk.Button(parent, text=text, command=command, **style)
    return place(widget, x=x, y=y, width=width, height=height)


def set_status(status_label, text, *, kind="info"):
    """更新已创建的提示标签。kind 可选 info、success 或 error。"""
    colors = {"info": "muted", "success": "success", "error": "error"}
    if kind not in colors:
        raise ValueError("提示类型可选 info、success 或 error")
    status_label.configure(text=text, foreground=PALETTE[colors[kind]])


def demo():
    """运行演示，练习输入、回调、状态提示和子窗口。"""
    root = create_window("小猫工程师 · Tkinter 模板", (600, 400))
    label(root, "薄荷青 · Tkinter 模板", x=28, y=18,
          font=("Microsoft YaHei UI", 20, "bold"))
    label(root, "试试输入、回车和子窗口。", x=29, y=61)
    form = panel(root, x=28, y=98, width=544, height=270)
    account = labeled_entry(form, "账号", x=24, y=25, width=492)
    password = labeled_entry(form, "密码", x=24, y=74, width=492, masked=True)
    status = label(form, x=24, y=127, width=492, height=44, wraplength=490,
                   justify="left")
    set_status(status, "这里会显示操作结果。")

    def submit():
        # 把 .get() 拿到的值交给自己的函数，就能接上项目的业务逻辑。
        if not account.get().strip() or not password.get():
            set_status(status, "请输入账号和密码。", kind="error")
            return
        set_status(status, "已读取输入，可以交给你的业务函数处理。", kind="success")

    def clear():
        account.delete(0, tk.END)
        password.delete(0, tk.END)
        set_status(status, "输入已清空。")
        account.focus_set()

    def open_dialog():
        # 子窗口和主窗口共用同一个事件循环。
        dialog = create_window("子窗口示例", (340, 195), parent=root)
        dialog.transient(root)  # 让系统把它作为主窗口的附属窗口管理。
        label(dialog, "这是一个 Toplevel 子窗口。", x=22, y=26, width=296)
        label(dialog, "可以在这里放注册表单或项目设置。", x=22, y=60, width=296)
        button(dialog, "关闭", dialog.destroy, x=116, y=114)
        dialog.bind("<Escape>", lambda event: dialog.destroy())

    button(form, "读取输入", submit, x=24, y=185)
    button(form, "清空", clear, x=146, y=185, variant="secondary")
    button(form, "打开子窗口", open_dialog, x=268, y=185, width=138, variant="secondary")
    account.focus_set()
    account.bind("<Return>", lambda event: submit())
    password.bind("<Return>", lambda event: submit())
    root.mainloop()


# 直接运行本文件时展示示例。其他程序 import 时，可自行创建窗口。
if __name__ == "__main__":
    demo()
