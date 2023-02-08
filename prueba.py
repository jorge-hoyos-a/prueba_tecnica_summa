import numpy as np
from itertools import combinations

N=9 
# your set of numbers
nums = np.array([2,7,11,15])

# prepare list of all possible combinations of two numbers using built-in generator
combs = [i for i in combinations(nums,2)]

# sum up these two numbers
sums = np.sum(combs, axis=1)

# find index of wanted summed of the two numbers in sums
good_comb = np.where(sums==N)[0][0]

# search the indices in your original list, knowing index in combs
indices_sum_to_N = [np.where(nums==i)[0][0] for i in combs[good_comb]]
print(indices_sum_to_N)