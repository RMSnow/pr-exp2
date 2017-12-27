# encoding:utf-8
# 主函数
from multi_classification import i_non_i
from multi_classification import i_j
from dataset import gen
import numpy as np
import matplotlib.pyplot as plt


# 整个流程：.txt ==> train(data_k) ==> LMSE(data)


# 从文件加载数据集 .txt ==> train(data_k)
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
        data_k.append(data_i)  # 文档末尾
    return data_k


# 将数据data_k展示出来
def show_data(train_data_k, test_data_k, d_k, class_size=6):
    # 获取x轴与y轴数据
    train_x_k = []
    train_y_k = []
    test_x_k = []
    test_y_k = []

    for i in range(class_size):
        train_x_k.append([x[0] for x in train_data_k[i]])
        train_y_k.append([x[1] for x in train_data_k[i]])
        test_x_k.append([x[0] for x in test_data_k[i]])
        test_y_k.append([x[1] for x in test_data_k[i]])

    # 展示数据集
    fig, axes = plt.subplots(1, 3)
    axes[0].set_title("train_data")
    axes[1].set_title("test_data")
    axes[2].set_title("output")

    # 绘制三条准线
    d_1 = np.arange(50)
    d_2_x = np.arange(50)
    d_2_y = d_2_x * (-1) + 50
    d_3_x = np.zeros(50) + 20
    d_3_y = np.arange(50)
    for ax in axes[0:2]:
        ax.plot(d_1)
        ax.plot(d_2_x, d_2_y)
        ax.plot(d_3_x, d_3_y)

    # 绘制散点图
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for k in range(class_size):
        axes[0].scatter(train_x_k[k], train_y_k[k], color=colors[k])
        axes[1].scatter(test_x_k[k], test_y_k[k], color=colors[k])
        # axes[2].scatter(train_x_k[k], train_y_k[k], color=colors[k])

    # 绘制判别函数
    # for d_i in d_k:
    #     k = (-1) * (d_i[0]) / (d_i[1])
    #     b = (-1) * d_i[2] / d_i[1]
    #     d_i_x = np.arange(50)
    #     d_i_y = int(k) * d_i_x
    #     axes[2].plot(d_i_x, d_i_y)
    #
    #     print k
    #     print b
    #     print

    plt.show()


# 线性分类算法的主函数
def linear_classification_main():
    # 随机生成数据集并导入文件
    train_random_file = 'data/train_random.txt'
    test_random_file = 'data/test_random.txt'
    gen.gen_data_to_file(train_random_file, test_random_file)

    # 从文件中加载数据集
    train_file = 'data/train.txt'
    test_file = 'data/test.txt'
    train_data_k = load_data_k(train_file)
    test_data_k = load_data_k(test_file)

    # i_j 分类法训练，并导入文件
    i_j_file = 'output/i_j.txt'
    i_j.train_to_file(train_data_k, i_j_file)

    # 从文件中加载判别函数并评测识别效果
    d_k_k = i_j.load_d_k_k(i_j_file)
    for test_k in test_data_k:
        for point in test_k:
            i_j.recognize(point, d_k_k)

            # show_data(train_data_k, test_data_k, d_k=[])


linear_classification_main()
