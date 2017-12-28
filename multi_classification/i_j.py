# encoding:utf-8
# w_i / w_j 两分法

import numpy as np
from algorithm.LMSE import least_mean_square_error


# 训练得到能够分开任意两类i/j的判别函数d_k_k
def train_to_file(data_k, to_file):
    d_k_k = []
    i = 0
    j = 0
    # data_i：第i个模式类的增广样本的"序列"
    for data_i in data_k:
        d_i_k = []
        for data_j in data_k:
            d_i_j = []
            if data_i != data_j:
                print "----------------d_" + str(i) + "_" + str(j) + "----------------"
                data_i_j = data_i[:]
                for point in data_j:
                    # 规范化增广样本
                    data_i_j.append([x * (-1) for x in point])
                d_i_j = least_mean_square_error(data_i_j)
                if d_i_j is None:
                    # 如果无法求得判别函数
                    print
                    print "data_i_j不存在判别函数: "
                    for data in data_i_j:
                        print data
                        return None
            d_i_k.append(d_i_j)
            j = j + 1
            print
        d_k_k.append(d_i_k)
        i = i + 1
        j = 0

    # 写入文件
    i = 0
    j = 0
    with open(to_file, 'w') as f:
        for d_i_k in d_k_k:
            for d_i_j in d_i_k:
                f.write(str(i) + "," + str(j))
                for d in d_i_j:
                    f.write("," + str(d))
                f.write("\n")
                j = j + 1
            i = i + 1
            j = 0

    return d_k_k


# 用任意两类i/j的判别函数d_k_k，对模式x进行识别(模式x为增广矩阵)
def recognize(x, d_k_k, index):
    tag = 0
    for d_i_k in d_k_k:
        d_i_mat = np.array(d_i_k)
        if (d_i_mat.dot(x) > 0).all():
            output_str = ""
            if tag == index:
                output_str = "分类正确"
            else:
                output_str = "分类错误"

            print str(x) + "\t属于模式类" + str(tag) + "," + output_str
            return tag
        else:
            tag = tag + 1

    print str(x) + "\t属于IR区"
    return -1


def load_d_k_k(from_file):
    class_tag = []
    d_k_k = []
    d_i_k = []
    with open(from_file, 'r') as f:
        for line in f.readlines():
            d_i_j_str = line.strip().split(',')
            if d_i_j_str[0] not in class_tag:  # 出现了一个新的类
                class_tag.append(d_i_j_str[0])
                if len(class_tag) != 1:
                    d_k_k.append(d_i_k)
                    d_i_k = []
            if len(d_i_j_str) != 2:
                d_i_k.append(np.array([float(x) for x in d_i_j_str[2:]]))
        d_k_k.append(d_i_k)
    return d_k_k


def i_j_main(train_data_k, test_data_k, i_j_file):
    train_to_file(train_data_k, i_j_file)
    return load_d_k_k(i_j_file)
