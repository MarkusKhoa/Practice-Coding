def makeSet():
      global ranks, parents, count
  ranks = [0 for _ in range(MAX+5)]
  count = [1 for _ in range(MAX+5)]
  parents = [i for i in range(MAX+5)]

def findSet(u):
  if parents[u] != u:
    parents[u] = findSet(parents[u])
  return parents[u]

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return
  if ranks[up] > ranks[vp]:
    parents[vp] = up
    count[up] += count[vp]
  elif ranks[up] < ranks[vp]:
    parents[up] = vp
    count[vp] += count[up]
  else:
    parents[up] = vp
    ranks[vp] += 1
    count[vp]+= count[up]

T = int(input())
for _ in range(T):
  global ranks, parents, count
  MAX = 30000
  parents = []
  ranks = []
  count = []
  n, m = map(int, input().split())
  makeSet()
  for j in range(m):
    a, b = map(int, input().split())
    unionSet(a, b)
  res = max(count)
  print(res)