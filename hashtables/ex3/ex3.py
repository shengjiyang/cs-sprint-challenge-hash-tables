import itertools

def intersection(arrays):
    d = {}
    for i in range(len(arrays)):
        d[i] = arrays[i]

    a = list(itertools.chain.from_iterable(arrays))

    d2 = {}
    for i in d[i]:
        d2[i] = a.count(i)

    return [i for i in d2 if d2[i] > 1]

if __name__ == "__main__":

    arrays = []
    
    # arrays.append([1, 2, 3])
    # arrays.append([1, 4, 5])
    # arrays.append([1, 6, 7])

    # arrays = [[1], [1]]

    # arrays = [[1, 2], [1]]

    arrays.append([1, 2, 3])
    arrays.append([1, 4, 5, 3])
    arrays.append([1, 6, 7, 3])

    print(intersection(arrays))

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))
