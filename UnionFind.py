  
class UnionFind:
	def __init__(self, n):
		self.n = n
		self.parents = [i for i in range(n)] # parents
		self.rank = [1] * n # height of tree
		self.size = [1] * n # size[i] ->頂点 i を root とする group のサイズ

	# 木の根を返す
	def find(self, x):
		if self.parents[x] == x:
			return x
		else:
			self.parents[x] = self.find(self.parents[x])
			return self.parents[x]

	# xとyの属する集合を併合する
	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if x == y:
			return
		if self.rank[x] < self.rank[y]:
			self.parents[x] = y
			self.size[y] += self.size[x] 
		else:
			self.parents[y] = x
			self.size[x] += self.size[y]
			if self.rank[x] == self.rank[y]:
				self.rank[x] += 1

	# xとyが同じグループに属しているかを判定する
	def same(self, x, y):
		return self.find(x) == self.find(y)


n, q = map(int, input().split())
uf = UnionFind(n)
for i in range(q):
    t, u, v = map(int, input().split())
    if t == 0:
        uf.union(u, v)
    elif t == 1:
        if uf.same(u, v):
            print(1)
        else:
            print(0)
    