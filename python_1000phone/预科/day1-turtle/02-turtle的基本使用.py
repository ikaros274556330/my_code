"""__author:吴佩隆"""
import turtle

# 1.创建画布（准备纸和笔）
turtle.setup(800,600)

# 2.准备笔（默认就有，使用前设置，不设置为黑，粗细为1）
# 1）设置笔的颜色
# 颜色值-颜色对应的英文单词引号括起来/'#6位的16进制数'
# 计算机三原色：红(255,0,0)，绿(0,255,0)，蓝(0,0,255) RGB值
# 0->00 255->ff
# 红ff0000 绿00ff00 蓝0000ff
turtle.pencolor('red')

# 2)设置笔的粗细
turtle.width(2)

# 3)设置笔的速度(1-10(值越大速度越快),0(看不到移动轨迹))
turtle.speed(1)

# 3.控制笔移动
# 1)控制笔向前移动
# turle.forward()/turtle.fd()
# turtle.forward(100)

turtle.begin_fill()

turtle.fd(100)

# 2)控制笔后退
# turtle.back()/turtle.bk()
turtle.pencolor('green')    #画下一条线的时候换颜色
turtle.bk(200)

# 3)控制笔直线移动到指定位置
# turtle.goto(x坐标,y坐标)
# turtle.setx(x坐标)/turtle.sety(y坐标) - 从当前坐标只移动x/y值
turtle.pencolor('blue')
turtle.goto(50,50)

turtle.pencolor('pink')
turtle.setx(-100)
turtle.pencolor('purple')
turtle.sety(100)

turtle.end_fill()

# turtle.home() - 控制笔回到原点
turtle.home()

# 4.控制笔的方向(笔的方向默认朝右)
# turtle.left(角度)/turtle.right(角度) - 当前方向向左/向右转多少度
turtle.left(90)

turtle.right(90)

# 5.抬笔和下笔(笔默认放下)
# 抬起
turtle.up()
turtle.speed(0)
turtle.goto(0,-200)

# 放下
turtle.down()
turtle.speed(1)
turtle.fd(100)

# 6.画圆
# turtle.circle(半径) - 圆环
# turtle.circle(半径,角度) - 指定圆弧
turtle.pencolor('orange')
turtle.circle(20)

turtle.pencolor('red')
turtle.circle(30,270)

turtle.right(90)
turtle.circle(40,90)

# turtle.dot(直径) - 实心圆
turtle.pencolor('yellow')
turtle.dot(60)

turtle.pencolor('black')

# 7.填充
# 1)设置填充颜色
turtle.fillcolor('green')

turtle.up()
turtle.goto(-200,200)
turtle.down()
# 开始填充
turtle.begin_fill()
turtle.fd(100)
turtle.left(90)
turtle.fd(100)
turtle.left(90)
turtle.fd(100)
turtle.left(90)
turtle.fd(100)
# 结束填充
turtle.end_fill()







#让程序可以一直运行
turtle.mainloop()