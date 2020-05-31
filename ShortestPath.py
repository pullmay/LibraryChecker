# wrong_dijkstra_killer_00 で TLE する -> 下のコードで通った

import sys
input = sys.stdin.readline

# TIL code
# def dijkstra(s, n): # (始点, ノード数)
#     dist = [INF] * n
#     # prev = [-1] * n
#     hq = [(0, s)] # (distance, node)
#     dist[s] = 0
#     seen = [False] * n # ノードが確定済みかどうか
#     while hq:
#         v = heappop(hq)[1] # ノードを pop する
#         seen[v] = True
#         for to, cost in adj[v]: # ノード v に隣接しているノードに対して
#             if seen[to] == False and dist[v] + cost < dist[to]:
#                 dist[to] = dist[v] + cost
#                 prev[to] = v
#                 heappush(hq, (dist[to], to))
#     return dist

def dijkstra(s, n):
    d = [INF] * n
    d[s] = 0
    seen = [False] * n
    seen[s] = True
    hq = []
    for e in adj[s]: # 始点と隣接している頂点を queue に入れる
        heappush(hq, e)
    while hq:
        u, v, p = heappop(hq)
        if seen[v]:
            continue
        d[v] = u
        seen[v] = True
        prev[v] = p
        for e in adj[v]:
            if not seen[e[1]]:
                heappush(hq, [e[0] + d[v], e[1], v])
    return d

# 入力
n, m, s, t = map(int, input().split())
adj = [[] for _ in range(n)]
prev = [-1] * n
for i in range(m):
    a, b, c = map(int, input().split())
    # adj[a].append((b, c))
    adj[a].append([c, b, a])

from heapq import heappush, heappop
INF = float('inf')

d = dijkstra(s, n)

# 経路が存在しない場合
if d[t] == INF:
    print(-1)
    sys.exit()

# 経路復元
path = []
cur = t
while cur != s:
    past = prev[cur]
    path.append([past, cur])
    cur = past

# 始点からにするために逆順にする
path = path[::-1]

print(d[t], len(path)) # 距離, 経由する辺の数
for p in path:
    print(*p)