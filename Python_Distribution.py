import numpy as np
from scipy.stats import binom, poisson, norm, uniform, expon, beta, hypergeom
print("DISCRETE ")
# Example for a binomial distribution
n = 10
p = 0.5
k = 5
P = binom.pmf(k, n, p)
print(f"Binomial distribution: P(X = {k}) = {P}")
print()
# Example for a Poisson distribution
mu = 5
k = 3
P = poisson.pmf(k, mu)
print(f"Poisson distribution: P(X = {k}) = {P}")
print()

# Example for a hypergeometric distribution
N = 100
M = 20
n = 10
k = 4
P = hypergeom.pmf(k, N, M, n)
print(f"Hypergeometric distribution: P(X = {k}) = {P}")
print()
print("CONTINUOUS")
# Example for a normal distribution
mu = 10
sigma = 2
x = 12
P = norm.cdf(x, mu, sigma)
print(f"Normal distribution: P(X <= {x}) = {P}")
print()
# Example for a uniform distribution
a = 0
b = 10
x = 5
P = uniform.cdf(x, a, b)
print(f"Uniform distribution: P(X <= {x}) = {P}")
print()
# Example for an exponential distribution
lambd = 0.5
x = 2
P = expon.cdf(x, scale=1/lambd)
print(f"Exponential distribution: P(X <= {x}) = {P}")
print()