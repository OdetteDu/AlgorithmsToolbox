## Lecture 2 - Apr.1

### Majority Element

Input: 

- array A, size $n$, element with frequency > $n/2$
	- there will be at most one output, maybe empty

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
	- array can be very large, millions of elements
- Output: all values with frequency (int [0-n]) $\ge n/k$
	- output may be empty, e.g. all elements distinct
- Majority is a special case of heavy hitters: $k=2$

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

- no small-space (smaller than linear space) 1-pass algorithm exists

Intuition:

- set $k = n/2$, output elements with freq at least 2
- suppose A has form: first $s$ number of distinct elements followed by $x$
- $x \in s$ => output $x$; else don't output $x$
- to answer "$x$ belongs to $s$?", linear space

Relaxation ($\epsilon$-H.H.)

- For a parameter $\epsilon$ (e.g. $\frac{1}{2k}$), return:
	1. every value with frequency $> n/k$
	2. only values with freq $\ge n/k - \epsilon * n$
	3. allow space to grow as $\epsilon$ decreases
	
Solution: Count-Min Sketch ('03)

- implemented in real system (include Google + AT&T)
- hashing-based
- "lossy compression"
- pros: parallelizes well

Role Modes: Bloom Filters

- Tell if the element inserted before, but never retrieve it
- solve membership queries ($x \in s$?)
- super fast (constant time insert, lookup, parallelizes well)
	- e.g. 8 bits per element stored
	- false positive prob $\approx 2\%$
	- first and perhaps only algorithm with false and uncertainty, but only *false positive*, never *false negative* (due to hash collision)
	- applicable in cases tolerating false positive
	
CMS Implementation

- Operations: `increment (t)`, `count (t)`
- Parameters: 
	- $b$ = # of buckets
	- $l$ = # of hash_fns
	- $n \propto$ billion, $b \propto$ thousands, $l \approx$ 5

Data Structure

- 2-D array of CMS counters, $l * b$
- smaller $b$ => compress more, more error

code for `increment (x)`:
	
	for i = 1...l
		increment CMS[i][h_i(x)]
	// only difference with Bloom Filter is that BF only has 0,1 instead of a CMS counter
	
Observation

- For any $x$, row $i$
- CMS[$i$][$h_i(x)$], increment 10 times, CMS $\ge 10$ (due to Hash collisions)
- How to estimate the actual increment count?
	- No: average, single-sided error
	- Yes: minimum

code for `count (x)`:

	return $min_{i=1..l} CMS[i][h_i(x)]$
	
Observation on $b$, $l$

- $b$, $l$, decided with trade-offs of space and tolerance with over estimates
- bigger $b$, bigger $l$, smaller error

#### Error Analysis

Trying to prove, typically with a given $x$, $count(x)$ is close to $freq(x)$

Fix $x$, row $i$:

- $E_i = CMS[i][h_i(x)]$
- $E_i = f_x + \sum_{y\in{}S}f_y$
- where $S = y | y\neq{}x, h_i(y)=h_i(x)$
	
Assume (*):

- for any $y\neq{}x$, $Pr[h_i(y)=h_i(x)] \le{} 1/b$
- THE definition of a universal hash function
- not true with MD5, since it's deterministic function
- a heuristic analysis assuming a good hash function
	
Reasoning:

- $E[E_i]$ = $E[f_x + \sum_{y\neq{}x} 1_y * f_y]$
- where $1_y = 1$ if $h_i(x) = h_i(y)$ or $0$ o.w.
- $= f_x + \sum_{y\neq{}x}E[1_y]*f_y$
- $= f_x + \frac{1}{b} * \sum_{y\neq{}x}f_y$
- $\le{} f_x + \frac{n}{b}$
- Therefore, let $b= 1/\epsilon{}$, relaxed condition holds


		


	