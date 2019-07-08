'''

turtle正方形绘制
 ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬

描述
使用turtle库，绘制一个正方形。

'''
#RectDraw.py
import turtle as t
t.pensize(2)
for i in range(4):
    t.fd(150)
    t.left(90)
t.done()