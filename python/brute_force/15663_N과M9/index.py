f = open('test3.txt', 'r')
n, m = map(int, f.readline().split())
numbers = list(f.readline().split())
numbers.sort()
answer = []
visited = [False] * n

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != numbers[i]:
            visited[i] = True
            answer.append(numbers[i])
            overlap = numbers[i]
            solve(depth+1, n, m)
            visited[i] = False
            answer.pop()

solve(0, n, m)
f.close()