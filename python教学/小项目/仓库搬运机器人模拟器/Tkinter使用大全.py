# -*- coding: utf-8 -*-
# ============================================================================
#  ████████████████████████████████████████████████████████████████████████
#  ██                                                                      ██
#  ██      TKINTER 使用大全  +  万能配色大全  （学习参考手册）                ██
#  ██                                                                      ██
#  ████████████████████████████████████████████████████████████████████████
#
# 【这个文件怎么用】
#   1. 直接运行本文件（python Tkinter使用大全.py）
#      → 会弹出一个"目录"窗口，点任意按钮就能打开对应模块的演示窗口；
#   2. 每个演示窗口的代码就是一个独立函数 demo_xxx()，
#      想抄哪个模块，就把那个函数复制走即可（记得把 _root() 换成你自己的窗口）；
#   3. 所有"表格类"的说明都写在注释里，注释比代码还值钱喵；
#   4. tkinter 官方有上千个方法，本文件覆盖日常 99% 的控件、布局、画图、事件、配色，
#      极冷门的方法请查官方文档：https://docs.python.org/zh-cn/3/library/tkinter.html
#
# 【目录】
#   第 01 章  快速开始 / 窗口基础        （Tk、Toplevel、标题、尺寸、居中、关闭协议）
#   第 02 章  万能配色大全                （8 套现成配色 + 配色规则 + 色卡演示）
#   第 03 章  变量类 Variable             （StringVar / IntVar / DoubleVar / BooleanVar）
#   第 04 章  控件通用参数大全            （几乎所有控件都能用的参数，注释表）
#   第 05 章  布局三剑客 pack/grid/place  （每种布局一个演示窗口）
#   第 06 章  常用控件逐个详解            （Label~Menu、滚动条、对话框……每个一个演示）
#   第 07 章  Canvas 画图大全             （直线/矩形/圆/弧/多边形/文字/图片/动画）
#   第 08 章  事件绑定 bind 大全          （鼠标/键盘/移动/滚轮 + 事件对象属性表）
#   第 09 章  字体 Font                   （family/size/weight/measure）
#   第 10 章  定时器 after                （倒计时 + 动画循环）
#   第 11 章  常见坑 & 必学技巧           （lambda 陷阱、窗口居中、图片引用……）
# ============================================================================

import tkinter as tk
import tkinter.font as tkfont  # 字体模块（第 09 章）
from tkinter import colorchooser  # 弹窗：取色器
from tkinter import filedialog  # 弹窗：打开/保存文件
from tkinter import messagebox  # 弹窗：提示/警告/错误/确认
from tkinter import simpledialog  # 弹窗：输入框
from tkinter import ttk  # ttk 控件（更现代外观的一部分控件）

# ---------------------------------------------------------------------------
# 全局唯一的"根窗口"懒加载器：
# 演示函数都从它身上开 Toplevel 子窗口，这样本文件运行起来互不干扰。
# 你自己写程序时不需要它，直接用 root = tk.Tk() 即可喵。
# ---------------------------------------------------------------------------
_root_window = None


def _root():
    """拿根窗口：第一次调用才创建；如果已经由主程序创建则直接复用。"""
    global _root_window
    if _root_window is None:
        _root_window = tk.Tk()
        _root_window.withdraw()  # 隐藏主窗口，只显示演示子窗口
    return _root_window


def _win(title, w=520, h=420):
    """快速造一个演示子窗口（帮演示代码省三行）"""
    win = tk.Toplevel(_root())
    win.title(title)
    win.geometry(f"{w}x{h}+120+80")
    return win


# ============================================================================
#  第 01 章  快速开始 / 窗口基础
# ============================================================================
def demo_window_basic():
    """最小可运行模板 + 窗口常用操作"""
    win = _win("第 01 章：窗口基础")

    # ---- 标题 / 尺寸 / 能否拉伸 ------------------------------------------
    win.title("我的窗口")  # 窗口标题
    win.geometry("400x300")  # 宽x高（单位：像素）
    win.resizable(False, False)  # 禁止用户拖动改变大小（(宽, 高)）
    # win.minsize(300, 200)                    # 最小尺寸限制
    # win.maxsize(600, 400)                    # 最大尺寸限制

    # ---- 窗口背景色 -------------------------------------------------------
    win.config(bg="#EAFBF7")  # 背景色（任意控件都可用 bg= 参数）

    # ---- 窗口图标（Windows 专用，文件不存在会报错，建议 try 包住） --------
    # try:
    #     win.iconbitmap("icon.ico")
    # except tk.TclError:
    #     pass                                  # 没图标就算了，别让程序崩

    # ---- 窗口居中（万能公式，抄走就能用） --------------------------------
    win.update_idletasks()  # 先让 Tk 算出窗口真实大小
    w, h = win.winfo_width(), win.winfo_height()
    x = (win.winfo_screenwidth() - w) // 2  # 屏幕宽 - 窗口宽 再对半分
    y = (win.winfo_screenheight() - h) // 2
    win.geometry(f"+{x}+{y}")  # 只设置位置（+x+y）

    # ---- 点右上角 × 时执行什么 ------------------------------------------
    # 默认行为是销毁窗口；也可以换成询问：
    def on_close():
        if messagebox.askyesno("确认", "真的要关闭吗喵？"):
            win.destroy()

    win.protocol("WM_DELETE_WINDOW", on_close)

    tk.Label(win, text="这是最小的窗口模板喵", font=("微软雅黑", 14),
             bg="#EAFBF7", fg="#0F4C49").pack(pady=40)
    tk.Button(win, text="关闭", command=win.destroy).pack()

    # ---- 其他常用窗口方法（抄用即可） ------------------------------------
    # win.attributes("-topmost", True)          # 置顶窗口
    # win.attributes("-alpha", 0.8)             # 半透明（0.0~1.0）
    # win.state("zoomed")                       # 最大化（Windows）
    # win.iconify()                             # 最小化
    # win.lift()                                # 提到最前
    # win.focus_force()                         # 抢焦点


