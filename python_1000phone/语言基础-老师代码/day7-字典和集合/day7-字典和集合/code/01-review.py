"""__author__=余婷"""

"""
列表
1.+, *, ==, !=, is, (>, >=, <, <=)
2.in, not in
3.max, min, sum, list, sorted, len
4.count, index, extend, sort, reverse, copy, clear...

元组:
(元素1, 元素2,...)
不可变(不支持增删改)，有序(支持下标操作)
查  - 和列表一样

1.单个元素的元组：(元素,)
2.元组变量 = 元素1,元素2,元素3,...
3.变量名1, 变量名2, ... = 元组
4.*变量名1, 变量名2, ... = 元组
"""
list1 = [1, 2, 3, 4]
list2 = list1[:]
list3 = list1.copy()
list4 = list1+[]
list5 = list1*1

