1. 为函数写一个装饰器，在函数执行之后输出 after

2. 为函数写一个装饰器，把函数的返回值 +100 然后再返回。

3. 写一个装饰器@tag要求满足如下功能:

```python
@tag
def render(text):
    # 执行其他操作
    return text

@tag
def render2():
    return 'abc'

print(render('Hello'))   # 打印出: <p>Hello</p>
print(render2())     # 打印出: <p>abc</p>
```



4. 写一个装饰器@tag要求满足如下功能(需要使用带参的装饰器，自己先自学正在一下):

```python
@tag(name='p')
def render(text):
    # 执行其他操作
    return text

@tag(name='div')
def render2():
    return 'abc'

print(render('Hello'))   # 打印出: <p>Hello</p>
print(render2())     # 打印出: <div>abc</div>
```



5. 为函数写一个装饰器，根据参数不同做不同操作。
   flag为True，则 让原函数执行后返回值加100，并返回。
   flag为False，则 让原函数执行后返回值减100，并返回。

