"""__author:吴佩隆"""
from PIL import Image

image = Image.open('files/chiling.jpg')
image1 = Image.open('files/tie.png').convert('RGBA')

image.paste(image1,(0,0),image1)
image.show()



