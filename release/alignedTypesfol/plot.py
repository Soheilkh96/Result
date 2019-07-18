#! /usr/bin/python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv


x= np.loadtxt('alignedTypes.data', delimiter='\t', unpack=True)

print(*x)

num_bins = 16
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()