# ============================================================================
#  第 02 章  万能配色大全
# ============================================================================
# 【配色万能规则（先看这几句，比色卡重要）】
#   1. 60-30-10 法则：主色占 60%（背景），辅助色占 30%（按钮/卡片），
#      强调色只占 10%（等号键、危险操作、重点按钮）；
#   2. 同一个界面别超过 5 个颜色，多出来的用"同色系深浅"代替新颜色；
#   3. 对比度铁律：浅底配深字，深底配白字（灰字白底 = 看不清）；
#   4. 一冷一暖才好看：冷色主调（青/蓝/绿）配暖色点缀（橙/粉/金）；
#   5. 别用纯黑 #000000（太死板），用带一点点色相的深色（如 #0F4C49）；
#   6. 在线配色工具：coolors.co（随机生成）、colorhunt.co（现成套色）、
#      webaim.org（对比度检测，无障碍标准）。
# ============================================================================

PALETTES = {
    # 每一套的 key 含义（所有套色统一，方便换主题）：
    #   bg             → 窗口/页面背景
    #   surface        → 卡片、输入框、面板底色（比 bg 亮一档或暗一档）
    #   primary        → 主按钮、选中状态、进度条
    #   primary_active → 主按钮按下/悬停色
    #   text           → 常规文字颜色
    #   accent         → 强调色（等号键、链接、重点提示）
    #   success        → 成功提示（绿色系）
    #   danger         → 危险/错误提示（红橙色系）

    "初音青（Miku 官方绿）": {
        "bg": "#39C5BB", "surface": "#EAFBF7",
        "primary": "#1F8C85", "primary_active": "#176F6A",
        "text": "#0F4C49", "accent": "#FF7043",
        "success": "#2E9E96", "danger": "#E8505B",
    },
    "暗夜黑金": {
        "bg": "#1E1E2E", "surface": "#2B2B3C",
        "primary": "#F5C518", "primary_active": "#D4A90E",
        "text": "#E8E8F0", "accent": "#FF6B6B",
        "success": "#4CC38A", "danger": "#FF5C5C",
    },
    "樱花粉": {
        "bg": "#FFF5F7", "surface": "#FFFFFF",
        "primary": "#F48FB1", "primary_active": "#EC7CA3",
        "text": "#5D3A4B", "accent": "#7E57C2",
        "success": "#66BB6A", "danger": "#EF5350",
    },
    "商务蓝": {
        "bg": "#F4F7FB", "surface": "#FFFFFF",
        "primary": "#2F6FED", "primary_active": "#255AC2",
        "text": "#22314E", "accent": "#0EA5A5",
        "success": "#2FA36B", "danger": "#E5484D",
    },
    "森林绿": {
        "bg": "#F2F7F2", "surface": "#FFFFFF",
        "primary": "#3E8E5A", "primary_active": "#337A4C",
        "text": "#1E3A2A", "accent": "#D9A441",
        "success": "#4CAF50", "danger": "#D9534F",
    },
    "简约灰白（iOS 风）": {
        "bg": "#F5F5F7", "surface": "#FFFFFF",
        "primary": "#333333", "primary_active": "#1A1A1A",
        "text": "#111111", "accent": "#007AFF",
        "success": "#34C759", "danger": "#FF3B30",
    },
    "夕阳橙紫": {
        "bg": "#FFF4EC", "surface": "#FFFFFF",
        "primary": "#FF7043", "primary_active": "#E85D3A",
        "text": "#3D2C2C", "accent": "#7C4DFF",
        "success": "#66BB6A", "danger": "#D32F2F",
    },
    "赛博霓虹": {
        "bg": "#0D0D1A", "surface": "#1A1A2E",
        "primary": "#00E5FF", "primary_active": "#00B8CC",
        "text": "#E0F7FF", "accent": "#FF2E97",
        "success": "#00FF9C", "danger": "#FF3B6B",
    },
}


# 计算器按钮速查（把上面的套色落地的例子）：
#   数字键    bg=surface        fg=text
#   运算符    bg=primary        fg=白
#   等号键    bg=accent         fg=白
#   清除键 C  bg=柔粉 #F8BBD0   fg=#7A2E4B（或直接用 danger）


def demo_color_swatches():
    """把 8 套配色画成色卡，一眼看懂每套长什么样"""
    win = _win("第 02 章：万能配色大全（8 套现成色卡）", 760, 620)

    row = 0
    for palette_name, colors in PALETTES.items():
        # 每套色一个 LabelFrame 框，标题就是套色名
        box = tk.LabelFrame(win, text=f" {palette_name} ", font=("微软雅黑", 11, "bold"),
                            padx=6, pady=6, fg="#333333")
        box.grid(row=row, column=0, sticky="ew", padx=10, pady=6)
        row += 1

        col = 0
        for key, hex_value in colors.items():
            # 上面：色块（用 Label 的 bg 当色块）
            chip = tk.Label(box, width=14, height=2, bg=hex_value,
                            relief="solid", bd=1)
            chip.grid(row=0, column=col, padx=2)
            # 下面：key 名 + 十六进制码（抄代码时直接看这里）
            tk.Label(box, text=f"{key}\n{hex_value}",
                     font=("Consolas", 8)).grid(row=1, column=col, padx=2)
            col += 1

    tk.Label(win, text="用法：color = PALETTES[\"初音青\"]  →  color[\"primary\"] 就是按钮色",
             fg="#555555").grid(row=row, column=0, pady=8)


# ============================================================================
#  第 03 章  变量类 Variable（界面和代码之间的"传话筒"）
# ============================================================================
# 控件显示的内容可以绑定一个变量：变量一变，界面自动变；用户改界面，变量自动变。
def demo_variables():
    win = _win("第 03 章：变量类 Variable")

    # ---- 四种变量：字符串 / 整数 / 小数 / 布尔 ---------------------------
    v_str = tk.StringVar(value="初始文字")
    v_int = tk.IntVar(value=3)
    v_dbl = tk.DoubleVar(value=3.14)
    v_bool = tk.BooleanVar(value=True)

    # textvariable= 把输入框和变量绑在一起
    tk.Entry(win, textvariable=v_str).pack(pady=4)

    def show():
        # get() 读变量，set() 写变量
        print(f"字符串={v_str.get()}  整数={v_int.get()}  "
              f"小数={v_dbl.get()}  布尔={v_bool.get()}")

    # trace_add：变量一变就自动执行回调（三个参数：模式、回调、函数名）
    v_str.trace_add("write", lambda *a: print("v_str 变了 →", v_str.get()))

    tk.Button(win, text="打印所有变量（看控制台）", command=show).pack(pady=4)
    tk.Checkbutton(win, text="布尔变量（勾= True）", variable=v_bool).pack()
    tk.Scale(win, from_=0, to=10, orient="horizontal", variable=v_int).pack()
    tk.Label(win, text="注意：trace 的回调会收到 3 个参数，所以用了 lambda *a 接住").pack()


