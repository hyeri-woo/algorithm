from itertools import permutations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

answer = []
for i in permutations(numbers, m):
    answer.append(' '.join(i))
answer.sort()
print('\n'.join(answer))