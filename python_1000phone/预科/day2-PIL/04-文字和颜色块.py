"""__author:吴佩隆"""
from PIL import Image,ImageFont,ImageDraw

# 1.文字水印 - 将文字渲染在图片上
# 准备图片

image1 = Image.open('./files/chiling.jpg')

# 准备文字
# 1)创建字体对象
# ImageFont.truetype(字体文件的路径,字体大小)
font1 = ImageFont.truetype('files/bb.ttf',80)

# 2)创建draw对象
# draw = ImageDraw.Draw(image1)
draw = ImageDraw.Draw(image1)

# 3)写
# draw.text(文字坐标,内容,(颜色),字体对象)
draw.text((0,0),'Hello Word!',(0,0,0),font1)
image1.show()

# 2.颜色块
image2 = Image.new('RGB',(200,50),(255,255,255))

# 1)创建draw对象
draw2 = ImageDraw.Draw(image2)
# 2)将图片上指定坐标设置为指定颜色
# draw2.point(坐标,颜色)
draw2.point((0,0),(255,0,0))

image2.show()



