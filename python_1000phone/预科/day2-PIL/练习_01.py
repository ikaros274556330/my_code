"""__author:吴佩隆"""
from PIL import Image

image = Image.open('files/海贼王/anchor.png').convert('RGBA')
bgImage = Image.new('RGB',(272,292),(255,255,0))


new1 = image.transpose(Image.FLIP_LEFT_RIGHT)
new2 = image.transpose(Image.FLIP_TOP_BOTTOM)
new3 = new1.transpose(Image.FLIP_TOP_BOTTOM)

bgImage.paste(image,(0,0),image)
bgImage.paste(new1,(0,146),new1)
bgImage.paste(new2,(136,0),new2)
bgImage.paste(new3,(136,146),new3)


bgImage.show()



