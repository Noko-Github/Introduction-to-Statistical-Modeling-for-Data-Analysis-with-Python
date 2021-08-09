import math

def poisson(_lambda, k):
    k = int(k)
    prob = (_lambda ** k) * (math.exp(-1 * _lambda)) / math.factorial(k)
    
    return prob
