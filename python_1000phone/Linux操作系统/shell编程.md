# shell编程

Shell脚本，是一种为shell编写的脚本程序。

Shell编程跟JavaScript、Python编程一样，只要有一个能编写代码的文本编辑器和一个能解释执行的脚本解释器就可以了。

Linux的Shell种类有很多，我们主要用的是Bourne Shell(/usr.bin/sh或/bin/sh)



##### 1.创建shell文件

原则上shell程序可以写在任何文件中，但是一般会在shell文件后加后缀.sh表示当前文件是一个shell文件

shell需要可执行权限，所以创建好的shell文件需要添加x权限



##### 2.基础语法

###### 1）注释

```shell
# 单行注释
:<<EOF
多行注释1
多行注释2
多行注释3
EOF
```

###### 2）输出和输入

echo指令就相当于python中的print函数(默认会换行)

```shell
echo  输出内容  
echo -n 输出内容     # 输出的时候不换行
```



printf指令（输出不能换行）

```
printf 输出内容
```



输入指令:  read 变量名    -- 输入内容，并且将输入的结果保存在变量中



###### 3）变量

a. 声明变量的语法:   变量名=值

说明:  a. 变量名和=, =和值之间不能有空格

​	   b. 变量名的要求和python变量名要求一样

```shell
name='小明'
age=18
stu_name=小红
```



b. 使用变量: 

​		 $变量

​		 ${变量}

```shell
age=18
echo $age
age2=${age}
```

c. 只读变量

使用 readonly 命令可以将变量定义为只读变量，只读变量的值不能被改变。

```shell
gender='男'
readonly gender
gender='女'     # test.sh: line 17: gender: readonly variable
```

d. 删除变量

使用 unset 命令可以删除变量

```shell
name='yuting'
unset name
```



###### 4）获取linux指令结果

在shell脚本中可以直接写linux指令，在执行shell脚本的时候这些指令可以直接获取

```shell
ls     # ls指令
ls  -lh      # ls指令，并且设置参数
touch a.txt    # 创建a.txt文件

# 获取指令结果: 变量=$(指令)  /   变量=`指令`
lsresult=$(ls)    #将ls指令的结果保存到变量lsresult中
currnet_path=`pwd`
```



##### 3.shell字符串

shell中的字符串可以用单引号也可以使用双引号甚至可以不用引号。但是单引号中不能出现单引号字符，加\也不行

```shell
str1='abc'
str2="abc"
str3=abc
str4='abc\n123'		#支持转义字符,但是不支持编码字符
str5="abc\n123"

age=18
str6="年龄是$age"    #双引号里面可以出现变量,单引号不行
```

###### 1）字符串拼接

```shell
str1="hello"

#单引号拼接
str2=''${str1}',world!'
str3=''$str1',world!'

#双引号拼接
str4="${str1},world!"
str5=""$str1",world!"

```

###### 2）获取字符串长度

```shell
str1="abcd"
echo ${#str1}    # 输出4
```

###### 3）字符串提取

```shell
# 字符串:下标:个数   --从字符串中指定下标开始获取指定个数字符,返回一个新的字符串
# 字符串:下标:1   -- 获取字符串中指定下标对应的字符
# 字符串:下标     -- 从指定下标开始获取到字符串最后

string='hello world'
echo ${string:1:4}    # ello
```



##### 4.shell数组

在 Shell 中，用括号来表示数组，数组元素用"空格"符号分割开。定义数组的一般形式为：

```shell
# 数组名=(元素1 元素2 元素3 ...)
names=(小明 小红 大黄 Tom)
names2=(
'小明'
'小红'
'大黄'
'Tom'
)
names3[0]=小明
names3[1]=小红
names3[2]=大黄
names3[3]=Tom

```

###### 1）获取数组元素：${数组[下标]}

```shell
echo ${names[1]}    # 小红
```

###### 2）获取数组的长度

```shell
nums=(100 200 300 400)
# 获取数组长度
length=${#nums[@]}
length=${#nums[*]}
# 获取数组指定下标对应的元素的长度
length2=${#num[n]}
```



##### 5.运算符

shell中支持的运算符有:  算术运算符、关系运算符、布尔运算符、字符串运算符

###### 1）算术运算符：+，-，*，/，%

