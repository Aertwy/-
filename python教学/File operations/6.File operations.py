"""
文件对象 = open（文件路径，访问模式，encoding="编码格式）
f = open("T1.txt","r",encoding="utf-8")
中间省略读写
关闭
f.close()


# with open("T1.txt","r",encoding="utf-8") as f:
#     print(f.encoding)
#
# print(f.closed)检测文件的关闭状态

#读取指定字符/字节
# with open("T1.txt","r",encoding="utf-8") as f:
#     content = f.read()
# print(f"读取到的内容\n{content}")


#打印一行
# with open("T1.txt","r",encoding="utf-8") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     print("第一行",line1,end="")
#     print("第二行", line2)

#遍历列表
# with open("T1.txt","r",encoding="utf-8") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

#只写模式（w）:文件不存在则创建，存在则覆盖给原有内容
with open("T1.txt","r",encoding="utf-8") as f:
    f.write("\nbingbing2")

    #追加模式（num）：文件不纯在则创建，存在则新内容会加在文件末尾，不会覆盖旧内容
with open("T1.txt","num") as f:
    f.write("bingbing2")
"""
"""
读取原来的图片
with open("白葱.jpg","rb") as f:
    f_put = f.read()
备份
with open("白葱.jpg","wb") as f:
    f.write(f_put)



with open(r"E:\python\程序\File operations\白葱.jpg","rb")as f:
    p_put=f.read()
    print(p_put)

with open(r"白葱.jpg","rb")as f:
    p_put=f.read()
    print(p_put)
"""





# ================================================================
#  文件操作速查表（Python 文件读写）
# ================================================================
#
#  一、打开模式（open 的第二个参数）
#  --------------------------------------------------------------
#  r   只读（默认）  ：文件不存在 → 报错；只能读，不能写
#  w   只写          ：不存在则创建，已存在则清空覆盖；只能写，不能读
#  num   追加          ：不存在则创建，已存在则写到末尾；只能写，不能读
#  r+  读写          ：文件不存在 → 报错；可读可写，不覆盖原内容
#  w+  读写          ：不存在则创建，已存在则覆盖；可读可写
#  num+  读写          ：不存在则创建，已存在则追加；可读可写，写在末尾
#
#  ★ 关键：二进制操作要加 b —— rb、wb、ab、rb+、wb+、ab+
#          （二进制模式不能写 encoding）
#  ★ 文本读写建议显式写 encoding="utf-8"，否则 Windows 下默认 GBK 易乱码
#
#  二、常用方法与参数
#  --------------------------------------------------------------
#  open(file, mode="r", encoding="utf-8")   打开文件，返回文件对象
#  with open(...) as f:                     推荐写法，结束自动关闭文件
#  f.read(n)          读 n 个字符；不传 n 则读全文
#  f.readline()       读一行
#  f.readlines()      读所有行，返回列表
#  f.write(s)         写入字符串，返回写入的字符数
#  f.writelines(seq)  写入多行（不会自动加换行符）
#  f.seek(pos)        把文件指针移到指定位置
#  f.tell()           返回当前指针位置
#  f.flush()          把缓冲区内容立即写入磁盘
#  f.close()          关闭文件
#
#  三、注意事项（易错点）
#  --------------------------------------------------------------
#  1. 用 w / w+ 打开会立刻清空原文件！要保留内容请用 num / num+ / r+
#  2. 读完后指针停在文件末尾，再读前要 f.seek(0) 复位
#  3. num / num+ 模式下，write 永远写到文件末尾，seek 也改变不了
#  4. 文件不存在时：r、r+ 抛 FileNotFoundError；其余模式自动新建
#  5. 不用 with 就要记得 f.close()，否则内容可能没写进磁盘
# ================================================================














