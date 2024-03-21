f = open('test1.txt', 'r')
n, m = map(int, f.readline().split())
numbers = list(f.readline().split())
numbers.sort()
answer = []

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(n):
        if len(answer) == 0 or answer[-1] <= numbers[i]:
            answer.append(numbers[i])
            solve(depth+1, n, m)
            answer.pop()

solve(0, n, m)
f.close()