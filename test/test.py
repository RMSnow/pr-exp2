# encoding:utf-8
from LMSE import *
from multi_classification import i_non_i
from multi_classification import i_j


def test_lmse():
    data_1 = [[0, 0, 1], [0, 1, 1], [-1, 0, -1], [-1, -1, -1]]
    data_2 = [[0, 0, 1], [1, 1, 1], [0, -1, -1], [-1, 0, -1]]
    print "------------test1---------------"
    least_mean_square_error(data_1)
    print "------------test2---------------"
    least_mean_square_error(data_2)


# test_lmse()

def test_i_non_i():
    x = np.array([7, 5, 1]).T
    d_1 = np.array([-1, 1, 1])
    d_2 = np.array([1, 1, -4])
    d_3 = np.array([0, -1, 1])
    d_k = [d_1, d_2, d_3]

    i_non_i.recognize(x, d_k)


# test_i_non_i()

# -------------------------
def test_i_j():
    # data = [[[0, 0, 1], [0, 1, 1]], [[1, 0, 1], [1, 1, 1]]]
    # a = i_j.train(data)
    # print a

    x = np.array([10, 10, 1]).T
    d_1_2 = [-1, -1, 5]
    d_1_3 = [-1, 0, 3]
    d_2_3 = [-1, 1, 0]

    d_1_k = [d_1_2, d_1_3]
    d_2_k = [[1, 1, -5], d_2_3]
    d_3_k = [[1, 0, -3], [1, -1, 0]]

    d_k_k = [d_1_k, d_2_k, d_3_k]
    i_j.recognize(x, d_k_k)


test_i_j()


def test_python():
    a = [1, 2, 3, 4]
    b = [x * (-1) for x in a]
    print a
    print b

    print "--------"
    w_i = [[2, 1, 1], [2, 0, 1]]
    w_j = [[0, 1, 1]]
    tag = 0
    for w in w_i:
        for y in w_i:
            if w == y:
                print "tag = " + str(tag)
            tag = tag + 1

# test_python()
