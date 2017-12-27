# encoding:utf-8

from multi_classification import i_non_i
from multi_classification import i_j
from data_set import gen
import numpy as np
import matplotlib.pyplot as plt


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


# 展示识别结果
def show_output(train_data_k, test_data_k, class_size, d_k_k=None, d_k=None):
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
    fig, axes = plt.subplots(1, 3, sharex=True, sharey=True)
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
        axes[2].scatter(test_x_k[k], test_y_k[k], color=colors[k], s=10)

    # i_j分类法识别结果
    if d_k_k is not None:
        recognize_sum = 0
        test_sum = 0
        for test_k in test_data_k:
            for point in test_k:
                index = test_data_k.index(test_k)
                tag = i_j.recognize(point, d_k_k, index)
                if tag == index:
                    recognize_sum += 1
                test_sum += 1
                if tag != -1:
                    axes[2].plot(point[0], point[1], color=colors[tag], marker='x')
                    # else:
                    #     axes[2].plot(point[0], point[1], color='k', marker='x')

        recognize_rate = float(recognize_sum) / float(test_sum)
        print "\n识别正确率为：" + str(recognize_rate)

    # plt.subplots_adjust(wspace=0)
    plt.show()


# 线性分类算法的主函数
def linear_classification_main(class_size=6):
    # 随机生成数据集并导出文件
    train_random_file = 'data/_train.txt'
    test_random_file = 'data/_test.txt'
    gen.gen_data_to_file(train_random_file, test_random_file)

    # 从文件中加载数据集
    train_file = 'data/train.txt'
    test_file = 'data/test.txt'
    train_data_k = load_data_k(train_file)
    test_data_k = load_data_k(test_file)

    while True:
        print "----------------------"
        print ">>> 请选择下列算法中的一项进行线性分类："
        print "\t1. LMSE算法（采用i_j分类）"
        print "\t2. LMSE算法（采用i_non_i分类）"
        print "\t3. 分段线性判别法"
        print "\t4. 退出\n"
        choice = input("请输入1-4中的一项：")
        if choice is 1:
            # i_j 分类法
            i_j_file = 'output/i_j.txt'
            i_j_d = i_j.i_j_main(train_data_k, test_data_k, i_j_file)
            # 展示结果
            show_output(train_data_k, test_data_k, class_size, d_k_k=i_j_d)
        elif choice is 2:
            pass
        elif choice is 3:
            pass
        elif choice is 4:
            return
        else:
            print "输入非法，请输入标号1-4"


linear_classification_main()
