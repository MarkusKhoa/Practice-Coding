MAX = 1001

visited = [False for i in range(MAX)]
graph = [[] for _ in range(MAX)]
path = [0 for i in range(MAX)]
result = []

def DFS(src):
  for i in range(V):
    visited[i] = False
    path[i] = -1
  s = []
  visited[src] = True
  s.append(src)
  while len(s) > 0:
    u = s.pop()
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        s.append(v)
        path[v] = u
        
def printPath(s, f, path):
  b = []
  if f == s:
    return
  if path[f] == -1:
    return
  while True:
    b.append(f)
    f = path[f]
    
    if f == s:
      b.append(s)
      break
  result.append((len(b)-1, b[0]))
  
  
hasGirl = []
noGirl = []
N = int(input())
V = N
E = N-1
for i in range(N-1):
  u, v = map(int, input().split())
  u, v = u-1, v-1
  graph[u].append(v)
  graph[v].append(u)
Q = int(input())
s = 0
DFS(s)

for i in range(Q):
  x = int(input())
  hasGirl.append(x)
  
  f = hasGirl[i] - 1
  printPath(s, f, path)
  
result.sort()
order, index = result[0]
print(index + 1)