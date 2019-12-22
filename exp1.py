import numpy as np
import prettytable as pt
import matplotlib.pyplot as plt

# 感知机算法
def perceptron(w,x,p):

    count = 0
    k = 0
    N = 0
    wk = 1
    tb = pt.PrettyTable()
    tb.field_names=['训练样本','dot(wk,x)','修正式','修正后的权值','迭代次数']

    while ((N<len(x))):
        count=count+1
        r=np.dot(w, x[k])
        if r >0:
            N=N+1
            tb.add_row(['x{_k},{_xk}'.format(_k=k, _xk=x[k]), "+", 'w{num}'.format(num=wk),w,count])
        elif r==0:
            w=w+p*x[k]
            wk+=1
            N=0
            sgn='0'
            tb.add_row(['x{_k},{_xk}'.format(_k=k, _xk=x[k]), "0", 'w{num}+x{k1}'.format(num=wk,k1=k), w, count])
        else:
            w = w + p*x[k]
            wk+=1
            N = 0
            sgn = '-'
            tb.add_row(['x{_k},{_xk}'.format(_k=k, _xk=x[k]), "-", 'w{num}+x{k1}'.format(num=wk,k1=k), w, count])
        k=(k+1)%len(x)
    # 打印表格和W
    print(tb)
    print('w =', w)
    plt.figure()
    # 画散点图和分界面图
    for i in range(len(x)):
        if x[i,2]>0:
            plt.scatter(x[i, 0], x[i, 1], color='red',s=75)
        else:
            plt.scatter(x[i, 0]*(-1), x[i, 1]*(-1), color='blue')
    x1=np.linspace(0,2,50)
    y=-1/w[1]*(w[0]*x1+w[2])
    # y = -1 / -1 * (1.5 * x1 -0.5)
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    plt.plot(x1,y)
    plt.show()

if __name__=='__main__':
    # 取不同的W和X顺序：
    w=np.array([0,0,0])
    x=np.array([[1,0,1],[1,1,1],[0,2,1],[-2,-1,-1],[-2,-2,-1],[-1,-3,-1]])
    p=1
    perceptron(w,x,p)

    w=np.array([1,1,1])
    x=np.array([[-2,-1,-1],[1,1,1],[1,0,1],[0,2,1],[-2,-2,-1],[-1,-3,-1]])
    p=1
    perceptron(w,x,p)

    w=np.array([-1,-1,1])
    x=np.array([[-2,-2,-1],[-1,-3,-1],[0,2,1],[1,0,1],[-2,-1,-1],[1,1,1]])
    p=1
    perceptron(w,x,p)

    w=np.array([0,0,0])
    x=np.array([[1,0,1],[1,1,1],[0,-1,-1],[-1,0,-1]])
    p=1
    perceptron(w,x,p)