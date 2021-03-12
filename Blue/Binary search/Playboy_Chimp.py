def search_right(l, r, M, arr):
      ans = r
  while l <= r:
    mid = int((l+r)/2)
    if arr[mid] > M:
      ans = mid
      r = mid - 1
    else:
      l = mid + 1
  return ans

def search_left(l, r, M, arr):
  ans = r
  while l <= r:
    mid = int((l+r)/2)
    if arr[mid] < M:
      ans = mid
      l = mid + 1
    else:
      r = mid - 1
  return ans

N = int(input())
arrN = list(map(int, input().split()))
arrN = sorted(arrN)
Q = int(input())
arrQ = list(map(int, input().split()))

for i in range(len(arrQ)):
  posLeft = search_left(0, len(arrN)-1, arrQ[i], arrN)
  posRight = search_right(0, len(arrN)-1, arrQ[i], arrN)
  
  shorter = arrN[posLeft]
  higher = arrN[posRight]
  
  if shorter >= arrQ[i]:
    shorter = 'X'
  if higher <= arrQ[i]:
    higher = 'X'
  print(shorter, higher)