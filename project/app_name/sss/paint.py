# -*-coding:utf-8-*- 
import numpy as np
import matplotlib.pyplot as plt
JINIPATH = 'F:/t8_28_2/t8_27_wanshang/t8_26/t8/project_name/static/js/assets/img/lingxiu/'


def zhitu(x1):
    y1=[]
    yn=float(1)/float(len(x1))
    for i in xrange(len(x1)-1):
        y1.append(float(i)*yn)
    y1.append(1)
    x=[0,1]
    y=[1,0]
    plt.figure()               #创建绘图对象
    for i in xrange(2):
        if i==0:
            plt.plot(x,y)
        else:
            plt.plot(x1,y1)    #对当前绘图对象进行绘图（两个参数是x，y轴的数据）
    plt.xlabel("P")
    plt.ylabel("L(p)")
    plt.title("Lorenz curve")
    plt.savefig(JINIPATH+"paint11.jpg") #保存图像


