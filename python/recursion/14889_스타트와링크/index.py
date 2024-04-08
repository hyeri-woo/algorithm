from itertools import combinations

f = open("test1.txt", "r")
n = int(f.readline())
team = [list(map(int, f.readline().split())) for _ in range(n)]
sum_stat = [sum(i) + sum(j) for i, j in zip(team, zip(*team))]
allstat = sum(sum_stat) // 2
result = float('inf')
for l in combinations(sum_stat, n//2):
    result = min(result, abs(allstat - sum(l)))
print(result)