# ============================================================================
#  第 04 章  控件通用参数大全（几乎所有控件都认这些参数）
# ============================================================================
# ┌───────────────┬──────────────────────────────────────────────────────────┐
# │ 参数          │ 作用                                                      │
# ├───────────────┼──────────────────────────────────────────────────────────┤
# │ text          │ 控件上显示的文字（Button/Label/Checkbutton……）            │
# │ font          │ 字体，写成元组：("微软雅黑", 14, "bold")                  │
# │ bg / fg       │ 背景色 / 文字色（十六进制如 "#39C5BB"）                   │
# │ activebackground│ 鼠标按下去时的背景色（activeforeground 同理管文字）     │
# │ relief        │ 边框样式：flat 无 / groove 凹槽 / raised 凸起 /           │
# │               │          ridge 凸棱 / sunken 下陷 / solid 实线            │
# │ bd(borderwidth)│ 边框粗细（像素），relief 不是 flat 时才看得到            │
# │ cursor        │ 鼠标悬停样式："hand2" 小手 / "arrow" 箭头 /               │
# │               │              "crosshair" 十字 / "watch" 沙漏 / "fleur"   │
# │ state         │ 可用状态："normal" 正常 / "disabled" 灰色不可点 /         │
# │               │           "readonly" 只读（Entry 里还能选中复制）        │
# │ width/height  │ 宽度/高度（单位：字符数；像素要加负号，如 width=-100）    │
# │ padx / pady   │ 控件内部文字与边框的水平/垂直留白（像素）                 │
# │ justify       │ 多行文字对齐：left / center / right                      │
# │ anchor        │ 文字在控件里的位置：n s e w ne nw se sw center            │
# │ command       │ 点击时执行的函数（传函数名，不加括号！）                  │
# │ textvariable  │ 绑定的 Variable 变量（见第 03 章）                        │
# │ takefocus     │ 能否用 Tab 键聚焦（True/False）                           │
# └───────────────┴──────────────────────────────────────────────────────────┘


# ============================================================================
#  第 05 章  布局三剑客：pack / grid / place
# ============================================================================
# 铁律：同一个父容器里，pack / grid / place 只能选一种，混用会报错！
def demo_layout_pack():
    """pack：按"方向"排队，最简单"""
    win = _win("第 05 章：pack 布局", 360, 300)

    # side   → 靠哪边：TOP(默认) BOTTOM LEFT RIGHT
    # fill   → 是否填满：tk.X 横向 / tk.Y 纵向 / tk.BOTH 全填
    # expand → 窗口变大时，多余空间是否分给它（True/False）
    # padx/pady → 与邻居的间距（像素）
    tk.Button(win, text="上", bg="#F48FB1").pack(side=tk.TOP, fill=tk.X, padx=8, pady=4)
    tk.Button(win, text="下", bg="#7E57C2").pack(side=tk.BOTTOM, fill=tk.X, padx=8, pady=4)
    tk.Button(win, text="左", bg="#2F6FED", fg="white").pack(side=tk.LEFT, fill=tk.Y, padx=4)
    tk.Button(win, text="右", bg="#2F6FED", fg="white").pack(side=tk.RIGHT, fill=tk.Y, padx=4)
    tk.Button(win, text="中间（expand 才真正居中）").pack(expand=True)


