N = int(input())
nums = list(map(int, input.split()))

points = [0, 0]
player = 1

i, j = 0, n-1
while i <= j:
    if nums[i] < nums[j]:
        points[player] += nums[j]
        j -= 1
    else:
        points[player] += nums[i]
        i += 1
    
    player = 1 - player

print(points[1], points[0])