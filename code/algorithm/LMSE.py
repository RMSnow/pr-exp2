# encoding:utf-8

import numpy as np
from numpy.linalg import inv


# 最小平方误差算法（Least Mean Square Error, LMSE）
# （1）输入参数：规范化增广样本矩阵x
# （2）求X的伪逆矩阵 x# = (xT x)-1 xT
# （3）设置初值c和B(1)
# （4）计算e(k)，并进行可分性判别
# （5）计算W(k+1)、B(k+1)


def least_mean_square_error(data, b_1=0.1, c=1, k_n=100000):
    # x：规范化增广样本"矩阵"
    x = np.array(data, dtype=np.float64)
    x_sharp = inv(x.T.dot(x)).dot(x.T)
    row, col = x.shape

    # print x

    k = 1
    while k < k_n:
        if k % 10000 == 0:
            print "第" + str(k) + "次迭代..."

        if k == 1:
            # 设置初值B(1)
            b_k = (np.zeros(row) + b_1).T
            # b_k = x[:, 0]
            w_k = x_sharp.dot(b_k)
        else:
            b_k = b(k + 1, b_k, c, e_k)
            w_k = w(k + 1, w_k, c, x_sharp, e_k)

        # w_k = w(k+1, x_sharp, b_k)        # 方法二
        e_k = e(k + 1, x, w_k, b_k)

        if (e_k == 0).all():
            print "第" + str(k) + "次迭代... " + "线性可分，解为"
            print w_k
            return w_k
        elif (e_k >= 0).all():
            k = k + 1
            print "第" + str(k) + "次迭代... " + "线性可分，继续迭代可得最优解"
        elif (e_k <= 0).all():
            # print e_k
            print "第" + str(k) + "次迭代... " + "e_k < 0, 停止迭代，检查XW(k)"
            if (x.dot(w_k) > 0).all():
                print "线性可分，解为" + str(w_k)
                return w_k
            else:
                print "XW(k) > 0 不成立，故无解，算法结束"
                return None
        else:
            k = k + 1

    return None


def b(k, b_k, c, e_k):
    return b_k + c * (e_k + np.abs(e_k))


def e(k, x, w_k, b_k):
    return x.dot(w_k) - b_k


# 方法一
def w(k, w_k, c, x_sharp, e_k):
    return w_k + c * x_sharp.dot(np.abs(e_k))

# 方法二
# def w(k, x_sharp, b_k):
#     return x_sharp.dot(b_k)
