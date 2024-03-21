f = open('test3.txt', 'r')
n, m = map(int, f.readline().split())
numbers = list(f.readline().split())
numbers.sort()
answer = []

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(n):
        answer.append(numbers[i])
        solve(depth+1, n, m)
        answer.pop()

solve(0, n, m)
f.close()