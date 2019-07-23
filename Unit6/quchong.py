#去重方法

ls = ["P","P","Y",123,"S","s","z","z"]
s = set(ls) #利用集合无重复元素的特点
lt = list(s) #将集合转换为列表
print(lt)