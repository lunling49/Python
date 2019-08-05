from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random


# 打开一个JPG图像
# im = Image.open(r'C:\Users\china\Pictures\2018-01-10\008.jpg')
# # 获得图像尺寸
# w, h = im.size
# print('image size: %sx%s' % (w, h))
# # 缩放到50%
# im.thumbnail((w//2, h//2))
# print('resize image to: %sx%s' % (w//2, h//2))
# # 把缩放后的图像用jpeg保存
# im.save('thumbnail.jpg', 'jpeg')

# 模糊
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('mohu.jpg', 'jpeg')


# 生成验证码图片
# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建font对象
font = ImageFont.truetype('arial.ttf', 36)
# 创建draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字
for t in range(4):
    draw.text((60*t+10, 10), rndChar(), font=font, fill=rndColor2())
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
image.show()





