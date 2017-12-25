# encoding:utf-8
# 主函数
from multi_classification import i_non_i
from multi_classification import i_j
from dataset import gen

# 整个流程：.txt ==> train(data_k) ==> LMSE(data)


# .txt ==> train(data_k)
def load_data_k(data_file):
    class_tag = []
    data_k = []
    with open(data_file, 'r') as f:
        data_i = []
        for line in f.readlines():
            point_str = line.strip().split(',')
            if point_str[0] not in class_tag:  # 出现了一个新的类
                class_tag.append(point_str[0])
                if len(class_tag) != 1:
                    data_k.append(data_i)
                    data_i = []
            data_i.append([float(point_str[1]), float(point_str[2]), 1])
        data_k.append(data_i)   # 文档末尾
    return data_k


# 线性分类算法的主函数
def linear_classification_main():
    # 生成数据集
    # gen.gen_data()

    train_file = 'data/train.txt'
    test_file = 'data/test.txt'
    train_data_k = load_data_k(train_file)
    test_data_k = load_data_k(test_file)

    # print len(train_data_k)
    # print len(train_data_k[0])
    # print len(test_data_k)
    # print len(test_data_k[0])

    # i_non_i.train(train_data_k)
    # i_j.train(test_data_k)


linear_classification_main()
