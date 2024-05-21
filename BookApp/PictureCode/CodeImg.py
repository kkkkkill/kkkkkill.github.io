from random import randint, choice
from PIL import Image, ImageDraw, ImageFont
import io, os


# 制作随机验证码：数字，大小写字母
def get_random_code():
    # 随机数字
    number = str(randint(0, 9))
    # 随机大写字母
    upper = chr(randint(65, 90))
    # 随机小写字母
    lower = chr(randint(97, 122))
    # 再大小写字母和数字中再随机获取一个
    code = choice([number, upper, lower])
    return code


# 获取随机颜色
def get_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


# 制作图片
def create_img():
    # 创建图片对象
    img = Image.new(mode='RGB', size=(90, 30), color=get_color())
    # 创建画笔工具
    draw = ImageDraw.Draw(img)
    # 制作图片噪点
    # 噪点

    for i in range(40):
        # point([xy:图片的坐标]，fill颜色)
        x0 = randint(0, 90)
        y0 = randint(0, 30)
        draw.point([x0,y0], fill=get_color())
    # 噪线
    for i in range(6):
        # line([xy:图片的坐标]，fill颜色)
        draw.line([randint(0, 90),randint(0, 30),randint(0, 90),randint(0, 30)], fill=get_color())
    # 圆，弧线
    for i in range(4):
        x0 = randint(0, 90)
        y0 = randint(0, 30)
        x1 = randint(x0, 90)
        y1 = randint(y0, 30)
        draw.arc([x0,y0,x1,y1],0,90,fill=get_color())
    # 设置字体，导入字体文件设置字体大小
    dir = os.path.join(os.path.dirname(__file__), 'fonts', 'Arial.ttf')
    font = ImageFont.truetype(dir, 24)
    #拼接生成的验证码
    text = ''
    # 生成验证码
    for i in range(4):
        c = get_random_code()
        # 将获取到的验证码字符写入到图片中
        draw.text((10 + 20 * i, 2), text=c, fill=get_color(), font=font)
        text += c
    #将图片保存到内存中
    out = io.BytesIO()
    # 保存验证码的图片
    img.save(out, format='png')
    return out.getvalue(), text


if __name__ == '__main__':
    code = get_random_code()
    color = get_color()
    print(code, color)
    create_img()
