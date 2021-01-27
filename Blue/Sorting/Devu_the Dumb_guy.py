n, x = map(int, input().split())
c = list(map(int, input().split()))

c = sorted(c, reverse = False)
min_times = 0
for i in range(len(c)):
  min_times += c[i]*x
  if x > 1:
    x -= 1
    
print(min_times)