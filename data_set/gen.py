# encoding:utf-8
# 生成数据集

import numpy as np


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


# 生成数据集并导入文件
def gen_data_to_file(train_file, test_file, class_size=6, train_set_size=10, test_set_size=5):
    train_sample_size = 8
    test_sample_size = 2
    train_x_k, train_y_k = gen_data_set(train_sample_size, class_size)
    test_x_k, test_y_k = gen_data_set(test_sample_size, class_size)

    # 数据集导入文件
    with open(train_file, 'w') as f:
        for i in range(class_size):
            for j in range(train_sample_size):
                f.write(str(i) + "," + str(train_x_k[i][j]) + "," + str(train_y_k[i][j]) + "\n")

    with open(test_file, 'w') as f:
        for i in range(class_size):
            for j in range(test_sample_size):
                f.write(str(i) + "," + str(test_x_k[i][j]) + "," + str(test_y_k[i][j]) + "\n")
