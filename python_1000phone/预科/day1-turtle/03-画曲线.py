"""__author:吴佩隆"""
import turtle

# 1.创建画布
turtle.setup(800,600)

# 2.画曲线
for x in range(90):
    turtle.fd(2)
    turtle.left(2)

for x in range(90):
    turtle.fd(2)
    turtle.right(2)

for x in range(180):
    turtle.fd(4)
    turtle.right(2)



turtle.mainloop()