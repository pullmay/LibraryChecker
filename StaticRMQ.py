import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

# 初期化
def init(lst):
    # 葉に要素を追加
    for i in range(n):
        seg[m - 1 + i] = lst[i]
    # 構築
    for i in range(m - 2, -1, -1):
        seg[i] = min(seg[2 * i + 1], seg[2 * i + 2])

# クエリの処理
# 半開区間 [l, r) における数列の最小値を返す
def query(a, b, k, l, r):
    if r <= a or b <= l: # 交差してる?
        return MAX
    elif a <= l and r <= b: # 完全に含む?
        return seg[k]
    else:
        vl = query(a, b, k * 2 + 1, l, (l + r) // 2)
        vr = query(a, b, k * 2 + 2, (l + r) // 2, r)
        return min(vl, vr)

# 入力
n, q = map(int, input().split())
A = list(map(int, input().split()))

# 完全二分木の構築
MAX = float('inf')
m = 2 ** (n - 1).bit_length() # n 以上の最小の2のべき乗
seg = [MAX] * (2 * m - 1) # 配列の要素数は 2 * m - 1

init(A) # セグメント木の構築

for i in range(q):
    l, r = map(int, input().split())
    res = query(l, r, 0, 0, m)
    print(res)