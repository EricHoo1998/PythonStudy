#字符反转

def rvs(s):
    if s =="":
        return s
    else:
        return rvs(s[1:])+s[0]