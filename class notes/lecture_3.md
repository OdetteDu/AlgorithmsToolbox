# Lecture 3 - Apr.6

### Simiularity Search

Problems:

- How to organize data to quickly found "similarities"?
	- within dataset
	- quickly deal with a new point
	
- How to define similarity?

Motivations, Applications:

- documents (e.g. code), web pages, de-duplication, genomic data
- collab. filtering (Amazon, Netflix)
	- how similar a person, group by things purchased, predict things to purchase
- machine learning/classification
- combining datasets (Astronomy)
- super fast labelling (ERN/LHC)
	- ~500$\cdot{}10^{14}$ proton-proton collisions
	- decide which to save in a very short time
	
### Jaccard Similarity

between sets, $S$, $T$:

- $J(S,T)=\frac{|S\cap{}T|}{|S\cup{}T|}$

For example:

- S = 2a 1b 1c 0d 0d
- T = 1a 0b 1c 1d 2d
- $J(S,T)=\frac{\sum{}min(S,T)}{\sum{}max(S,T)}$

e.g. 
- documents -> set of words -> "bag of words"
- individials -> set of people

Euclidean Dist/ L2 dist

- Points/vector $\in{} R^n$
- $D_{Eu}(X,Y)=||X-Y||_2=(\sum{}(x_i-y_i)^2)^{1/2}$
- L1 Distance $||X-Y|| = \sum{}|x_i-y_i|$
- L2 distance is rotation invariant, L1 is not, so apply L1 only when coordinates make sense

There're lots more similarity metrics

- e.g. $L_p: ||X-Y||_p=(\sum{}(x_i-y_i)^p)^{1/p}$
	- with larger p, small distances will be dwarfed
- cosine similarity
- edit distance (for strings)

### Metric Embeddings

- Given ${x_1, ... x_n}$
- Can I find ${y_1, ..., y_n}$?
- st. $D(x_i,x_j)\approx{}D'(y_i,y_j)$
- e.g. $D$ is a similarity function, and change to $D'=L_2$

### Voronoi Diagrams

- Partition of space according to closest element of a set

### Kd-Tree

- by Bentley '75, tons of variants, works for $k<20$

Idea:

- Make a balanced binary tree that partitions space
- In a way that's easily accessed
- Every edge of the tree cooresponds to a region of space

Algorithm: Given set of points

1. Pick a dimension $i$
2. $m$ = median of $i_{th}$ coodinates of points
3. Partition according to $m$, $S1$, $S2$
4. recurse on $S1$, $S2$

Variants:

- which dimmensions to pick first
- median?

How to use the data structure - add a point x

- Intuition
	- find smallest region contains y
	- go up tree asking "could the closest point lie in a region defined by the edge"

Performance:

- size: $\le$ linear to # points
- lookup time: log(# points)
	- as long as no need to check too many buckets
	- buckets to check can be exp to k




 








