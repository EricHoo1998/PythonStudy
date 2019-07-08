'''

turtle叠边形绘制
 ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬

描述
使用turtle库，绘制一个叠边形，其中，叠边形内角为100度。

'''
#TwoRoundDraw.py
import turtle as t
t.pensize(2)
for i in range(9):
    t.fd(150)
    t.left(80)  #720/9
t.done()