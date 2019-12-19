"""__author:吴佩隆"""
from PIL import Image,ImageFilter,ImageFont,ImageDraw
from random import randint
# 1.画颜色块
def draw_color_block(color,size,xy,image=None):
    # 1)根据图片对象创建draw对象
    w, h = size
    x, y = xy
    if image:
        draw = ImageDraw.Draw(image)
    else:
        image = Image.new('RGB',(w+x,h+y),(255,255,255))
        draw = ImageDraw.Draw(image)

    # 2）画颜色块
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            draw.point((x1,y1),color)

    # 3)处理图片
    image.show()


# 2.马赛克
def draw_mosaic(xy,size,image=None,width=2,text=''):
    x,y = xy
    w,h = size
    if image:
        draw = ImageDraw.Draw(image)
    else:
        Image.new('RGB',(w+x,h+y),(255,255,255))
        draw = ImageDraw.Draw(image)

    for x1 in range(x,x+w,width):
        for y1 in range(y,y+h,width):
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            for x2 in range(width):
                for y2 in range(width):
                    draw.point((x1+x2,y1+y2),(r,g,b))
    # 在马赛克上添加文字
    font = ImageFont.truetype('files/bb.ttf', 80)
    draw = ImageDraw.Draw(image)
    draw.text((x,y),text, (255, 255, 255), font)


    image.show()

image1 = Image.open('files/chiling.jpg')


# draw_color_block((255,255,0),(100,100),(0,0),image1)
draw_mosaic((100,200),(400,200),image1,10,'hello world')