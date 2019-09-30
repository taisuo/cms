from PIL import Image,ImageFilter,ImageDraw,ImageFont
from datetime import datetime
import random,string
im=Image.open('1.jpg')
# str="123456"
str=("".join(random.sample(string.ascii_letters+string.digits,4)))
font=ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# im2=Image.open('2.gif')
fColor=(random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
#先创建绘制的工具#新建绘图对象图片
draw=ImageDraw.Draw(im)
#写文字，画文字
draw.text((0,0),str,font=font,fill=fColor)
# im.paste(im2,(0,0),None)
im.show()










# print(im.size)   #元祖
# w=im.size[0]
# h=im.size[1]
# print(w,h)
# 缩放到50%:
# im.thumbnail((w//2, h//2))
# 应用模糊滤镜:
# im2 = im.filter(ImageFilter.BLUR)
# #显示
# im.show()
# imgName="head"+str(int(datetime.now().timestamp()))
# print(imgName)
# im.save(imgName+".png","png")
# im.show()