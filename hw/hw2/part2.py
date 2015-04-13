import csv
import math
import numpy as np

def cal_cos_sim (data,g1,g2,x1,x2):
	dict1 = data[g1][x1]
	dict2 = data[g2][x2]

	d1keys = set(dict1.keys())
	d2keys = set(dict2.keys())
	d1 = d1keys-d2keys
	d2 = d2keys-d1keys
	d1_d2 = d1keys&d2keys

	cos_prod = 0; cos_l2_1 = 0; cos_l2_2 = 0;
	for k in d1:
		v = dict1[k]
		cos_l2_1 += v*v
	for k in d2:
		v = dict2[k]
		cos_l2_2 += v*v
	for k in d1_d2:
		v1 = dict1[k]
		v2 = dict2[k]
		cos_l2_1 += v1*v1
		cos_l2_2 += v2*v2
		cos_prod += v1*v2
	cosine = cos_prod/math.sqrt(cos_l2_1)/math.sqrt(cos_l2_2)
	return cosine

def cal_cos_reduced (reduced,nnb,g1,g2,x1,x2):
	a1 = reduced[g1][x1]
	a2 = reduced[g2][x2]
	nnb1 = nnb[g1][x1]
	cosine = (a1*a2).sum()/math.sqrt((a1*a1).sum())/math.sqrt((a2*a2).sum())
	if (g2 != g1) and (cosine>nnb1[1]):
		nnb1[0] = g2
		nnb1[1] = cosine
	return cosine

# read in articleId->groupId list
label = []
label_file = open('p2_dataset/label.csv','r')
label_reader = csv.reader(label_file,delimiter=' ')
for entry in label_reader:
	groupId = int(entry[0])
	label.append(groupId)

# data is array<array<article>>
# nearest neighbor is array<array<[group,distance]>>
data = []; nnb = []; reduced = []
for idx in range(0,20):
	data.append([])
	nnb.append([])
	reduced.append([])

# read in data
data_file = open('p2_dataset/data50.csv','r')
data_reader = csv.reader(data_file,delimiter=' ')

cur_id = -1
for entry in data_reader:
	# retrive entry data
	article_id = int(entry[0])
	word_id = int(entry[1])
	count = int(entry[2])
	# create new article infomation if needed
	if cur_id != article_id:
		cur_id = article_id
		cur = {}
		group_id = label[cur_id]-1
		data[group_id].append(cur)
		nnb[group_id].append([-1,-1])
	cur[word_id] = count

# reduce
k = 62000
d = 50

M = np.random.normal(0,1,(d,k))
for group_id in range(0,20):
	for original in data[group_id]:
		r = np.empty(d)
		for i in range(0,d):
			sum = 0
			for key in original.keys():
				sum += M[i,key] * original[key]
			r[i] = sum
		reduced[group_id].append(r)

# calculate reduced_sim and get nearest neighbor
for g1 in range(0,20):
	for g2 in range(0,20):
		for x1 in range(0,len(reduced[g1])):
			for x2 in range(0,len(reduced[g2])):
				cal_cos_reduced(reduced,nnb,g1,g2,x1,x2)

# print "---calculate nnb similarity---"
# print "g1,g2,n"
for g1 in range(0,20):
	for g2 in range(0,20):
		n = 0
		for entry in nnb[g1]:
			if entry[0]==g2:
				n += 1
		# print "%d,%d,%d" % (g1,g2,n)

# print "--calculate original and reduced cos--"
# print "g1,x1,original,reduced"
# calculate with article 3
for g1 in range(0,20):
	for x1 in range(0,len(reduced[g1])):
		original_cos = cal_cos_sim(data,0,g1,2,x1)
		reduced_cos = cal_cos_reduced(reduced,nnb,0,g1,2,x1)
		print "%d,%d,%f,%f" % (g1,x1,original_cos,reduced_cos)




