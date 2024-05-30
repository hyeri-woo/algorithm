import sys
f = open('test7.txt')
input = f.readline
# input = sys.stdin.readline
n, m, h = map(int, input().split())
board = [[False] * n for _ in range(h)]

# i번째 줄이 i번째로 도착하는지 판단
def check_all_match_ladder():
    for start in range(n):
        now = start
        for j in range(h):
            if board[j][now]:   # 가로선이 오른쪽에 존재한다면
                now += 1        # 오른쪽 이동
            elif now > 0 and board[j][now - 1]:     # 가로선이 왼쪽에 존재한다면
                now -= 1                            # 왼쪽 이동
        if now != start: # 시작 위치로 안돌아았으면
            return False
    return True


def dfs(count, x, y):
    global answer
    # 조건 탐색 후 종료 또는 진행
    if check_all_match_ladder():    # 조건 만족하면 최소값 업데이트 후 종료
        answer = min(answer, count)
        return
    elif count == 3 or answer <= count: # 횟수가 3 넘어가거나 최소값 넘어가면 종료
        return
    
    for i in range(x, h):   # 행
        if i == x:  # 행이 변경되기 전에는 지금 탐색 중인 열부터
            now = y
        else:       # 행이 변경될 경우 가로선 처음부터 탐색
            now = 0
        
        for j in range(now, n - 1): # 열
            if not board[i][j] and not board[i][j+1]:   # 오른쪽에 사다리가 존재하지 않는 경우
                if j > 0 and board[i][j - 1]:           # 왼쪽에 사다리가 존재하는 경우는 패스
                    continue
                board[i][j] = True
                dfs(count + 1, i, j+2)
                board[i][j] = False

# 사다리가 있는 곳 입력
for _ in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = True  

answer = 4
dfs(0, 0, 0)
print(answer if answer < 4 else -1)
