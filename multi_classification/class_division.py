# encoding:utf-8
# 分段线性判别函数：已知子类的划分

import numpy as np

from algorithm.LMSE import least_mean_square_error


def train_to_file(data_k, to_file):
    d_k = []
    index = 0
    for i in range(0, 6, 2):
        print "------------划分父类_" + str(index) + "------------"
        data_division_1 = data_k[i][:]
        data_division_2 = data_k[i + 1][:]
        data_i = data_division_1
        for point in data_division_2:
            data_i.append([x * (-1) for x in point])
        d_i = least_mean_square_error(data_i, b_1=1, c=0.8)
        if d_i is None:
            # 如果无法求得判别函数
            print
            print "data_i不存在判别函数: "
            for data in data_i:
                print data
                # return None
        d_k.append(d_i)
        index += 1
        print

    # 写入文件
    index = 0
    with open(to_file, 'w') as f:
        for d_i in d_k:
            f.write(str(index))
            for d in d_i:
                f.write("," + str(d))
            f.write("\n")
            index += 1

    return d_k


def recognize(x, d_k, index):
    d_0_division_1 = d_k[0].dot(x)
    d_0_division_2 = ((-1) * d_k[0]).dot(x)
    d_1_division_1 = d_k[1].dot(x)
    d_1_division_2 = ((-1) * d_k[1]).dot(x)
    d_2_division_1 = d_k[2].dot(x)
    d_2_division_2 = ((-1) * d_k[2]).dot(x)

    # 首先用子类代替父类
    d_0 = d_0_division_1 if d_0_division_1 > d_0_division_2 else d_0_division_2
    d_1 = d_1_division_1 if d_1_division_1 > d_1_division_2 else d_1_division_2
    d_2 = d_2_division_1 if d_2_division_1 > d_2_division_2 else d_2_division_2

    # 再用父类判别
    tag = -1
    if d_0 > d_1 and d_0 > d_2:
        tag = 0
    if d_1 > d_0 and d_1 > d_2:
        tag = 1
    if d_2 > d_0 and d_2 > d_1:
        tag = 2

    if tag == index:
        output_str = "分类正确"
    elif tag == -1:
        output_str = "IR区"
    else:
        output_str = "分类错误"

    print str(x) + "\t属于模式类" + str(tag) + "," + output_str
    return tag


def load_d_k(from_file):
    class_tag = []
    d_k = []
    with open(from_file, 'r') as f:
        for line in f.readlines():
            d_i_str = line.strip().split(',')
            d_k.append(np.array([float(x) for x in d_i_str[1:]]))
    return d_k


def class_division_main(train_data_k, test_data_k, class_division_file):
    train_to_file(train_data_k, class_division_file)
    return load_d_k(class_division_file)
