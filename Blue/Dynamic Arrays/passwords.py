f =[0]*101
worst_case = best_case = 0
n, k = map(int, input().split())
for _ in range(n):
  psw = input()
  f[len(psw)] += 1

true_psw = input()

for i in range(len(true_psw)):
  best_case += f[i]

worst_case = best_case + f[len(true_psw)] - 1

best_case += (best_case // k)*5
worst_case += (worst_case // k)*5

print(best_case+1, worst_case+1, sep = ' ')