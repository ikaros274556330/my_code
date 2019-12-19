"""__author__=吴佩隆"""
# json模块是python提供专门用来支持json数据
import json

# 1.什么是json
"""
json是一种数据格式:一个json只有一个数据;唯一的这个数据必须是json支持的数据类型的数据

json支持的数据类型:
a.数字类型(number) - 包含所有的数字,并且支持科学记数法;数字直接写

b.字符串(string) - 文本数据，只能使用双引号引起来
                  支持转义字符

c.布尔(boolean) - 只有true和false两个值

d.空值 - null
e.数组(array) - [元素1,元素2,元素3,...]  这儿的元素可以为json支持的所有数据
f.字典(dictionary) - {key1:value1,key2:value2,key3:value3.....} key必须是字符串
"""

# 2.json转python
"""
1)转换规律
json            python
数字             int/float
字符串           字符串;双引号可能会变单引号
布尔             布尔;true -> True;false -> False
null            None
数组             列表
字典             字典

json.load(字符串) - 将json格式的字符串转换成python对应的数据
                    注意:要求这个字符串的内容必须是json格式的数据
"""
result = json.loads('"abc"')
print(result)

result = json.loads('[12,"abc",true,null]')
print(result)

print('==========================================')

# 3.python转json
"""
1)转换规律
python             json
int/float           数字
字符串               字符串;单引号变双引号
布尔值               布尔值;True -> true;False -> false
None                null
列表/元组             数组
字典                 字典

2) 方法
json.dumps(数据)  -  将python数据转成json格式的字符串
"""
result = json.dumps(100)
print(result)                                   # 100

result = json.dumps('abc')
print(result)                                   # "abc"

result = json.dumps([True, None, 'hello', 123])
print(result)                                   # [true, null, "hello", 123]

result = json.dumps((10, 'avc', False))
print(result)                                   # [10, "avc", false]

result = json.dumps({10: 100, 'name': '123'})
print(result)                                   # {"10": 100, "name":"123"}

