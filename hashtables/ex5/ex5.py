# hashtables/ex5/ex5.py

from collections import defaultdict

def finder(files, queries):
    d = {}
    for f in files:
        for q in queries:
            if f[-len(q):] == q:
                d[q] = f

    return [i for i in list(d.values())]


def finder(files, queries):
    d = defaultdict(list)
    for f, q in zip(files, queries):
        if f[-len(q):] == q:
            d[f].append(q)

    return [i for i in d]

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
    print(finder(files, queries=["qux"]))

    # files = []

    # for i in range(500000):
    #     files.append(f"/dir{i}/file{i}")

    # for i in range(500000):
    #     files.append(f"/dir{i}/dirb{i}/file{i}")

    # queries = []

    # for i in range(1000000):
    #     queries.append(f"nofile{i}")

    # queries += [
    #     "file3490",
    #     "file256",
    #     "file999999",
    #     "file8192"
    # ]

    # print(finder(files, queries))