def demo_layout_grid():
    """grid：按"表格"摆放，最适合计算器、表单"""
    win = _win("第 05 章：grid 布局", 420, 320)

    # row / column      → 第几行第几列（从 0 开始）
    # columnspan/rowspan→ 跨几列 / 跨几行
    # sticky            → 在格子里贴哪边：n s e w（可组合 "nsew" 表示撑满）
    # padx/pady         → 外边距；ipadx/ipady → 内边距
    # rowconfigure/columnconfigure + weight → 窗口变大时哪些行列跟着变大
    for i in range(3):
        win.columnconfigure(i, weight=1, uniform="key")  # 3 列平均分宽度
    for i in range(3):
        win.rowconfigure(i, weight=1)  # 3 行平均分高度

    texts = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
    for index, t in enumerate(texts):
        tk.Button(win, text=t, font=("微软雅黑", 16)).grid(
            row=index // 3, column=index % 3, sticky="nsew", padx=3, pady=3)
    # 跨 3 列的按钮
    tk.Button(win, text="0（columnspan=3 跨三列）").grid(
        row=3, column=0, columnspan=3, sticky="ew", padx=3)


def demo_layout_place():
    """place：按"坐标"精确摆放（像素定位，一般不常用）"""
    win = _win("第 05 章：place 布局", 420, 300)
    win.config(bg="#1E1E2E")

    # x / y       → 绝对坐标（像素，原点在左上角）
    # relx / rely → 相对坐标（0.0~1.0，0.5 就是正中间，随窗口缩放！）
    # anchor      → 以控件的哪个点对齐坐标（"center" 就是中心对齐）
    # relwidth/relheight → 宽度是父窗口的百分之几
    tk.Label(win, text="x=20,y=20（绝对定位）", bg="#F5C518").place(x=20, y=20)
    tk.Label(win, text="relx=0.5,rely=0.5（相对定位，永远居中）",
             bg="#00E5FF").place(relx=0.5, rely=0.5, anchor="center")
    tk.Label(win, text="底部通栏（relwidth=1）", bg="#FF2E97", fg="white").place(
        relx=0, rely=0.9, relwidth=1.0)


# ============================================================================
#  第 06 章  常用控件逐个详解
# ============================================================================
def demo_label_button():
    """Label 文字标签 + Button 按钮"""
    win = _win("第 06 章：Label 和 Button", 420, 300)

    # Label：显示文字/图片，不能点
    tk.Label(win, text="我是标签喵", font=("微软雅黑", 16, "bold"),
             bg="#EAFBF7", fg="#0F4C49",
             relief="groove", bd=2,  # 凹槽边框
             padx=20, pady=10).pack(pady=10)

    # Button：点击执行 command
    count = [0]  # 用列表当"计数器"（闭包改数字要用容器）

    def click():
        count[0] += 1
        btn.config(text=f"点了我 {count[0]} 次")

    btn = tk.Button(win, text="点我", command=click,
                    font=("微软雅黑", 14), bg="#1F8C85", fg="white",
                    activebackground="#176F6A",  # 按下变色
                    relief="flat", bd=0,  # 扁平化按钮（现代风）
                    cursor="hand2",  # 悬停小手
                    padx=20, pady=8)
    btn.pack(pady=10)

    # 禁用按钮
    tk.Button(win, text="我被禁用了", state="disabled").pack()


def demo_entry():
    """Entry 单行输入框"""
    win = _win("第 06 章：Entry 输入框", 420, 300)

    # show="*" 可做密码框；state="readonly" 只读（键盘打不进去）
    tk.Label(win, text="普通输入框：").pack()
    e1 = tk.Entry(win, font=("微软雅黑", 14))
    e1.pack(pady=4)

    tk.Label(win, text="密码框（show=*）：").pack()
    tk.Entry(win, show="*", font=("微软雅黑", 14)).pack(pady=4)

    # validate + validatecommand：限制只能输入数字（%P = 输入后框里的新内容）
    def only_digits(new_text):
        return new_text == "" or new_text.isdigit()  # 返回 False 就拒绝这次输入

    vcmd = (win.register(only_digits), "%P")
    tk.Label(win, text="只能输入数字的输入框：").pack()
    tk.Entry(win, validate="key", validatecommand=vcmd).pack(pady=4)

    def read():
        print("你输入了：", e1.get())  # get() 读内容
        e1.delete(0, "end")  # delete(起点, 终点) 清空

    tk.Button(win, text="读取并清空第一个框", command=read).pack(pady=8)


def demo_text():
    """Text 多行文本框（带滚动条）"""
    win = _win("第 06 章：Text 多行文本框", 460, 340)

    txt = tk.Text(win, font=("Consolas", 11), wrap="word")  # wrap 自动换行
    txt.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(8, 0), pady=8)

    # 滚动条必须和文本框互相"牵手"：谁也别落下
    bar = ttk.Scrollbar(win, orient="vertical", command=txt.yview)
    bar.pack(side=tk.RIGHT, fill=tk.Y, pady=8)
    txt.config(yscrollcommand=bar.set)

    # 插入文字（"1.0" 表示第 1 行第 0 个字符；"end" 表示末尾）
    txt.insert("1.0", "第一行\n")
    txt.insert("end", "第二行喵\n" * 30)

    # 给文字上色：先配 tag，再给范围贴 tag
    txt.tag_config("red", foreground="#E5484D")
    txt.tag_add("red", "1.0", "1.3")

    def read_first_line():
        print("第一行内容：", txt.get("1.0", "2.0").strip())  # get 范围

    tk.Button(win, text="读取第一行", command=read_first_line).pack(side=tk.BOTTOM, pady=6)


def demo_listbox():
    """Listbox 列表选择框（带滚动条）"""
    win = _win("第 06 章：Listbox 列表", 420, 340)

    lb = tk.Listbox(win, selectmode=tk.SINGLE,  # SINGLE/BROWSE 单选
                    font=("微软雅黑", 12))  # MULTIPLE/EXTENDED 多选
    for i in range(1, 31):
        lb.insert("end", f"第 {i} 项")
    lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(8, 0), pady=8)

    bar = ttk.Scrollbar(win, orient="vertical", command=lb.yview)
    bar.pack(side=tk.RIGHT, fill=tk.Y, pady=8)
    lb.config(yscrollcommand=bar.set)

    def read():
        sel = lb.curselection()  # 选中项的下标元组，如 (2,)
        if sel:
            print("选中了：", lb.get(sel[0]))
        else:
            print("什么都没选喵")

    tk.Button(win, text="读取选中项", command=read).pack(side=tk.BOTTOM, pady=6)


def demo_check_radio():
    """Checkbutton 多选框 + Radiobutton 单选框"""
    win = _win("第 06 章：勾选框和单选框", 420, 300)

    # Checkbutton：多选，variable 存 1/0
    v_a = tk.IntVar()
    v_b = tk.IntVar()
    tk.Checkbutton(win, text="选项 A（可以勾）", variable=v_a).pack(anchor="w", padx=20)
    tk.Checkbutton(win, text="选项 B（也可以勾）", variable=v_b).pack(anchor="w", padx=20)

    # Radiobutton：同组共用一个 variable，值互斥
    v_sex = tk.StringVar(value="喵星人")
    tk.Label(win, text="单选：你是？").pack(anchor="w", padx=20, pady=(12, 0))
    for text, val in [("喵星人", "喵星人"), ("汪星人", "汪星人"), ("人类", "人类")]:
        tk.Radiobutton(win, text=text, variable=v_sex, value=val,
                       command=lambda v=val: print("选了", v)).pack(anchor="w", padx=40)


def demo_scale_spin():
    """Scale 滑杆 + Spinbox 步进数字框"""
    win = _win("第 06 章：滑杆和步进框", 420, 300)

    v = tk.DoubleVar(value=50)
    # from_ / to → 范围（注意 from 是关键字，要加下划线 from_）
    # orient    → horizontal 横 / vertical 竖
    # resolution→ 每格精度
    tk.Scale(win, from_=0, to=100, orient="horizontal", variable=v,
             resolution=1, tickinterval=20, length=300,
             label="拖动我（Scale）").pack(pady=10)

    tk.Label(win, text="当前值会随滑杆自动变：" + str(v.get())).pack()

    # Spinbox：带上下箭头的数字框，也能直接输入
    sp = tk.Spinbox(win, from_=0, to=10, increment=0.5,
                    font=("微软雅黑", 14), width=8)
    sp.pack(pady=10)
    tk.Button(win, text="读取 Spinbox", command=lambda: print(sp.get())).pack()


