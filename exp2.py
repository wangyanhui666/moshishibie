import numpy as np
import matplotlib.pyplot as plt
import os

root=os.getcwd()

# 计算一个点到每一类的平均距离
def distance(point,kind,i,c):
    count=np.zeros(c)
    cache=np.square(point-point[i])
    for j in range(c):
        index1=np.argwhere(kind==j)
        a=index1.flatten()
        count[j]=np.mean(cache[a])
    return count


def refine(point,kind,c):
    while(1):
        flag=0
        for i in range(len(point)):
            dis=distance(point,kind,i,c)
            k=np.argmin(dis)
            if k==kind[i]:
                continue
            else:
                # print(k, type(k),kind[i])
                kind[i]=k
                flag=1
                break
        if flag==0:
            break
    print('refine finish!!!!!!!')
    plt.figure()
    color = ['c', 'b', 'g', 'r', 'm', 'y', 'k']
    # print(kind)
    for j in range(c):
        index1 = np.argwhere(kind == j)
        a1 = index1.flatten()
        # print(a1)
        plt.scatter(point[a1, 0], point[a1, 1], c=color[j])
    for j in range(1000):
        if os.path.exists(os.path.join(root,'{i}.jpg'.format(i=j))):
            continue
        plt.savefig(os.path.join(root,'{i}.jpg'.format(i=j)))
        print("save!", os.path.join(root,'{i}.jpg'.format(i=j)))
        break
    plt.pause(1)
    plt.close()
    return kind

def cmean(point,z,n):
    point=np.array(point)
    kind=np.zeros(len(point),dtype=int)
    cache=np.zeros(n)
    z=np.array(z)
    znew=np.zeros([n,2])
    count=np.zeros(n)
    while(1):
        print('z', z)
        znew = np.zeros([n, 2])
        count = np.zeros(n)
        for i in range(len(point)):
            for j in range(n):
                cache[j]=np.linalg.norm(point[i]-z[j])
            m=np.argmin(cache)
            kind[i]=m
            znew[m]=znew[m]+point[i]
            count[m]+=1

        for i in range(n):
            if count[i]!=0:
                znew[i]=znew[i]/count[i]
        # print('znew',znew)
        if(np.max(abs(znew-z))<1e-6):
            print("finish!!")
            plt.figure()
            color = ['c', 'b', 'g', 'r', 'm', 'y', 'k', ]
            # print(kind)
            for j in range(n):
                index1 = np.argwhere(kind == j)
                a1 = index1.flatten()
                # print(a1)
                plt.scatter(point[a1, 0], point[a1, 1], c=color[j])
            for j in range(1000):
                if os.path.exists(os.path.join(root,'{i}.jpg'.format(i=j))):
                    continue
                plt.savefig(os.path.join(root,'{i}.jpg'.format(i=j)))
                print(os.path.join(root,'{i}.jpg'.format(i=j)))
                break
            plt.pause(1)
            plt.close()
            return kind
        z=znew
        plt.figure()
        color = ['c', 'b', 'g', 'r', 'm', 'y', 'k']
        #print(kind)
        for j in range(n):
            index1 = np.argwhere(kind == j)
            a1 = index1.flatten()
            # print(a1)
            plt.scatter(point[a1, 0], point[a1, 1], c=color[j])
        plt.pause(0.5)
        plt.close()


def createrandm(k,N,d):
    randmk=d*(np.random.rand(k,2)-0.5)
    sum=np.sum(N)
    point=np.zeros([sum,2])
    m=0
    for i in range(k):
        print('i',i)
        print("k",k)
        point[m:m+N[i]]=np.random.multivariate_normal(randmk[i],[[0.5,0],[0,0.5]],N[i])
        m += N[i]

    plt.figure()
    plt.scatter(point[:, 0], point[:, 1], c='red')
    for j in range(1000):
        if os.path.exists(os.path.join(root,'{i}.jpg'.format(i=j))):
            continue
        plt.savefig(os.path.join(root,'{i}.jpg'.format(i=j)))
        print("save!",os.path.join(root,'{i}.jpg'.format(i=j)))
        break
    plt.pause(1)
    plt.close()
    return point


if __name__=='__main__':
    # 产生随机点
    print(root)
    point=createrandm(3, [20, 500, 20], 20)
    # cmean聚类(使用随机初始点)
    rand=np.random.randint(0,len(point),3)
    print(rand)
    kind1 = cmean(point,point[rand],3)
    # cmean聚类(使用前几个点)
    kind2 = cmean(point, point[0:3], 3)
    # cmean聚类（使用密度）
    # 使用加权平均平方距离和准则来refine
    kindnew=refine(point,kind1,3)
    kindnew2=refine(point,kind2,3)
    print('kindnew',kindnew)
    # print(kind)