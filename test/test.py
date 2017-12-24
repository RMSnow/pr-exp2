# encoding:utf-8
from LMSE import *
from multi_classification.i_non_i import *


def test_lmse():
    data_1 = [[0, 0, 1], [0, 1, 1], [-1, 0, -1], [-1, -1, -1]]
    data_2 = [[0, 0, 1], [1, 1, 1], [0, -1, -1], [-1, 0, -1]]
    print "------------test1---------------"
    least_mean_square_error(data_1)
    print "------------test2---------------"
    least_mean_square_error(data_2)


def test_i_non_i():
    x = np.array([7, 5, 1]).T
    d_1 = np.array([-1, 1, 1])
    d_2 = np.array([1, 1, -4])
    d_3 = np.array([0, -1, 1])
    d_k = [d_1, d_2, d_3]

    recognize(x, d_k)


# test_lmse()
# test_i_non_i()

a = [1, 2, 3, 4]
arr = np.array([a, a, a])
x = [0, 0, 0, 1]
value = np.array(x).T

print np.array(a)
print np.array(a).dot(value)
print arr
print arr.dot(value)
