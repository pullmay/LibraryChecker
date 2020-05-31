from collections import defaultdict
q = int(input())
d = defaultdict(int)
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        k, v = query[1], query[2]
        d[k] = v
    else:
        k = query[1]
        print(d[k])
