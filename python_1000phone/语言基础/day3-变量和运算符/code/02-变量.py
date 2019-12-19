"""__author__=吴佩隆"""
# 1.什么是变量
# 声明变量是用来申请空间保存数据的

"""
1)声明变量的语法
变量名 = 值

2）说明
变量名 - 程序员自己命名的;
        要求:是标识符;不能是关键字
        规范:见名知义;满足PEP8命名规范(所有字母都小写,多个单词用下划线隔开);
            不能使用系统提供的函数名、类名、库名等来给变量命名
            
=     - 赋值符号，将右边的数据赋给左边的变量(动词)
值  -   任何的结果表达式:例如:数据、已经声明的变量、运算表达式......

"""

# 2.变量的使用
"""
使用变量就是在使用变量里面存储的值,变量中的值可以修改
"""

# 3.同时声明多个变量
"""
1)同时声明多个变量赋相同的值
变量名1 = 变量名2 = 变量名3 = ... = 值

2)同时声明多个变量赋不同的值
变量名1,变量名2,变量名3... = 值1,值2,值3,... (前后元素数量不同会报错)
"""

# 4.python声明变量的原理
"""
先开辟空间存储数据(存储的数据需要多大的内存就开辟多少内存空间),然后再将变量和这个数据对应的内存空间关联在一起
变量三要素:
值 - 给变量赋值的数据 - 使用变量
类型 - 给变量赋值的数据的类型(int) - type(变量)
地址 - 给变量的数据在内存中的地址,也是变量中真正存储的东西(0xff) - id(变量)
注意:用一个变量给另一个变量赋值的时候,是将原来变量中数据的地址赋给另一个变量;赋值完成后,数据还是只有一个
"""
a = 10
print(a)
print(type(a))
print(id(a))