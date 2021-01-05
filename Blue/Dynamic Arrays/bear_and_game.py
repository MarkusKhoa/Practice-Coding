def minutes(lst, n):
      res = 15
  end = len(lst)-1
  if n == 1:
    if lst[0] <= 15:
        return lst[0]+15
  if lst[0] > 15:
    return res
  for i in range(len(lst)-1):
    if (lst[i] + 15 < lst[i+1]):
      res = lst[i] + 15
      if res > 90:
        res = 90
      break
        
    elif lst[end] + 15 <= 90:
        res = lst[end] + 15
    else:
        res = 90
  
  return res
  
n = int(input())
lst = list(map(int, input().split()))
print(minutes(lst,n))