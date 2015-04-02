## Lecture 2 - Apr.1

### Majority Element

Input: 

- array A, size n, one value occurs > $n/2$

Solution:

	counter := 0, current := NULL
	for i = 1 to n
		if counter == 0
			current := A[i], counter ++
		else if A[i] == current
			counter ++
		else
			counter --

### Heavy Hitters

- Input: array A, size $n$, parameter $k$
- (array can be very large, millions of elements)
- Output: all values with frequency (int [0-n]) $\ge n/k$
- (output may be empty, e.g. all elements distinct)
- (Majority is a special case of heavy hitters)

Application:

- popular products
- popular queries
- TCP flows
- volatile stock
- etc.

Requirements:

- One pass
- Small working memory

Fact:

- no small-space 1-pass algorithm exists

Intuition:

- set $k = n/2$, output elements with freq at least 2
- suppose A has form: $s$ number of distinct elements & $x$
- $x \in s$ => output $x$; else don't output $x$
- to answer "$x$ belongs to $s$", linear space

Relaxation ($\epsilon$-H.H.)

- For a parameter $\epsilon$ (e.g. $\frac{1}{2k}$), return:
	1. every value with frequency $> n/k$
	2. only values with freq $\ge n/k - \epsilon * n$
	3. allow space to grow as $\epsilon$ decreases
	
Solution: Count-min Sketch ('03)

- implemented in real system (include Google + AT&T)
- hashing-based
- "lossy compression"
- pros: parallelizes well

Role Modes: Bloom Filters

- did I insert the element before, but will never retrieve it
- solve membership queries (x belongs to s?)
- super fast (constant time insert, lookup, parallelize well)
	- e.g. 8 bits per element stored
	- false positive prob ~ 2%
	- first and perhaps only with false, but only false positive, never false negative (why?)
	- applicable in cases tolerating false positive
	
CMS Implementation

- Operations: increment(t), Count(t)
- Parameters: b = # of buckets, l = # of hash_fns
	- n billion, b thousands, l perhaps 5

Data Structure

- 2-D array of CMS of counters, l * b
- smaller b => compress more, more error

code for increment (x)
	
	for i = 1...l
		increment CMS[i][h_i(x)]
	// only different with Bloom Filter is that BF only has 0,1
	
Observation:

- For any x, row i
- CMS[i][h_i(x)], increment 10 times, might be more (collisions)
- estimates? average? no, single-sided error

code for count (x)

	return min{i=1..l} CMS[i][h_i(x)]
	
Observation on b,l:

- b, l, decided with tradeoffs of space and tolenrence with over estimates
- bigger b, bigger l, smaller error

#### Error Analysis

Tring to prove, typically with a given x, count (x) is close to freq(x)

Fix x, row i:

	E_i = CMS[i][h_i(x)]
	E_i = f_x + Sum{y belongs to S}f_y
	where S = {y != x | h_i (y) = h_i (x)}
	
Assume (*):

	for any y!=x, Pr[h_i(y)=h_i(x)] <= 1/b
	// THE definition of a universal hash function
	// not true with MD5, since it's deterministic function
	// a herustic analysis with a good hash function
	
Resoning:

	E[E_i] = E[f_x + Sum{y != x} 1_y * f_y]
	where 1_y = {1 if h_i(x) = h_i(y)/ 0 o.w.}
	= f_x + sum{y!=x}f_y * E[1_y]
	<= f_x + 1/b * Sum{y!=x} f_y
	<= f_x + n/b
	// sum (y!=x) f_y <= n
	// if b = 1/\epsilon{} ...

Linear Expectiations
	
	E[sum X_i] = sum E[X_i], even if Xj's not independent



		


	