```shell
# 如果想要在shell完成数值运算，运算的语法:  `expr 运算表达式`; 并且运算符两边必须加空格
re1=10+20
echo ${re1}    # 10+20

# 1.加法运算
re2=`expr 10 + 20`    
echo ${re2}    # 30

# 2.减法运算
re3=`expr 10 - 20`
echo ${re3}	   # -10

# 3.乘法运算
re4=`expr 10 \* 20`   # 注意:使用*作为乘法运算符的时候需要前面加\
echo ${re4} 	# 200

# 4.除法运算
# 小数除法运算: `echo "scale=小数点位数;数值1 / 数值2"|bc`
# 整数除法运算: `expr 数值1 / 数值2`
re5=`echo "scale=2;7 / 3"|bc`
echo $re5

re6=`expr 5 / 2`
echo $re6

# 5.求余数
re7=`expr 10 % 3`

re8=`echo "10.2 + 5.1"|bc`
echo $re8
```

###### 2） 关系运算符(比较运算符)，比较的是数字大小

```shell
# -eq  ---  等于,相当于 ==
# -ne  ---  不等于,相当于!=
# -gt  ---  大于
# -lt  ---  小于
# -ge  ---  大于等于
# -le  ---  小于等于
# 使用语法: [ 值1 关系运算符 值2 ]
a=100
b=10

# 关系运算符要配合if语句或者循环语句使用
if [ $a -gt $b ]
then
	echo a大于b
else 
	echo a不大于b
fi
```

###### 3）布尔运算符(逻辑运算符)

```shell
# !    --  逻辑非运算
# -o   --  逻辑或运算
# -a   --  逻辑与运算

age=18
score=95
# 参加比赛的条件：分数大于90分并且年龄大于等于18岁
if [ $age -ge 18 -a $score -gt 90 ]
then
	echo 可以参见比赛
else
	echo 不能参加比赛
fi
```

###### 4）字符串运算符

```shell
# [ 字符串1 = 字符串2 ]    -- 判断两个字符串是否相等
# [ 字符串1 != 字符串2 ]   -- 不相等
# [ -z 字符串]   -- 判断字符串长度是否为0
# [ -n "字符串" ]    -- 判断字符串长度是否不为0
# [ $ 字符串 ]   -- 判断字符串是否是空串

a="abc"
b="123"

if [ $a = $b ]
then
    echo a和b相等
else
    echo a和b不相等
fi

a=""
if [ -n "${a}" ]
then
    echo a的长度不为0
else
    echo a的长度为0
fi

```



##### 6. if语句

```shell
语法1：
if 条件语句
then
    满足条件执行的代码
fi

语法2:
if 条件语句
then
    满足条件执行的代码
else
    不满足条件执行的代码
fi


语法3：
if 条件语句1
then 
    代码块1
elif 条件语句2
then
    代码块2
elif 条件语句3
then 
    代码块3
else
    代码块N
fi
```



##### 7. for循环

```shell
语法:
for 变量 in 序列
do
    循环体
done

# 遍历字符串
for char in "hello word"
do
    echo 循环体char: ${char}
done

# 遍历数组
arr1=(10 20 "abc")
for x in ${arr1[@]}
do
    echo 循环体2x: ${x}
done

# 遍历多个值
for x in 10 20 "你好" 123
do
    echo 循环体3：${x}
done
```

##### 8. while循环

```shell
语法:
while 条件语句
do
    循环体
done

# 遍历字符串
str1="helloWorld!"
index=0
len=${#str1}
while [ $index -lt $len ]
do
    echo ${str1:${index}:1}
    index=`expr ${index} + 1`
done

# 计算1+2+3+...+100
num=1
sum=0
while [ ${num} -le 100 ]
do
    sum=`expr ${sum} + ${num}`
    num=`expr ${num} + 1`
done
echo 1+2+3+...+100 = ${sum}

# 死循环
while true
do
    read -p "请输入一个数字:" num
    if [ ${num} == 100 ]
    then
        break
    fi
done
```

##### 9.函数

###### 1）函数的声明和调用

```shell
# 1.函数的声明
声明的语法：
函数名(){
    函数体
}

调用函数语法:  函数名

#声明函数
func1(){
    echo 你好函数1
}
#调用函数
func1

# 2.有参数的函数
# 声明的时候不需要形参, 直接在函数体中通过'${N}'来获取第N个实参
# 调用的时候:  函数名 实参1 实参2 实参3 ...
func2(){
    echo 函数2被调用
    echo 第一个参数: ${1}
    echo 第二个参数: ${2}
    echo 第三个参数: ${3} 
}
func2 10 20 "abc"

# 3.函数的返回值
# return 数字   - 数字的范围是0~255
func3(){
    echo 函数3被调用
    return 256
    #a=`expr 100 + 200`
}

func3
echo ${?}
```











