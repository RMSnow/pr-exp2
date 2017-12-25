# encoding:utf-8
# 生成数据集

import numpy as np
import matplotlib.pyplot as plt


# 生成数据集
def gen_data_set(sample_size, class_size):
    x_k = []
    y_k = []

    for k in range(6):
        x = []
        y = []

        if k == 0:
            for i in range(sample_size):
                m = np.random.random() * 20
                n = np.random.random() * m
                x.append(m)
                y.append(n)

        if k == 1:
            for i in range(sample_size):
                m = np.random.random() * 30 + 20
                if m < 25:
                    n = np.random.random() * m
                else:
                    n = np.random.random() * ((-1) * m + 50)
                x.append(m)
                y.append(n)

        if k == 2:
            for i in range(sample_size):
                m = np.random.random() * 25 + 25
                n = np.random.random() * (2 * m - 50) + ((-1) * m + 50)
                x.append(m)
                y.append(n)

        if k == 3:
            for i in range(sample_size):
                m = np.random.random() * 30 + 20
                if m < 25:
                    n = np.random.random() * m + ((-1) * m + 50)
                else:
                    n = np.random.random() * (50 - m) + m
                x.append(m)
                y.append(n)

        if k == 4:
            for i in range(sample_size):
                m = np.random.random() * 20
                n = np.random.random() * m + ((-1) * m + 50)
                x.append(m)
                y.append(n)

        if k == 5:
            for i in range(sample_size):
                m = np.random.random() * 20
                n = np.random.random() * ((-2) * m + 50) + m
                x.append(m)
                y.append(n)

        # 记录坐标
        # for i in range(sample_size):
        #     print str(k) + "," + str(x[i]) + "," + str(y[i])

        x_k.append(x)
        y_k.append(y)

    return x_k, y_k


# 生成并展示数据集
def gen_data(class_size=6, train_set_size=10, test_set_size=5):
    train_sample_size = 8
    test_sample_size = 2
    train_x_k, train_y_k = gen_data_set(train_sample_size,class_size)
    test_x_k, test_y_k = gen_data_set(test_sample_size,class_size)

    # 数据集导入文件
    with open('data/train.txt', 'w') as f:
        for i in range(class_size):
            for j in range(train_sample_size):
                f.write(str(i) + "," + str(train_x_k[i][j]) + "," + str(train_y_k[i][j])+"\n")

    with open('data/test.txt', 'w') as f:
        for i in range(class_size):
            for j in range(test_sample_size):
                f.write(str(i) + "," + str(test_x_k[i][j]) + "," + str(test_y_k[i][j])+"\n")

    # 展示数据集
    fig, axes = plt.subplots(1, 2)
    axes[0].set_title("train_data")
    axes[1].set_title("test_data")

    # 绘制三条准线
    d_1 = np.arange(50)
    d_2_x = np.arange(50)
    d_2_y = d_2_x * (-1) + 50
    d_3_x = np.zeros(50) + 20
    d_3_y = np.arange(50)
    for i in range(2):
        axes[i].plot(d_1)
        axes[i].plot(d_2_x, d_2_y)
        axes[i].plot(d_3_x, d_3_y)

    # 绘制散点图
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for k in range(class_size):
        axes[0].scatter(train_x_k[k], train_y_k[k], color=colors[k])
        axes[1].scatter(test_x_k[k], test_y_k[k], color=colors[k])

    plt.show()
