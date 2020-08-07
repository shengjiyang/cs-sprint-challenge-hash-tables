# hashtables/ex5/ex5.py

def finder(files, queries):
    d = {}
    for f in files:
        for q in queries:
            if f[-len(q):] == q:
                d[q] = f

    return [i for i in list(d.values())]



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
