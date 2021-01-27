n, a, b = map(int, input().split())
h = list(map(int, input().split()))

h = sorted(h, reverse=False)
#Vesya
count = 0
ans = h[b-1]
while ans < h[n-a]:
  ans += 1
  count += 1
  
print(count)