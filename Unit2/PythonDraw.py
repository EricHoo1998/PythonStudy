#PythonDraw.py

# from turtle import *
# import turtle as  as_turt le

import turtle
turtle.setup(650,350,200,200) #(width,height,startx,starty) 后两个为可选 起始点X Y坐标
turtle.penup()
turtle.fd(-250) #前进 forward
turtle.pendown()
turtle.pensize(25)#画笔宽度
turtle.pencolor("purple")#颜色
turtle.seth(-40)#角度 setheading
for i in range(4):
    #循环4次
    # range()函数 产生循环计数序列
    # range(N) 产生0到N-1的整数序列 共N个
    # range(M,N) 产生M到N-1的整数序列 共N-M个
    turtle.circle(40,80)#(x半径,y弧度)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()