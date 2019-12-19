"""__author__=吴佩隆"""

"""
列表
1.+,*,
2.in , not in
3.max,min,sum,list,sorted,len
4.count(),index(),sort(),reverse(),extend(),clear(),copy()

元组
不可变(不支持增删改)，有序(支持下标操作)
查 - 和列表一样

1.单个元素的元组(元素,)
2.元素变量 = 元素1,元素2,...
3.变量1,变量2,... = 元组
4.*变量1,变量2,...= 元组
"""

# 复制列表的操作(浅拷贝)
list1 = [1, 2, 3, 4]
list2 = list1[:]
list3 = list1.copy()
list4 = list1 + []
list5 = list1 * 1
