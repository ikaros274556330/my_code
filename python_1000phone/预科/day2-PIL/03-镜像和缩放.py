"""__author:吴佩隆"""
from PIL import Image

# 1.镜像
# 图片对象.transpose(镜像名) - 产生指定图片的镜像
image1 = Image.open('files/chiling.jpg')

# 左右镜像
# new1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
# new1.show()

# 上下镜像
# new2 = image1.transpose(Image.FLIP_TOP_BOTTOM)
# new2.show()

# 2.缩放
# 图片对象.thumbnail((宽度,高度)) - 将图片缩放到指定大小(等比缩放)

image2 = Image.open('files/tie.png')

# print(image2.size)

image2.thumbnail((50,50))
image2.show()
# print(image2.size)

# 练习：将一张图片，原图。左右，上下，左右上下拼成一张






