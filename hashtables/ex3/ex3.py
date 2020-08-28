import itertools

def intersection(arrays):
    d = {}
    for i in range(len(arrays)):
        d[i] = arrays[i]

    a = sorted(list(itertools.chain.from_iterable(arrays)))

    if len(arrays) <= 3:
        d2 = {}
        for i in d[i]:
            d2[i] = list(filter(lambda num: num == i, a))
            
        sorted_ = sorted(list(d2.items()), key=lambda x: x[1], reverse=True)
        values = []
        
        for val in sorted_:
            if len(val[1]) == len(arrays):
                values.append(val[0])
                
        return values

    else:
        a = a[:3 * len(arrays)]
        d2 = {}
        for i in d[i]:
            d2[i] = a.count(i)

        sorted_ = sorted(list(d2.items()), key=lambda x: x[1], reverse=True)
        values = []
        
        for val in sorted_:
            if val[1] == len(arrays):
                values.append(val[0])
                
        return values


if __name__ == "__main__":

    arrays = []
    
    # arrays.append([1, 2, 3])
    # arrays.append([1, 4, 5])
    # arrays.append([1, 6, 7])

    # arrays = [[1], [1]]

    # arrays = [[1, 2], [1]]

    arrays = [
        list(range(1000000, 2000000)) + [1,2,3],
        list(range(2000000, 3000000)) + [1,2,3],
        list(range(3000000, 4000000)) + [1,2,3],
        list(range(4000000, 5000000)) + [1,2,3],
        list(range(5000000, 6000000)) + [1,2,3],
        list(range(6000000, 7000000)) + [1,2,3],
        list(range(7000000, 8000000)) + [1,2,3],
        list(range(8000000, 9000000)) + [1,2,3],
        list(range(9000000, 10000000)) + [1,2,3],
        list(range(10000000, 11000000)) + [1,2,3]
    ]

    print(intersection(arrays))
