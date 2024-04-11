f = open("test1.txt", "r")
N = int(f.readline())
board = [list(map(int, f.readline().split())) for _ in range(N)]
visited = [False for _ in range(N)]
INF = 2147000000
answer = INF

def solve(L,idx):
    global answer
    if L == N//2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B +=board[i][j]
        answer = min(answer, abs(A-B))
        return
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            solve(L+1,i+1)
            visited[i] = False
            
solve(0,0)
print(answer)
# 조합
# sum_stat = [sum(i) + sum(j) for i, j in zip(team, zip(*team))]
# allstat = sum(sum_stat) // 2
# result = float('inf')
# for l in combinations(sum_stat, n//2):
#     result = min(result, abs(allstat - sum(l)))
# print(result)


