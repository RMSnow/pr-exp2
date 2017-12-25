# encoding:utf-8
# w_i / w_j 两分法

from LMSE import least_mean_square_error
import numpy as np


# 训练得到能够分开任意两类i/j的判别函数d_k_k
def train(data_k):
    d_k_k = []
    # data_i：第i个模式类的增广样本的"序列"
    for data_i in data_k:
        d_i_k = []
        for data_j in data_k:
            if data_i != data_j:
                data_i_j = data_i
                for point in data_j:
                    # 规范化增广样本
                    data_i_j.append([x * (-1) for x in point])

                d_i_j = least_mean_square_error(data_i_j)
                if d_i_j is None:
                    # 如果无法求得判别函数--------------------------------------
                    print "data_i_j" + str(data_i_j) + " 不存在判别函数"
                    return None

            d_i_k.append(d_i_j)
        d_k_k.append(d_i_k)
    return d_k_k


# 用任意两类i/j的判别函数d_k_k，对模式x进行识别(模式x为增广矩阵)
def recognize(x, d_k_k):
    tag = 0
    for d_i_k in d_k_k:
        d_i_mat = np.array(d_i_k)
        if (d_i_mat.dot(x) > 0).all():
            print "X属于模式类" + str(tag)
            return tag
        else:
            tag = tag + 1

    print "IR区"
    return -1
