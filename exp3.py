def delta(Q,i):
    if (Q=="B")&(i=='a'):
        return 'TB'
    elif (Q=='B')&(i=='b'):
        return 'S'
    elif (Q=='S')&(i=='a'):
        return 'B'
    elif (Q=='TB')&(i=='a'):
        return 'TB'
    elif (Q == 'TB') & (i == 'b'):
        return 'S'
    else:
        return 0

# 以a开头和结尾，两个b不能连续出现的均可识别
def DFAutom(x):
    sigma=['a','b']
    Q=['S','B','TB']
    q='S'
    F=['TB']
    for i in range(len(x)):
        q=delta(q,x[i])
        print(q)
        if q==0:
            print('不能识别')
            return 0
    for s in F:
        if q==s:
            print('可以识别')
            return 1
    print("不能识别")
    return 0

if __name__=="__main__":
    x='aababaaababaaa'
    DFAutom(x)
    x='ababaababaaba'
    DFAutom(x)



