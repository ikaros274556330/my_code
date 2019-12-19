"""__author__=余婷"""
import json

"""
1.文件操作
打开文件  ->   操作文件  -> 关闭文件
open(文件路径, 打开方式, 编码方式)
with open(文件路径, 打开方式, 编码方式) as 文件对象:
    文件域

read()/write()

close()

2.数据持久化

3.json数据
1)一个json有且只有一个数据； 2)这个唯一的数据是json支持的数据类型的数据

number   ->    19, 12.9, -12.8, 3e4
字符串    ->    "abc", "abc\n123", "\u4e00"
布尔      ->    true, false
null     ->    null
数组(Array)  ->  [23, 23, true, null, "abc"]
字典      ->   {"name": 12, "age": "abc"}

python转json
json.dumps(python数据)  -> 'json数据' 

json转python
json.loads('json数据')  -> python数据
"""



