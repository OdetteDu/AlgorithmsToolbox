import csv
import matplotlib.pyplot as plt
import numpy as np


label = []
label_file = open('p2_dataset/groups.csv')
label_reader = csv.reader(label_file,delimiter=' ')
for entry in label_reader:
	label.append(entry[0])

nnb = np.empty((20,20))
nnb_file = open('part2_50_nnb.txt')
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

# original = []; reduced = [];
# cos_file = open('part2_50_cos.txt')
# cos_reader = csv.reader(cos_file,delimiter=',')
# for entry in cos_reader:
# 	original.append(float(entry[2]))
# 	reduced.append(float(entry[3]))
# plt.scatter(original,reduced)
# plt.xlabel('original')
# plt.ylabel('reduced')
# plt.title('d=50')
# plt.show()
