f = open("test1.txt", "r")
n = int(f.readline())
numbers = [i for i in range(1, n+1)]
answer = []
visited = [False] * n

def solve(depth, n):
    if depth == n:
        print(' '.join(map(str, answer)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(numbers[i])
            solve(depth+1, n)
            answer.pop()
            visited[i] = False

solve(0, n)