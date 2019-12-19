"""__author:吴佩隆"""
from PIL import Image,ImageFilter,ImageDraw
# 1.图片剪切
# 加载图片
image1 = Image.open('files/chiling.jpg')
# image1.save('路径/文件名.jpg') - 保存图片

# 剪切图片
# 图片对象.crop(x1,y1,x2,y2) - 确定左上角和右下角的坐标

# new_1 = image1.crop((212,665,270,752))
# new_1.show()

# 2.粘贴
# 1）贴小图
# 图片对象1.paste(图片对象2,(x坐标,y坐标)) - 将图片对象2粘贴到图片对象1的指定位置

# image2 = Image.open('files/tie.png')
# image1.paste(image2,(0,0))
# image1.show()

# 2）拼图
# 创建空白图片：Image.new(图片模式，图片大小，图片背景颜色)
bgImage = Image.new('RGB',(300,145),(255,255,0))

# 贴图
small1 = Image.open('files/海贼王/anchor.png')
small2 = Image.open('files/海贼王/bear.png')
bgImage.paste(small1,(0,0))
bgImage.paste(small2,(136,0))

bgImage.show()