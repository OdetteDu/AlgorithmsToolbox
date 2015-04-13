import csv
import matplotlib.pyplot as plt
import numpy as np

jac = np.empty((20,20)); l2 = np.empty((20,20)); cos = np.empty((20,20))

label = []
label_file = open('p2_dataset/groups.csv')
label_reader = csv.reader(label_file,delimiter=' ')
for entry in label_reader:
	label.append(entry[0])

# data_file = open('part1_jac_l2_cos.txt')
# data_reader = csv.reader(data_file,delimiter=',')
# for entry in data_reader:
# 	x = int(entry[0])
# 	y = int(entry[1])
# 	jac[x,y] = float(entry[2])
# 	l2[x,y] = float(entry[3])
# 	cos[x,y] = float(entry[4])

# plt.pcolor(cos,cmap=plt.cm.Blues,edgecolors='k')
# plt.xticks(np.arange(0,20)+0.5, label)
# plt.yticks(np.arange(0,20)+0.5, label)
# plt.xticks(rotation=-90)
# plt.subplots_adjust(top=0.99,bottom=0.22,right=0.95)
# plt.colorbar()
# plt.show()

nnb = np.empty((20,20))
nnb_file = open('part1_nnb.txt')
nnb_reader = csv.reader(nnb_file,delimiter=',')
for entry in nnb_reader:
	x = int(entry[0])
	y = int(entry[1])
	nnb[x,y] = int(entry[2])
plt.pcolor(nnb,cmap=plt.cm.Blues,edgecolors='k')
plt.xticks(np.arange(0,20)+0.5, label)
plt.yticks(np.arange(0,20)+0.5, label)
plt.xticks(rotation=-90)
plt.subplots_adjust(top=0.99,bottom=0.22,right=0.95)
plt.colorbar()
plt.show()

