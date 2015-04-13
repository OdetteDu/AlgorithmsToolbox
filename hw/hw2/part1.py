import csv
import math

def cal_sim_sparse (data,nnb,g1,g2,x1,x2):
	dict1 = data[g1][x1]
	nnb1 = nnb[g1][x1]
	dict2 = data[g2][x2]
	nnb2 = nnb[g2][x2]

	d1keys = set(dict1.keys())
	d2keys = set(dict2.keys())
	d1 = d1keys-d2keys
	d2 = d2keys-d1keys
	d1_d2 = d1keys&d2keys

	jac_min_sum = 0; jac_max_sum = 0
	l2_sum = 0
	cos_prod = 0; cos_l2_1 = 0; cos_l2_2 = 0;

	for k in d1:
		v = dict1[k]
		jac_max_sum += v
		l2_sum += v*v
		cos_l2_1 += v*v

	for k in d2:
		v = dict2[k]
		jac_max_sum += v
		l2_sum += v*v
		cos_l2_2 += v*v

	for k in d1_d2:
		v1 = dict1[k]
		v2 = dict2[k]
		jac_min_sum += min(v1,v2)
		jac_max_sum += max(v1,v2)
		l2_sum += (v1-v2)*(v1-v2)
		cos_l2_1 += v1*v1
		cos_l2_2 += v2*v2
		cos_prod += v1*v2

	jac = jac_min_sum*1.0/jac_max_sum
	l2 = -math.sqrt(l2_sum)
	cosine = cos_prod/math.sqrt(cos_l2_1)/math.sqrt(cos_l2_2)

	# update n1's nearst
	if (g2 != g1) and (jac>nnb1[1]):
		nnb1[0] = g2
		nnb1[1] = jac

	return [jac, l2, cosine]


# read in articleId->groupId list
label = []
label_file = open('p2_dataset/label.csv','r')
label_reader = csv.reader(label_file,delimiter=' ')
for entry in label_reader:
	groupId = int(entry[0])
	label.append(groupId)

# data is array<array<article>>
# nearest neighbor is array<array<[group,distance]>>
data = []; nnb = [];
for idx in range(0,20):
	data.append([])
	nnb.append([])

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

# calculate jaccard, L2, cosine similarity
for g1 in range(0,20):
	for g2 in range(0,20):
		jac_avg = 0.0; l2_avg = 0.0; cos_avg = 0.0
		cnt = 0
		for x1 in range(0, len(data[g1])):
			for x2 in range(0, len(data[g2])):
				r = cal_sim_sparse(data,nnb,g1,g2,x1,x2)
				jac_avg += r[0]
				l2_avg += r[1]
				cos_avg += r[2]
				cnt += 1
		jac_avg = jac_avg/cnt
		l2_avg = l2_avg/cnt
		cos_avg = cos_avg/cnt
		# print "%d,%d,%f,%f,%f" % (g1,g2,jac_avg, l2_avg, cos_avg)

# calculate nnb similarity
for g1 in range(0,20):
	for g2 in range(0,20):
		n = 0
		for entry in nnb[g1]:
			if entry[0]==g2:
				n += 1
		print "%d,%d,%d" % (g1,g2,n)



