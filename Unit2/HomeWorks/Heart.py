from turtle import *
import time


def setTurtle():
    # 窗口大小
    screensize(900, 700, 'white')
    # 颜色
   # color('red', 'pink')
    # 笔粗细
    pensize(3)
    # 速度
    speed(8)
    # 提笔
    penup()


def getStart(h):
    # 去到的坐标,窗口中心为0,0
    goto(0, -180)
    r = h / 5
    drawBigL(r, h)
    drawBigArc(r, 140)
    drawBigArc(r, 70)
    drawBigR(r, h)
    centerRange()
    done()


def drawBigL(r, h):
    colors = ['red', 'red', 'red', 'red', 'red', 'red']
    for i in range(int(240 / h) + 1):
        seth(0)
        color(colors[i], colors[i + 1])
        drawHeart(r)
        seth(140)
        fd(h)


def drawBigArc(r, rad):
    colors = ['red', 'red', 'red', 'red', 'red', 'red']
    for i in range(50):
        if (i % 10 == 0):
            color(colors[int(i / 10)], colors[int(i / 10) + 1])
            seth(0)
            drawHeart(r)
            seth(rad - (i + 1) * 4)
        rt(4)
        fd(10.5)


def drawBigR(r, h):
    colors = ['red', 'red', 'red', 'red', 'red', 'red']
    for i in range(int(240 / h) + 1):
        color(colors[i], colors[i + 1])
        seth(0)
        drawHeart(r)
        setheading(220)
        fd(h)


def drawHeart(r):
    down()
    begin_fill()
    factor = 180
    seth(45)
    circle(-r, factor)
    fd(2 * r)
    right(90)
    fd(2 * r)
    circle(-r, factor)
    end_fill()
    up()


# 在心中写字
def centerRange():
    for i in range(6):
        drawCenter(i)
        time.sleep(1)


def drawCenter(i):
    goto(0, 0)
    colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']
    pencolor(colors[i])
    write('Love', font=('gungsuh', 50,), align="center")
    up()


setTurtle()
getStart(80)



