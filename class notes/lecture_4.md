- dissimilarity
- nearest neighbo
- k-dtrees
	- regions to check => expotential to dimension  
	- "curse of dimensinoality"
	
### Issue: 

the nature representation of data is of a very high dimension

### Goal: 

compress to small number of dimensions, with little loss. (similar to boom filter, preseving membership relationship with false positive)

### Solution:

1. represent data in high dimensions
2. map to low dimensions
3. solve NN (Nearest Neighbor) in low dimensions
	
### Role Model:

- Choose hash function $h$
- map each object to $h(x)$ mod 2

### Properties:

- $x=y\Rightarrow{}h(x)=h(y)$
- $x\neq{}y\Rightarrow{}P(h(x)=h(y))=0.5$

Repeat the process $log_2(1/\delta)$ (i.e. independent trials)

- $x=y\Rightarrow{}h(x)=h(y)$
- $x\neq{}y\Rightarrow{}P(h(x)=h(y))=0.5^{log_2(1/\delta)}=\delta$
- distinct when $x\neq{}y$ with prabability ($1-\delta$)

Change the number of buckets (2 in this example) will have similar results.

> Distance will be focused on L2 distance.

### Random Projections:

- choose a "random vector" $r_1, ..., r_k$
- map each point $x\in{}R^k$ to $<x,r>=\sum_{j=1}^{j=k}x_jr_j=f_r(x)$ (dot production)

### Gaussian distribution ($N(\mu, \sigma^2)$)

- $X_1\sim{}N(\mu_1, \sigma_1^2), X_2\sim{}N(\mu_2, \sigma_2^2)$
- $\Rightarrow{}X_1+X_2\sim{}N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)$
- $f_r(x) - f_r(y) = f_r(x-y)$ in which each $r_i$ taken by normal distribution
- $r_i(x_i-y_i)$ term has mean 0, variance $=1 * (x_i-y_i)^2$
- $\Rightarrow{}f_r(x) - f_r(y)\sim{}N(0, \sum_j(x_j-y_j)^2)$
- Recall, if $EX=0, Var(X)=E(X^2)$
- $\Rightarrow{} E((f_r(x) - f_r(y))^2)=\sum_j(x_j-y_j)^2=||x-y||_2^2$
- note the $Var((f_r(x) - f_r(y))^2)$, but can average $d$ independant copies to reduce variance
- Theriotical results:
- $d=O(\frac{lgn}{\epsilon^2})$ in which n is number of pts

## JL Dimensionality Reduction

### Input:

n points in $R^k$, k can be large

### Algorithm: 

- choose a matrix $A_{d\times{}k}$, $Ax$ change it $x$ to a vector of dimension $d$

### Claim:

- L2 distance 
- ||f_A(x)-f_A(y)||_2^2 
- = ||Ax/r_d - Ay/r_d||_2^2 
- = 1/r_d||A(x-y)||_2^2
- $\Rightarrow{}$ Row $i$ = output of the $i^{th}$ independant trial

### Real Number?

- $A$ can be chosen to be random +/- 1
- $A$ design: Fast JL Transform

## Jaccad Similarity

- $A, B\subseteq{}U$
- $J(A,b)=\frac{|A\cap{}B|}{|A\cup{}B|}$

### Minhash 

- choose random permutation of $U$ (usual implementation: hash function)
- map each set $S\subseteq{}U$ to $argmin_x\Pi(x)$, $\Pi$ is a random permutation

Logpoint:

- all relative ordering of A\cupB equally likely
- Prob(minhash A = minhash B) = J(A,B)
- map vector to real number, average to 






