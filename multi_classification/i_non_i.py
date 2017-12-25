# encoding:utf-8
# w_i / non_w_i 两分法

from LMSE import least_mean_square_error


# 训练得到每个模式类的判别函数d_k
def train(data_k):
    d_k = []
    for data_i in data_k:
        # data_i：第i个模式类的增广样本的"序列"
        d_i = least_mean_square_error(data_i)
        if d_i is not None:
            d_k.append(d_i)
        else:
            # 如果无法求得判别函数--------------------------------------
            print "data_i" + str(d_i) + " 不存在判别函数"
            return None
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
