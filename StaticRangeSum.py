from itertools import accumulate

n, q = map(int, input().split())
A = list(map(int, input().split()))

# 累積和
B = [0] + A
B = list(accumulate(B))

for i in range(q):
    l, r = map(int, input().split())
    print(B[r] - B[l])