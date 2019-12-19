"""__author:吴佩隆"""
# 导入PIL中图片处理相关库
from PIL import Image,ImageFilter,ImageDraw

# 1.加载图片-选择你想处理的图片
# Image.open(图片路径)-返回图片对象
# 路径-绝对路径（文件在电脑上的完整路径）
# 路径-相对路径（./（当前代码文件所在目录）../(当前代码文件所在的上层目录)当前文件到文件的路径）
image1 = Image.open('./files/chiling.jpg')
# image1.show()

# 2.使用滤镜
# 1）PIL自带滤镜效果
# 图片对象.filter(滤镜效果)-返回滤镜后的图片对象
"""
ImageFilter.EMBOSS - 浮雕效果
ImageFilter.FIND_EDGES - 泼墨效果
ImageFilter.SHARPEN - 锐化滤波
ImageFilter.SMOOTH - 平滑滤波
ImageFilter.EDGE_ENHANCE_MORE - 边界增强滤波（程度更深）
ImageFilter.EDGE_ENHANCE - 边界增强滤波
ImageFilter.DETAIL - 细节滤波
ImageFilter.CONTOUR - 轮廓滤波（铅笔画）
ImageFilter.BLUR - 模糊滤波

"""

# f_image1 = image1.filter(ImageFilter.FIND_EDGES)
# f_image1.show()

# 2）写自己的滤镜效果
"""
class 滤镜名(ImageFilter.BuiltinFilter):
    name = '滤镜首字母大写'
    filterargs = (num1,num2),num3,num4,
    (3X3/5X5 的矩阵)
"""
class WPL1(ImageFilter.BuiltinFilter):
    name = 'Wpl1'
    filterargs = (3, 3), 13, 0, (
        2, 2, 2,
        2, 2, 2,
        2, 2, 2,
    )

a = image1.filter(WPL1)
a.show()


