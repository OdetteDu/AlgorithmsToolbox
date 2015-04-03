import random
import numpy
from matplotlib import pyplot

N = 100000
r = range (0, N)

def throw_cnt_rand (bin, cnt):
	samples = random.sample (r, cnt)
	minimum = N + 1
	ties = []
	for s in samples:
		if (bin[s] < minimum):
			ties = [s]
			minimum = bin[s]
		elif (bin[s] == minimum):
			ties.append (s)
	target = random.sample (ties, 1) [0]
	bin[target] = bin[target] + 1

def throw_one_rand (bin):
	throw_cnt_rand (bin, 1)

def throw_two_rand (bin):
	throw_cnt_rand (bin, 2)

def throw_three_rand (bin):
	throw_cnt_rand (bin, 3)

def throw_half_determ (bin):
	s1 = random.randrange (0, N/2)
	s2 = random.randrange (N/2, N)
	if (bin[s2] < bin[s1]):
		bin[s2] = bin[s2] + 1
	else:
		bin[s1] = bin[s1] + 1

def simulate (strategy_func):
	bin = [0] * N
	for i in r:
		strategy_func (bin)
	return max (bin)

if __name__ == "__main__":
	
	# simulation:

	# one_rand = []
	# two_rand = []
	# three_rand = []
	# half_determ = [] 
	# for i in range (0, 30):
	# 	one_rand.append (simulate (throw_one_rand))
	# 	two_rand.append (simulate (throw_two_rand))
	# 	three_rand.append (simulate (throw_three_rand))
	# 	half_determ.append (simulate (throw_half_determ))
	# print one_rand
	# print two_rand
	# print three_rand
	# print half_determ

	# results:

	one_rand = [8, 8, 8, 8, 7, 7, 8, 7, 8, 7, 8, 9, 7, 7, 7, 7, 7, 8, 8, 7, 7, 7, 7, 8, 7, 8, 8, 8, 7, 8]
	two_rand = [3, 4, 3, 3, 4, 3, 4, 3, 3, 3, 3, 4, 4, 3, 3, 3, 4, 3, 3, 3, 3, 3, 4, 3, 3, 4, 3, 3, 4, 3]
	three_rand = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
	half_determ = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

	# ploting:

	bin_range = numpy.arange (0.5, 10.5, 1)
	xlim = (0,10)
	ylim = (0,32)

	pyplot.subplot (411)
	pyplot.hist (one_rand, bins = bin_range, color = 'r', alpha = 0.9)
	pyplot.ylim(ylim)
	pyplot.xlim(xlim)
	pyplot.title ('S1')

	pyplot.subplot (412)
	pyplot.hist (two_rand, bins = bin_range, color = 'b', alpha = 0.9)
	pyplot.ylim(ylim)
	pyplot.xlim(xlim)
	pyplot.title ('S2')

	pyplot.subplot (413)
	pyplot.hist (three_rand, bins = bin_range, color = 'g', alpha = 0.9)
	pyplot.ylim(ylim)
	pyplot.xlim(xlim)
	pyplot.title ('S3')

	pyplot.subplot (414)
	pyplot.hist (half_determ, bins = bin_range, color = 'y', alpha = 0.9)
	pyplot.ylim(ylim)
	pyplot.xlim(xlim)
	pyplot.title ('S4')
	pyplot.show ()
    
