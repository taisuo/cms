# from PIL import Image
# im = Image.open('./wxgzh.jpg')
# w, h = im.size
# print(w, h)
# im.thumbnail((w//2, h//2))
# print(w//2, h//2)
# print('%sx%s' % (w//2, h//2))
# im.save('thumbnail.jpg', 'jpeg')

# from PIL import Image, ImageFilter
# im = Image.open('./wxgzh.jpg')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg', 'jpeg')
# import os
# os.getcwd
# print(os.path.abspath("./"))
#
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
def rndChar():
    return chr(random.randint(65, 90))
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(2):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
# im = Image.open('./wxgzh.jpg')
# region  = Image.open('./code.jpg')
# im.paste(region,(50,0),None)
# im.show()
# box = (50,50,200,200)
# region = im.crop(box)
# # region.show()
#
# im_rotate_180 = im.transpose(Image.FLIP_LEFT_RIGHT)
# im_rotate_180.show()
