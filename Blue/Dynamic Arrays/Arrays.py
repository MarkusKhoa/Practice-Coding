na, nb = map(int, input().split())
#k: segments of arrA, m: segments of arrB
k, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

if arr_a[k-1] < arr_b[nb-m]:
  print('YES')
else:
  print('NO')