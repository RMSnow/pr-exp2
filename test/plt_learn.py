# encoding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax1.set_title('test111')
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# plt.plot([1.5, 3.5, -2, 1.6])
ax3.plot(randn(50).cumsum(), 'g--')
ax3.plot(randn(50).cumsum(), 'k--')
ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))

x = np.arange(10)
y = np.arange(0, 20, 2)
print x
print y
ax4.plot(x, y)
ax4.plot(np.arange(20) + 1)

plt.show()

# K-Means
#
# def show_k_means(data_mat, k=5):
#     num_samples, dim = data_mat.shape
#     centroids, cluster_assignment = k_means(data_mat, k)
#     mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
#     for i in range(num_samples):
#         mark_index = int(cluster_assignment[i, 0])
#         plt.plot(data_mat[i, 0], data_mat[i, 1], mark[mark_index], marker='x')
#     plt.show()
#     return