def demo_combobox_progress():
    """ttk.Combobox 下拉框 + ttk.Progressbar 进度条 + ttk.Separator 分隔线"""
    win = _win("第 06 章：下拉框和进度条", 420, 320)

    # Combobox：能选也能打的"下拉列表"；state="readonly" 只能选
    cb = ttk.Combobox(win, values=["选项一", "选项二", "选项三"],
                      state="readonly", font=("微软雅黑", 12))
    cb.current(0)  # 默认选中第 0 项
    cb.pack(pady=10)
    # 选中变化事件（ttk 控件用 <<>> 双尖括号事件名）
    cb.bind("<<ComboboxSelected>>", lambda e: print("选了这个：", cb.get()))

    # Separator：一条分隔线
    ttk.Separator(win, orient="horizontal").pack(fill=tk.X, padx=20, pady=8)

    # Progressbar：进度条
    #   mode="determinate" 定长进度：step(10) 走一步
    #   mode="indeterminate" 来回滚动：start(15) 开始 / stop() 停止（用于"不知道要多久"）
    bar = ttk.Progressbar(win, length=300, mode="determinate", maximum=100)
    bar.pack(pady=10)

    def go():
        bar["value"] = 0
        bar.step(20)  # 每次 +20

    tk.Button(win, text="走一步（+20）", command=go).pack()


def demo_frame_labelframe():
    """Frame 容器 + LabelFrame 带标题容器（分组布局全靠它们）"""
    win = _win("第 06 章：容器 Frame / LabelFrame", 460, 300)

    # Frame：单纯的分组盒子，本身看不见，用来装别的控件
    top = tk.Frame(win, bg="#EAFBF7", relief="groove", bd=2)
    top.pack(fill=tk.X, padx=10, pady=10)
    tk.Label(top, text="我是 Frame 里的标签", bg="#EAFBF7").pack(pady=10)

    # LabelFrame：带标题的框，一眼知道这组是干嘛的
    group = tk.LabelFrame(win, text=" 登录信息（LabelFrame） ",
                          font=("微软雅黑", 11, "bold"), padx=10, pady=10)
    group.pack(fill=tk.X, padx=10)
    tk.Label(group, text="用户名：").grid(row=0, column=0, sticky="e")
    tk.Entry(group).grid(row=0, column=1, pady=4)
    tk.Label(group, text="密  码：").grid(row=1, column=0, sticky="e")
    tk.Entry(group, show="*").grid(row=1, column=1, pady=4)


def demo_panedwindow():
    """PanedWindow 可拖动分隔条（拖中间那条缝试试）"""
    win = _win("第 06 章：PanedWindow 拖动分栏", 460, 300)

    pw = tk.PanedWindow(win, orient="horizontal", sashrelief="raised")
    pw.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
    left = tk.Label(pw, text="左栏（拖中间的缝可以调整大小）", bg="#F48FB1")
    right = tk.Label(pw, text="右栏", bg="#2F6FED", fg="white")
    pw.add(left, minsize=100)  # minsize 最小宽度
    pw.add(right, minsize=100)


def demo_notebook():
    """ttk.Notebook 多页签窗口（设置面板常用）"""
    win = _win("第 06 章：Notebook 页签", 440, 300)

    nb = ttk.Notebook(win)
    nb.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    page1 = tk.Frame(nb, bg="#FFF5F7")
    page2 = tk.Frame(nb, bg="#F2F7F2")
    page3 = tk.Frame(nb, bg="#F4F7FB")
    nb.add(page1, text="第一页")
    nb.add(page2, text="第二页")
    nb.add(page3, text="第三页")

    tk.Label(page1, text="页签 1 的内容", bg="#FFF5F7").pack(pady=40)
    tk.Label(page2, text="页签 2 的内容", bg="#F2F7F2").pack(pady=40)
    tk.Label(page3, text="页签 3 的内容", bg="#F4F7FB").pack(pady=40)


def demo_treeview():
    """ttk.Treeview 表格（类似 Excel 的多列列表）"""
    win = _win("第 06 章：Treeview 表格", 520, 360)

    # columns 定义数据列；show="headings" 只显示表头（隐藏默认的 #0 树列）
    tree = ttk.Treeview(win, columns=("name", "score", "level"),
                        show="headings", height=8)
    tree.heading("name", text="名字")
    tree.heading("score", text="分数")
    tree.heading("level", text="等级")
    tree.column("name", width=160)
    tree.column("score", width=100, anchor="center")
    tree.column("level", width=100, anchor="center")
    tree.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    data = [("喵酱", 100, "SSS"), ("汪酱", 90, "S"),
            ("兔酱", 80, "A"), ("熊酱", 70, "B")]
    for row in data:
        tree.insert("", "end", values=row)  # 插入一行

    def read():
        sel = tree.selection()  # 选中行的 id 元组
        if sel:
            print("整行数据：", tree.item(sel[0], "values"))
        else:
            print("没选行")

    tk.Button(win, text="读取选中行", command=read).pack(pady=6)


