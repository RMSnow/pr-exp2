# encoding:utf-8
from numpy.matlib import randn

from LMSE import least_mean_square_error

data_1 = [[0, 0, 1], [0, 1, 1], [-1, 0, -1], [-1, -1, -1]]
data_2 = [[0, 0, 1], [1, 1, 1], [0, -1, -1], [-1, 0, -1]]
print "------------test1---------------"
least_mean_square_error(data_1)
print "------------test2---------------"
least_mean_square_error(data_2)
