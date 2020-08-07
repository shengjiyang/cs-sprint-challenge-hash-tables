import numpy as np

def has_negatives(a):
    d = {}
    for i in a:
        if a.count(-i) > 0:
            d[i] = i

    if np.where(np.array(a) < 0) == np.array([]):
        return []

    else:
        return [i for i in d if i > 0]


if __name__ == "__main__":
    print(has_negatives([1,2,3]))
    print(has_negatives([1,2,3,-4]))
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

    # a = list(range(5000000))
    # a += [-1,-2,-3]

    # print(has_negatives(a))