def demo_menu():
    """Menu 菜单栏 + OptionMenu 下拉选择 + 右键菜单"""
    win = _win("第 06 章：菜单大全", 460, 320)

    # ---- 1. 顶部菜单栏：先建 Menu 当菜单栏，再挂 cascade 下拉 ------------
    menubar = tk.Menu(win)
    file_menu = tk.Menu(menubar, tearoff=0)  # tearoff=0 去掉"虚线撕下"功能
    file_menu.add_command(label="打开", command=lambda: print("打开喵"))
    file_menu.add_separator()  # 分隔线
    file_menu.add_command(label="退出", command=win.destroy)
    menubar.add_cascade(label="文件", menu=file_menu)

    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="关于", command=lambda: messagebox.showinfo("关于", "Tkinter 教程喵"))
    menubar.add_cascade(label="帮助", menu=help_menu)
    win.config(menu=menubar)

    # ---- 2. OptionMenu：点击展开的下拉按钮（不是菜单栏） -----------------
    v = tk.StringVar(value="选一个喵")
    tk.OptionMenu(win, v, "选项 A", "选项 B", "选项 C").pack(pady=20)
    v.trace_add("write", lambda *a: print("OptionMenu 选了：", v.get()))

    # ---- 3. 右键菜单：bind Button-3 + post ------------------------------
    pop = tk.Menu(win, tearoff=0)
    pop.add_command(label="复制", command=lambda: print("复制喵"))
    pop.add_command(label="粘贴", command=lambda: print("粘贴喵"))

    def right_click(e):
        pop.post(e.x_root, e.y_root)  # 在鼠标位置弹出

    win.bind("<Button-3>", right_click)

    # ---- 4. 全局快捷键：任何窗口里按 Esc 都执行 --------------------------
    win.bind_all("<Escape>", lambda e: win.destroy())
    tk.Label(win, text="在窗口里右键试试；按 Esc 关闭本窗口").pack()


