import numpy as np

def has_negatives(a):
    where = np.where(np.array(a) < 0)

    if len(where[0]) == 0:
        return []

    else:
        neg = []
        for i in where[0]:
            neg.append(a[i])

        pos = []
        for i in neg:
            if a.count(-1) > 0:
                pos.append(-i)

        return pos
    


if __name__ == "__main__":
    print(has_negatives([1,2,3]))
    print(has_negatives([1,2,3,-4]))
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

    a = list(range(5000000))
    a += [-1,-2,-3]

    print(has_negatives(a))