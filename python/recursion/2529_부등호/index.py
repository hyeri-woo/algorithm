f = open('test2.txt')
N = int(f.readline())
S = list(map(str, f.readline().split()))
result = []
visited = [False] * 10
answer = []

def permutation(depth, m, numbers, result, visited):
    if depth == m:
        answer.append(''.join(map(str, result)))
        return
    for i in range(len(numbers)):
        if not visited[i]:
            if len(result) == 0 or (S[depth-1] == '<' and result[-1] < i) or (S[depth-1] == '>' and result[-1] > i):
                visited[i] = True
                result.append(numbers[i])
                permutation(depth+1, m, numbers, result, visited)
                result.pop()
                visited[i] = False

permutation(0, N+1, range(10), result, visited)
print(answer[-1])
print(answer[0])