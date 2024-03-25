f = open('test2.txt', 'r')
n, m = map(int, f.readline().split())
numbers = list(f.readline().split())
numbers.sort()
answer = []

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    overlap = 0
    for i in range(n):
        if overlap != numbers[i]:
            answer.append(numbers[i])
            overlap = numbers[i]
            solve(depth+1, n, m)
            answer.pop()

solve(0, n, m)
f.close()