#! /usr/bin/python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = []
import binascii
filename = 'alignedTypes.data'
with open(filename, 'rb') as f:
	 for line in f: 
#		 print int(line, 16)/16
		 x.append(int(line,16)/16)  

print x[1]
num_bins = 16
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.savefig("/home/paperspace/gpgpu-sim_simulations/benchmarks/src/4.2/C/bin/linux/release/alignedTypesfol/a.png")
#print(binascii.hexlify(content))


