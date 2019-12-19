"""__author:吴佩隆"""
import turtle

turtle.setup(400,600)
turtle.width(2)
turtle.speed(2)

turtle.up()
turtle.goto(0,-260)

turtle.left(150)
turtle.down()
for x in range(30):
    turtle.forward(1)
    turtle.right(2)

turtle.forward(20)

turtle.right(10)

for x in range(100):
    turtle.forward(3)
    turtle.left(0.3)

for x in range(130):
    turtle.forward(3)
    turtle.right(1.5)

turtle.up()
turtle.goto(160,150)
turtle.down()

for x in range(100):
    turtle.forward(3)
    turtle.right(0.3)

turtle.right(170)

for x in range(50):
    turtle.forward(3)
    turtle.left(0.3)

turtle.left(160)

for x in range(80):
    turtle.forward(3)
    turtle.left(0.4)

turtle.right(175)

for x in range(80):
    turtle.forward(3)
    turtle.right(0.4)

turtle.right(5)

for x in range(10):
    turtle.forward(3)
    turtle.left(0.4)


for x in range(40):
    turtle.forward(2)
    turtle.left(2)

for x in range(40):
    turtle.forward(2)
    turtle.right(1)

turtle.left(170)

for x in range(50):
    turtle.forward(2)
    turtle.left(1.2)

turtle.right(160)

for x in range(60):
    turtle.forward(2)
    turtle.right(1.2)

turtle.left(148)

for x in range(60):
    turtle.forward(3)
    turtle.left(0.3)

turtle.up()
turtle.sety(50)
turtle.setx(-10)
turtle.down()

turtle.left(15)

for x in range(30):
    turtle.forward(2)
    turtle.right(0.2)

turtle.left(45)

for x in range(25):
    turtle.forward(2)
    turtle.left(1)

for x in range(25):
    turtle.forward(2)
    turtle.left(1.5)

turtle.up()
turtle.sety(50)
turtle.setx(-10)
turtle.down()

turtle.width(5)

turtle.left(10)

for x in range(18):
    turtle.forward(2)
    turtle.right(4)

turtle.up()
turtle.goto(75,75)

turtle.left(90)
turtle.down()

turtle.fillcolor('black')
turtle.begin_fill()
for x in range(37):
    turtle.forward(2)
    turtle.right(6)

for x in range(10):
    turtle.forward(2)
    turtle.right(8)

for x in range(5):
    turtle.forward(2)
    turtle.right(8)

for x in range(11):
    turtle.forward(2)
    turtle.right(4)

turtle.end_fill()
turtle.goto(100,75)

turtle.pencolor('white')
turtle.circle(3)

turtle.up()
turtle.pencolor('black')
turtle.width(3)
turtle.goto(50,0)
turtle.down()
for x in range(5):
    turtle.forward(2)
    turtle.right(2)

turtle.width(2)
turtle.up()
turtle.goto(15,10)
turtle.down()
turtle.left(70)
turtle.pencolor('red')
turtle.forward(10)
turtle.up()
turtle.goto(19,10)
turtle.down()
turtle.forward(5)
turtle.up()
turtle.goto(22,12)
turtle.down()
turtle.forward(8)

turtle.up()
turtle.goto(90,25)
turtle.down()
turtle.forward(8)
turtle.up()
turtle.goto(93,22)
turtle.down()
turtle.forward(4)
turtle.up()
turtle.goto(96,27)
turtle.down()
turtle.forward(6)

turtle.up()
turtle.goto(60,-20)
turtle.down()
turtle.pencolor('black')
turtle.width(4)
turtle.bk(100)
turtle.left(20)
turtle.bk(100)
turtle.fd(100)
turtle.right(20)
turtle.fd(50)
turtle.left(70)
turtle.fd(120)
turtle.bk(120)
turtle.right(20)
turtle.bk(80)
turtle.fd(80)
turtle.right(50)
turtle.bk(50)
turtle.left(90)
turtle.fd(100)

turtle.mainloop()