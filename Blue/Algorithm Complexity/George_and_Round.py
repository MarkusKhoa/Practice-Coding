N, M = map(int, input().split())
i = j = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))
while i < N and j < M:
    if a[i] <= b[j]:
        i += 1
        j += 1
    else:
        j += 1

print(N-i)