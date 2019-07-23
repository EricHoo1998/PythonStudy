'列表操作'
# 定义空列表
lt = []

# 新增5个元素
lt += [1,2,3,4,5]

# 修改lt中第二个元素
lt [2] = 6

# 向lt中第二个位置添加一个元素
lt.insert(2,7)

# 删除lt中第一个位置的元素
del lt[1]

# 删除lt中 1-3位置元素 （从零开始）
del lt[1:4]

# 判断lt中是否包含数字0
0 in lt

# 向lt新增数字0
lt.append(0)

# 返回数字0所在lt中的索引
lt.index(0)

# lt的长度
len(lt)

# lt中最大元素
max(lt)

# 清空lt
lt.clear()