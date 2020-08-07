# hashtables/ex1/ex1.py

from itertools import combinations
import numpy as np

def get_indices_of_item_weights(weights, length, limit):
    pairs = [pair for pair in combinations(weights, 2)]
    d = {}
    for pair in pairs:
        d[pair] = sum(pair)

    for pair in d:
        if d[pair] == limit:
            if pair[0] != pair[1]:
                return [weights.index(pair[1]), weights.index(pair[0])]
            else:
                return [np.where(np.array(pair) == pair[0])[0][1], np.where(np.array(pair) == pair[0])[0][0]]

    return None
