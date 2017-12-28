# encoding:utf-8
# w_i / non_w_i 两分法

from algorithm.LMSE import least_mean_square_error


# 训练得到每个模式类的判别函数d_k
def train_to_file(data_k, to_file):
    d_k = []
    index = 0
    for data_i in data_k:
        print "--------------------d_" + str(index) + "--------------------"
        # data_i：第i个模式类的增广样本的"序列"
        data = data_i[:]
        for data_other in data_k:
            if data_i != data_other:
                for point in data_other:
                    # 规范化增广样本
                    data.append([x * (-1) for x in point])
        d_i = least_mean_square_error(data,c=0.28)
        if d_i is not None:
            d_k.append(d_i)
        else:
            # 如果无法求得判别函数
            print
            print "data_" + str(index) + "不存在判别函数: " + "....    " + str(len(data))
            for data_element in data:
                print data_element
        index = index + 1
        print
    return d_k


# 用k个模式类的判别函数d_k，对模式x进行识别
def recognize(x, d_k):
    positive_tag = 0
    negative_tag = 0
    index = 0
    tag = 0

    for d_i in d_k:
        if d_i.dot(x) > 0:
            tag = index
            positive_tag = positive_tag + 1
            if positive_tag > 1:
                print "d_i(X) > 0 的条件超过一个，分类失效"
                return None
        else:
            negative_tag = negative_tag + 1
        index = index + 1

    if positive_tag == 0:
        print "d_i(X) > 0 的条件无法满足，分类失效"
        return None

    print "X属于模式类" + str(tag) + ":"
    print d_k[tag]
    return d_k[tag]


def i_non_i_main(train_data_k, test_data_k, i_j_file):
    train_to_file(train_data_k, i_j_file)