def demo_dialogs():
    """弹窗四件套：提示 / 确认 / 输入 / 文件 + 取色器"""
    win = _win("第 06 章：对话框大全", 420, 420)

    def info():
        messagebox.showinfo("提示", "这是提示信息喵")

    def warn():
        messagebox.showwarning("警告", "这是警告信息喵")

    def err():
        messagebox.showerror("错误", "这是错误信息喵")

    def ask():
        # 三个确认类都会返回布尔值：True / False
        if messagebox.askyesno("确认", "确定要这样做吗？"):
            print("你选了：是")
        messagebox.askokcancel("确认", "okcancel 也有返回值")
        messagebox.askretrycancel("确认", "retrycancel 也有返回值")

    def ask_input():
        name = simpledialog.askstring("输入", "你的名字是？", initialvalue="喵酱")
        age = simpledialog.askinteger("输入", "你的年龄是？", minvalue=0, maxvalue=150)
        score = simpledialog.askfloat("输入", "你的成绩是？")
        print(name, age, score)

    def open_file():
        # filetypes：过滤文件类型；返回值是完整路径字符串
        path = filedialog.askopenfilename(
            title="选择一个文件",
            filetypes=[("Python 文件", "*.py"), ("所有文件", "*.*")])
        print("打开：", path)

    def save_file():
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("文本", "*.txt")])
        print("保存到：", path)

    def pick_dir():
        print("文件夹：", filedialog.askdirectory())

    def pick_color():
        # 返回值是 ((r,g,b), '#hex')，取消时是 (None, None)
        result = colorchooser.askcolor(color="#39C5BB", title="选一个颜色")
        print("取色结果：", result)
        if result[1]:
            win.config(bg=result[1])  # 把窗口背景换成选中的颜色

    buttons = [("showinfo 提示", info), ("showwarning 警告", warn),
               ("showerror 错误", err), ("askyesno 确认", ask),
               ("输入框三连", ask_input), ("打开文件", open_file),
               ("保存文件", save_file), ("选文件夹", pick_dir),
               ("取色器", pick_color)]
    for i, (text, cmd) in enumerate(buttons):
        tk.Button(win, text=text, command=cmd, width=18).grid(
            row=i // 3, column=i % 3, padx=6, pady=6)


# ============================================================================
#  第 07 章  Canvas 画图大全
# ============================================================================
# Canvas 坐标系：原点在左上角，x 向右变大，y 向下变大。
# 所有 create_xxx 都返回一个"图形 id"，之后靠 id 移动/改色/删除。
def demo_canvas_basic():
    """Canvas 所有基本图形一次画全"""
    win = _win("第 07 章：Canvas 画图大全", 620, 460)

    c = tk.Canvas(win, width=600, height=380, bg="#FFFFFF",
                  cursor="crosshair")
    c.pack(padx=8, pady=8)

    # ---- 直线：起点(x1,y1) 终点(x2,y2) ----------------------------------
    # arrow 箭头：tk.FIRST 起点 / tk.LAST 终点 / tk.BOTH 两头
    # dash  虚线：(线长, 空长) 可写多个数字
    # smooth=True 贝塞尔曲线平滑（配合多组坐标）
    c.create_line(10, 10, 200, 10, fill="#E5484D", width=3,
                  arrow=tk.LAST, dash=(6, 3))

    # ---- 矩形：左上角(x1,y1) 右下角(x2,y2) -------------------------------
    c.create_rectangle(20, 40, 120, 140, fill="#39C5BB", outline="#0F4C49", width=2)

    # ---- 椭圆/圆：外接矩形的两个对角；outline="" 表示不要描边 ------------
    c.create_oval(140, 40, 240, 140, fill="#FF7043", outline="")

    # ---- 圆弧/扇形：start 起始角度(度)，extent 扫过角度 -------------------
    # style：tk.PIESLICE 扇形（默认）/ tk.CHORD 弓形 / tk.ARC 只有弧线
    c.create_arc(260, 40, 360, 140, start=30, extent=240,
                 style=tk.PIESLICE, fill="#7C4DFF", outline="")
    c.create_arc(380, 40, 480, 140, start=0, extent=180,
                 style=tk.ARC, outline="#007AFF", width=4)

    # ---- 多边形：顶点坐标两两一组，自动闭合 ------------------------------
    c.create_polygon(20, 170, 130, 170, 75, 250, fill="#F5C518", outline="#333")

    # ---- 文字：anchor 是文字的哪个点对齐 (x,y) ---------------------------
    c.create_text(300, 40, text="Canvas 原点在左上角喵",
                  font=("微软雅黑", 12), fill="#333333", anchor="nw")

    # ---- 图片：PhotoImage 生成纯色块（不需要外部文件） -------------------
    img = tk.PhotoImage(width=80, height=80)
    img.put("#F8BBD0", to=(0, 0, 80, 80))  # 给图片区域填色
    c.create_image(560, 260, image=img, anchor="center")
    c.img = img  # 必须保存引用！否则图片会被回收消失

    # ---- 网格线示例：循环画线 --------------------------------------------
    for x in range(0, 600, 50):
        c.create_line(x, 300, x, 380, fill="#DDDDDD")
    for y in range(300, 380, 20):
        c.create_line(0, y, 600, y, fill="#DDDDDD")

    # ---- 图形的四种常用操作（id 靠 create 的返回值拿） -------------------
    rect = c.create_rectangle(300, 300, 380, 360, fill="#2F6FED", outline="")

    def change():
        c.itemconfig(rect, fill="#FF7043")  # 改属性
        c.coords(rect, 300, 300, 420, 380)  # 直接改坐标
        c.move(rect, -100, -20)  # 平移 dx, dy
        # c.delete(rect)                       # 删除图形

    tk.Button(win, text="操作蓝色矩形（变色/改坐标/平移）", command=change).pack()

    # 图形也能绑事件：鼠标点中矩形才触发
    c.tag_bind(rect, "<Button-1>", lambda e: print("点到矩形了！"))


def demo_canvas_animation():
    """Canvas 动画：after 每 16ms 动一格（约 60 帧/秒）"""
    win = _win("第 07 章：Canvas 动画（小球弹来弹去）", 520, 300)

    c = tk.Canvas(win, width=500, height=220, bg="#123F3C")
    c.pack(padx=8, pady=8)

    ball = c.create_oval(10, 90, 34, 114, fill="#39C5BB", outline="")
    dx, dy = 4, 3

    def tick():
        nonlocal dx, dy
        try:
            x1, y1, x2, y2 = c.coords(ball)  # 读小球当前位置
            if x2 >= 500 or x1 <= 0:  # 撞左右墙就反弹
                dx = -dx
            if y2 >= 220 or y1 <= 0:  # 撞上下墙就反弹
                dy = -dy
            c.move(ball, dx, dy)
            win.after(16, tick)  # 16 毫秒后再来一次 ≈ 60fps
        except tk.TclError:
            pass  # 窗口被关了，停止循环，别报错

    tick()


# ============================================================================
#  第 08 章  事件绑定 bind 大全
# ============================================================================
# 事件格式：widget.bind("<事件名>", 回调函数)
# 回调函数必须接收一个参数 e（事件对象），用 lambda e: ... 接住。
# ┌──────────────────────┬───────────────────────────────────────────────┐
# │ 事件名               │ 触发时机                                       │
# ├──────────────────────┼───────────────────────────────────────────────┤
# │ <Button-1>           │ 鼠标左键按下（Button-2 中键，Button-3 右键）   │
# │ <Double-Button-1>    │ 左键双击                                       │
# │ <B1-Motion>          │ 按住左键拖动                                   │
# │ <Motion>             │ 鼠标在控件上移动（不带按键）                   │
# │ <Enter> / <Leave>    │ 鼠标进入 / 离开控件（做悬停变色用这个！）      │
# │ <MouseWheel>         │ 滚轮（Windows 上 e.delta 是 120 的倍数）       │
# │ <KeyPress> 或 <Key>  │ 任意键按下；指定键写 <KeyPress-a>、<Return>、   │
# │                      │ <Escape>、<space>、<Up>、<F1>                  │
# │ <KeyRelease>         │ 按键松开                                       │
# │ <FocusIn>            │ 控件获得焦点（点进输入框时）                   │
# │ <Configure>          │ 窗口/控件大小或位置变化                        │
# │ <Destroy>            │ 控件被销毁                                     │
# └──────────────────────┴───────────────────────────────────────────────┘
# 事件对象 e 的常用属性：
#   e.widget → 触发事件的控件    e.x, e.y → 相对控件左上角的坐标
#   e.x_root, e.y_root → 相对屏幕的坐标
#   e.keysym → 按下的键名(如 "a", "Return")   e.char → 按下的字符
#   e.num → 鼠标按键编号         e.delta → 滚轮方向
#   e.state → 修饰键（有没有按住 Ctrl/Shift）
def demo_bind_events():
    """bind 演示：点、移、键、滚轮全都安排上"""
    win = _win("第 08 章：事件绑定 bind 大全", 480, 400)

    # ---- 鼠标事件 --------------------------------------------------------
    lbl = tk.Label(win, text="点我 / 把鼠标移到我身上 / 按键盘",
                   font=("微软雅黑", 13), bg="#EAFBF7",
                   relief="groove", bd=2, padx=20, pady=16)
    lbl.pack(pady=10)
    lbl.bind("<Button-1>", lambda e: lbl.config(
        text=f"左键点击于 ({e.x},{e.y})"))
    lbl.bind("<Button-3>", lambda e: lbl.config(text="右键点击喵！"))
    lbl.bind("<Enter>", lambda e: lbl.config(bg="#F8BBD0", text="鼠标进来了（悬停变色）"))
    lbl.bind("<Leave>", lambda e: lbl.config(bg="#EAFBF7", text="鼠标离开了"))
    lbl.bind("<Double-Button-1>", lambda e: lbl.config(text="双击喵！"))

    # ---- 键盘事件：绑在输入框上，按一下显示一次 --------------------------
    entry = tk.Entry(win, font=("微软雅黑", 13))
    entry.pack(pady=6)
    entry.bind("<KeyRelease>", lambda e: print("按键：", e.keysym, "字符：", e.char))
    entry.bind("<Return>", lambda e: print("回车啦！内容：", entry.get()))

    # ---- 鼠标移动事件（画布上实时显示坐标） ------------------------------
    c = tk.Canvas(win, width=440, height=120, bg="white")
    c.pack(pady=6)
    tip = c.create_text(220, 60, text="在上面移动鼠标", font=("微软雅黑", 12), fill="#333")
    c.bind("<Motion>", lambda e: c.itemconfig(tip, text=f"坐标：({e.x},{e.y})"))
    c.bind("<B1-Motion>", lambda e: c.create_oval(
        e.x - 2, e.y - 2, e.x + 2, e.y + 2, fill="#FF7043"))  # 按住左键当画笔

    # ---- 滚轮：delta>0 向上滚，<0 向下滚 --------------------------------
    win.bind("<MouseWheel>", lambda e: print("滚轮：", "上" if e.delta > 0 else "下"))

    # ---- bind_all：全局事件（不挑控件，整个程序都响应） -------------------
    # win.bind_all("<F1>", lambda e: messagebox.showinfo("帮助", "F1 全局帮助喵"))


# ============================================================================
#  第 09 章  字体 Font
# ============================================================================
def demo_font():
    """Font 对象：字体想怎么调就怎么调"""
    win = _win("第 09 章：字体 Font", 460, 340)

    # 字体参数：family 字体名 / size 字号 / weight bold / slant italic /
    #          underline 下划线 / overstrike 删除线
    f1 = tkfont.Font(family="微软雅黑", size=18, weight="bold",
                     slant="italic", underline=True)
    f2 = tkfont.Font(family="Consolas", size=14)

    tk.Label(win, text="微软雅黑 18 粗斜体+下划线", font=f1).pack(pady=8)
    tk.Label(win, text="Consolas 14（等宽字体，代码感）", font=f2).pack(pady=8)

    def measure():
        text = "喵喵喵"
        width = f1.measure(text)  # 这段文字需要多少像素宽
        print(f"“{text}” 用 f1 渲染需要 {width} 像素宽")
        print("f1 实际配置：", f1.actual())  # 看字体真实生效的参数
        print("系统前 5 个字体：", tkfont.families()[:5])

    tk.Button(win, text="测量文字宽度并打印字体信息", command=measure).pack(pady=8)


# ============================================================================
#  第 10 章  定时器 after
# ============================================================================
# after(毫秒, 函数) → 到时间自动执行一次（不阻塞界面，和 time.sleep 完全不同！）
# after_cancel(id)  → 取消还没执行的定时任务（id 是 after 的返回值）
def demo_timer():
    """after 倒计时：每秒减 1"""
    win = _win("第 10 章：after 定时器（倒计时）", 340, 240)

    lbl = tk.Label(win, text="10", font=("微软雅黑", 60, "bold"), fg="#0F4C49")
    lbl.pack(expand=True)

    remaining = [10]  # 用列表装数字，闭包里才能改

    def count_down():
        try:
            remaining[0] -= 1
            lbl.config(text=str(remaining[0]))
            if remaining[0] > 0:
                win.after(1000, count_down)  # 1 秒后再执行一次
            else:
                lbl.config(text="时间到喵！", fg="#E5484D")
        except tk.TclError:
            pass  # 窗口关了就别再跑了

    win.after(1000, count_down)


# ============================================================================
#  第 11 章  常见坑 & 必学技巧
# ============================================================================
# ┌── 坑 1：循环里创建按钮，command 千万别写 lambda: f(i) ────────────────┐
# │  错误：command=lambda: print(i)     → 10 个按钮全打印最后一个值（9）  │
# │  正确：command=lambda x=i: print(x) → 用默认参数把当前值"锁"进闭包    │
# ├── 坑 2：同一个父容器里 pack/grid/place 混用 → 直接报错                 │
# ├── 坑 3：多窗口要用 Toplevel，别 new 多个 Tk()（一个程序一个 Tk）       │
# ├── 坑 4：PhotoImage 一定要保存引用（self.img = img），否则图片秒消失    │
# ├── 坑 5：回调里的异常会被 tkinter 吞掉 → 回调里写 try/except 打印错误   │
# ├── 坑 6：子线程里不能直接操作界面（会崩），跨线程用 queue + after       │
# ├── 坑 7：ttk 的按钮想改颜色要用 ttk.Style；想简单上色就用 tk.Button    │
# ├── 坑 8：after 循环要能停止（try/except TclError 或 after_cancel）      │
# ├── 坑 9：窗口没显示前 winfo_width() 是 1 → 先 update_idletasks() 再取   │
# └── 坑 10：Entry 想只读用 state="readonly"（还能复制），别用 disabled    │
# ============================================================================


# ============================================================================
#  目录启动器：运行本文件后，点按钮打开对应章节的演示
# ============================================================================
DEMOS = [
    ("第01章 窗口基础", demo_window_basic),
    ("第02章 配色大全", demo_color_swatches),
    ("第03章 变量类", demo_variables),
    ("第05章 pack 布局", demo_layout_pack),
    ("第05章 grid 布局", demo_layout_grid),
    ("第05章 place 布局", demo_layout_place),
    ("Label / Button", demo_label_button),
    ("Entry 输入框", demo_entry),
    ("Text 多行文本", demo_text),
    ("Listbox 列表", demo_listbox),
    ("勾选框/单选框", demo_check_radio),
    ("滑杆/步进框", demo_scale_spin),
    ("下拉框/进度条", demo_combobox_progress),
    ("Frame 容器", demo_frame_labelframe),
    ("PanedWindow", demo_panedwindow),
    ("Notebook 页签", demo_notebook),
    ("Treeview 表格", demo_treeview),
    ("菜单大全", demo_menu),
    ("对话框大全", demo_dialogs),
    ("Canvas 画图", demo_canvas_basic),
    ("Canvas 动画", demo_canvas_animation),
    ("事件绑定 bind", demo_bind_events),
    ("字体 Font", demo_font),
    ("after 定时器", demo_timer),
]

if __name__ == "__main__":
    _root_window = tk.Tk()  # 手动创建主窗口（当目录用）
    _root_window.title("Tkinter 使用大全 —— 目录（点按钮打开对应章节）")
    _root_window.config(bg="#EAFBF7")

    tk.Label(_root_window, text="Tkinter 使用大全 + 万能配色大全",
             font=("微软雅黑", 15, "bold"), bg="#EAFBF7", fg="#0F4C49"
             ).grid(row=0, column=0, columnspan=3, pady=12)
    tk.Label(_root_window, text="想抄哪段代码，就到本文件里找同名的 demo_xxx 函数",
             bg="#EAFBF7", fg="#555555"
             ).grid(row=1, column=0, columnspan=3, pady=(0, 8))

    for i, (name, func) in enumerate(DEMOS):
        btn = tk.Button(_root_window, text=name, command=func, width=22,
                        bg="#FFFFFF", fg="#0F4C49",
                        activebackground="#D9F3EE",
                        relief="flat", bd=0, cursor="hand2", pady=4)
        btn.grid(row=i // 3 + 2, column=i % 3, padx=4, pady=3)

    _root_window.mainloop()
