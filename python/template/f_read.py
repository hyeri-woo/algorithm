from itertools import permutations

f = open('test3.txt', 'r')
n, m = map(int, f.readline().split())
numbers = list(f.readline().split())

answer = []
for i in permutations(numbers, m):
    answer.append(' '.join(i))
answer.sort()
print('\n'.join(answer))

f.close()