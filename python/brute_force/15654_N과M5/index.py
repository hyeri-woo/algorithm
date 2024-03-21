f = open('test1.txt', 'r')
n, m = map(int, f.readline().split())
numbers = list(f.readline().split())
numbers.sort()
visited = [False] * n
answer = []

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(numbers[i])
            solve(depth+1, n, m)
            answer.pop()
            visited[i] = False

solve(0, n, m)
f.close()