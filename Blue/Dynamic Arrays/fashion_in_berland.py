def check_buttons(lst, n):
      count = 0
  flag = False
  if n == 1:
    if lst[0] == 1:
      flag = True
    else:
      return flag
  for i in range(0, n, 1):
    if lst[i] == 0:
      count += 1
  
  if count == 1:
    flag = True
    
  return flag

n = int(input())
lst = list(map(int, input().split()))

if check_buttons(lst, n) == True:
    print('YES')
else:
    print('NO')