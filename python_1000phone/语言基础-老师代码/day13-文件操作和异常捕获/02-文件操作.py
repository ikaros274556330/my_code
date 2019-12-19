"""__author__=余婷"""
# 1.数据的存储
"""
1）数据存储的特点
计算机的内存分为硬盘和运行内存:
硬盘是用来存储文件的，除非手动删除或者硬盘出问题，否则存储在硬盘中的文件一直存在不会销毁；
运行内存是用来存储，程序在运行过程中产生的数据; 当程序运行结束后会自动销毁

如果希望程序中产生的数据在程序运行结束后不销毁，就需要将数据存到硬盘中（需要存在文件中）。

2）常用的文件
txt文件、json文件、plist文件、数据库文件等  -- 文本数据
图片文件(png，jpg等)、音频文件(mp3, wav)、视频文件...   -- 二进制文件
"""

# 2.文件操作  - 操作文件内容
"""
文件操作基本步骤:
打开文件(open) -> 操作文件(读read、写)  -> 关闭文件(close)
"""
# 2.1 打开文件
"""
open(file,mode='r',...,encoding=None) 
open(文件路径, 打开方式, 文本编码方式)  -  以指定的方式打开指定文件并且返回文件对象

说明: 
file  -  文件路径; 可以传文件的绝对路径和相对路径
         1) 绝对路径: 文件在计算机中的全路径
         2) 相对路径: ./   -  表示当前目录(当前写代码的那个文件所在的目录) - 可以省略
                    ../   -  表示当前目录的上层目录
                    .../  -  表示当前目录的上层目录的上层目录

mode  -  文件打开方式, 决定打开文件后的操作权限(能读还是能写 - r/w); 操作的文件的时候数据的类型(文本/二进制 - t/b)
         r - 只读；w - 只写; a - 只写; t - 文本数据(默认，可以不写), b - 二进制数据
         r(rt/tr) - 打开文件后只能进行读操作，读出来的数据是字符串
         rb/br    - 打开文件后只能进行读操作, 读出来的数据是二进制数据(bytes)
         w(wt/tw) - 打开文件后只能进行写操作, 写入的数据是字符串；打开的时候先清空原文件
         wb/bw    - 打开文件后只能进行写操作, 写入的数据是二进制数据；打开的时候先清空原文件
         a(at/ta) - 打开文件后只能进行写操作, 写入的数据是字符串；打开的时候不会清空原文件
         ab/ba    - 打开文件后只能进行写操作, 写入的数据是二进制数据；打开的时候不会清空原文件
         
         注意: a、w在打开文件的时候，如果文件不存在，会自动创建文件
              r在打开文件的时候，如果文件不存在,会报错
              
encoding  -  文本文件编码方式; 只能以t的方式打开文本文件的时候可以赋值
             一般采用'utf-8'的编码方式进行编码；保证同一个文件读和写的编码方式要一致
             
"""
# 1.==============文件路径=============
# 1）绝对路径
# open(r'/Users/yuting/Workspace/JAVA/授课/python1906/02-语言基础/day13-文件操作和异常捕获/files/test.txt')

# 2）相对路径
# open('./files/test.txt')
# open('files/test.txt')

# 2.==============打开方式=============
# open('files/test.txt', 'a')
# open('files/luffy.jpg', 'wb')

# open('files/a.txt')  # FileNotFoundError: [Errno 2] No such file or directory: 'files/a.txt'
# open('files/a.txt', 'w')
# open('files/b.txt', 'a')
# open('files2/b.txt', 'a')  # FileNotFoundError: [Errno 2] No such file or directory: 'files2/b.txt'


# 2.2操作文件
"""
1）读操作
文件对象.read()  - 读指定文件，并且返回文件中的内容(所有的文件都支持)
文件对象.readline() - 读指定文件一行的内容(只支持文本文件)

2）写操作
"""
f = open('files/test.txt', 'r', encoding='utf-8')
content = f.read()
print(content)

# 将读写位置移动到文件开头： 文件对象.seek(N)  -  将读写位置移动到第N个字节的位置
f.seek(0)
line = f.readline()
print('line:', line)

# 关闭
f.close()

# print(f.read())   # ValueError: I/O operation on closed file.



# f = open('files/test.txt', 'w')
# content = f.read()  # io.UnsupportedOperation: not readable
# print(content)
print('====================')
f = open('files/test.txt', 'r')
line = f.readline()
print(line)
print('读所有:')
content = f.read()
print(content)

f.close()

print('============练习============')
# 练习: 读指定文本文件中的内容，一行一行的读，读完为止
f = open('files/test.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()

# 文本文件打开方式带b，读出来的数据是二进制数据
f = open('files/test.txt', 'rb')
content = f.read()
print(type(content))   # <class 'bytes'>
f.close()

# 注意: 二进制文件(图片、音频、视频、exe文件等)打开的时候必须带b
f = open('files/luffy.jpg', 'rb')
content = f.read()
print(content)

f.close()


# 2.3 写操作
"""
文件对象.write(内容)  - 将指定的内容写入到指定文件中
"""
f = open('files/test.txt', 'a', encoding='utf-8')
f.write('abc')
f.close()

# 如果写的时候带b,写入数据的类型必须是二进制
f = open('files/test.txt', 'ab')
f.write('hello'.encode())
f.close()

num = 100
f = open('files/num.txt', 'w', encoding='utf-8')
f.write(str(num))
f.close()







