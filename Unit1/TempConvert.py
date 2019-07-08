#TempConvert.py

'''
评估函数eval() 执行一个字符串表达式，并返回表达式的值
语法
以下是 eval() 方法的语法:

eval(expression[, globals[, locals]])

参数
expression -- 表达式。
globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

返回值
返回表达式计算结果。

实例：
>>> eval("1")
1
>>> eval("1+2")
3
>>> eval('"1+2"')
'1+2'
>>> eval('print("Hello")')
Hello



注意：
(1) 将输入字符串转换为数字时使用eval()函数，不要用int()函数，因为输入的数字可能不是整数；

(2) 采用{:.2f}将输出数字变成两位小数点表示时，即使数学上该输出值是整数，也会按照小数方式输出，例如，转换后温度为10度，输出为10.00。

'''

TempStr= input("请输入带符号的温度值")  #从控制台输入信息

if TempStr[-1] in ['F','f']:   # in 判断一个元素是否在列表中
    C = (eval(TempStr[:-1])-32)/1.8
    print("转换后的温度时：{:.2f}°C".format(C)) #以字符形式向控制台输出结果的函数


elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[:-1])+32
    print("转换后的温度时：{:.2f}°F".format(F))


else:
    print("输入格式错误！")


