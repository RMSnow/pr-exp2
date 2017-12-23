# encoding:utf-8

import numpy as np
from numpy.linalg import inv


# 最小平方误差算法（Least Mean Square Error, LMSE）
# （1）输入参数：矩阵x
# （2）求X的伪逆矩阵 x# = (xT x)-1 xT
# （3）设置初值c和B(1)
# （4）计算e(k)，并进行可分性判别
# （5）计算W(k+1)、B(k+1)


def least_mean_square_error(data, c=1):
    x = np.array(data, dtype=np.float64)
    x_sharp = inv(x.T.dot(x)).dot(x.T)
    row, col = x.shape

    k = 1
    while True:
        if k == 1:
            b_k = np.ones(row).T
        else:
            b_k = b(k, b_k, c, e_k)

        w_k = w(k, x_sharp, b_k)
        e_k = e(k, x, w_k, b_k)

        if (e_k == 0).all():
            print "线性可分，解为"
            print w_k
            break
        elif (e_k >= 0).all():
            print "线性可分，继续迭代可得最优解"
        elif (e_k <= 0).all():
            print e_k
            print "e_k < 0, 停止迭代，检查XW(k)"
            if (x.dot(w_k) > 0).all():
                print "线性可分，解为" + w_k
            else:
                print "XW(k) > 0 不成立，故无解，算法结束"
            break
        else:
            k = k + 1


def b(k, b_k, c, e_k):
    return b_k + c * (e_k + np.abs(e_k))


def e(k, x, w_k, b_k):
    return x.dot(w_k) - b_k


def w(k, x_sharp, b_k):
    return x_sharp.dot(b_k)
