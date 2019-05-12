from turtle import *
# turtle包本身只是一个绘图库，但是配合Python代码，就可以绘制各种复杂的图形
"""
设置画布大小
screensize(canvwidth=None,canvheight=None,bg=None),参数分别为画布的宽（单位像素）、高、背景颜色
如:screensize(800,600,'green')
   screensize()--返回默认大小（400，300）
   
setup(width=0.5,height=0.75,startx=None,starty=None)
width,height:输入宽和高为整数时，表示像素；为小数时，表示占据电脑屏幕的比例
startx,starty:这一坐标表示矩形窗口左上角顶点的位置，如果为空，则窗口位于屏幕中心
如:setup(width=0.6,height=0.6)
   setup(width=800,height=800,startx=100,starty=100)
   
画笔
pensize() / width() --设置画笔的宽度
pencolor()--没有参数传入，返回当前画笔颜色；传入参数设置画笔颜色，可以是字符串如'red','green'，也可以是RGB 3元组
speed()--设置画笔移动速度，画笔绘制的速度范围[0,10]整数，0表示最快，数字1-10越大越快
    内置的速度字符串：'fastest':0
                    'fast':10
                    'normal':6
                    'slow':3
                    'slowest':1

绘图命令：1、运动命令     2、画笔控制命令    3、全局控制命令
画笔运动命令
forward(distance) / fd(distance) --向当前画笔方向移动distance像素长度
backward(distance) / bk(distance) /back(distance) --向当前画笔相反方向移动distance像素长度
right(degree) / rt(degree) --顺时针移动degree度
left(degree) / lt(degree) --逆时针移动degree度
pendown() / pd() / down() -- 移动时绘制图形，缺省时也绘制
goto(x,y) / setpos(x,y) / setposition(x,y) --将画笔移动到坐标为x，y的位置
penup() / pu() / up() --提起笔移动，不绘制图形，用于另起一个地方绘制
circle(r,extent=None,steps=None) --画圆
    r--圆半径，为正数则逆时针画圆，为负数则顺时针画圆
    extent--一个角度，决定哪部分圆圈被绘制，不提供extent表示画完整的圆
    steps--指定半径r前提下，完成extent的角度时，分了几步，如画正5边形时circle(40,None,5)
setx() --将当前x轴移动到指定位置
sety() --将当前y轴移动到指定位置
setheading(angle) / seth(angle) --设置当前朝向为angle角度
home() --设置当前画笔位置为原点，朝向东
dot(size=None,*color) --绘制一个指定直径和颜色的圆点

画笔控制命令
fillcolor(color) --绘制图形的填充颜色
color(color1,color2) --同时设置pencolor=color1，fillcolor=color2
filling() --返回当前是否在填充状态
begin_fill() --准备开始填充图形
end_fill() --填充完成
hideturtle() / ht() --隐藏画笔的turtle形状
showturtle() / st() --显示画笔的turtle形状

全局控制命令
clear() / clearscreen() --清屏且画笔形状也恢复默认，但是画笔的位置和状态不会改变
reset() / resetscreen() --清屏并将画笔位置和方向恢复到初始状态，保持画笔形状不变，即位置恢复到原点(0, 0)位置
undo() --撤销上一个turtle动作
isvisible() --返回turtle画笔当前是否可见
stamp() --复制当前图形,在当前位置拷贝一份此时箭头的形状,返回一个stamp_id(int型)
clearstamp(stamp_id) --用来删除指定stamp_id的箭头形状
turtle.clearstamps(n=None) --n为None时表示删除所有拷贝的箭头形状;为0不删除;n > 0 表示删除前n个,n < 0 表示删除后n个
write(arg,move=False,align='left',font=('font-name',font_size,'font_type')) --写文本
    arg--文本内容
    move--True/False，设置是否绘制
    align--left,center,right，设置文本下方初始位置
    font--字体的参数，分别为字体名称、大小和类型，font为可选项，font参数也是可选项
    
其他命令
mainloop() / done() --运行后屏幕自动消失,调用这句后屏幕会保持,直到主动关闭当前窗口
mode(mode=None) --设置乌龟模式（“standard”，“logo”或“world”）并执行重置。如果没有给出模式，则返回当前模式
    Mode         初始方向         角度方向
    standard     向右（东）       逆时针方向
    logo         向右（东）       逆时针方向
    world        向上（北）       顺时针方向
delay(delay=None) --设置或返回绘图延迟（单位：毫秒），绘图延迟越长，动画的速度越慢
    delay--正整数
begin_poly() --表示开始记录多边形第一个顶点
end_poly() --表示结束记录多边形顶点
get_poly() --表示获取最后记录的多边形
"""


# 绘制长方形
# width()--设置笔刷宽度，pencolor()--设置颜色
# width(4)        # 设置笔刷宽度
# forward(200)    # 前进
# right(90)       # 右转90度
# pencolor('red')     # 笔刷颜色
# forward(100)
# right(90)
# pencolor('green')
# forward(200)
# right(90)
# pencolor('blue')
# forward(100)
# right(90)
# done()  # 调用done()使得窗口等待被关闭，否则将立即关闭窗口

# 循环绘制5个五角星
# def draw_star(x, y):
#     pu()
#     goto(x, y)
#     pd()
#     # set heading: 0
#     seth(0)
#     for i in range(5):
#         fd(40)
#         rt(144)
#
# for x in range(0, 250, 50):
#     draw_star(x, 0)
# done()

# 绘制五角星
# ht()
# fd(200)
# x = 1
# begin_fill()
# while x <5:
#     rt(144)
#     fd(200)
#     x += 1
# end_fill()
# done()

# 一棵分型树
# colormode(255)      # 设置色彩模式是RGB
# lt(90)
# lv = 14
# l = 120
# s = 45
# width(lv)
# # 初始化RGB颜色
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)
# pendown()
# fd(l)
#
# def draw_tree(l, level):
#     global r, g, b
#     # save the turrent pen width
#     w = width()
#
#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color
#     r += 1
#     g += 2
#     b += 3
#     pencolor(r % 200, g % 200, b % 200)
#
#     l = 3.0 / 4.0 * l
#
#     lt(s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level +1)
#     bk(l)
#     rt(2 * s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level +1)
#     bk(l)
#     lt(s)
#
#     # restore the previous pen width
#     width(w)
#
# speed('fastest')
#
# draw_tree(l, 4)
# done()
