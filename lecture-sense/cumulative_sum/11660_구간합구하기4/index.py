# import sys
# input = sys.stdin.readline
f = open("test2.txt")
input = f.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 누적합 구하기
prefix = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] + board[i-1][j-1] - prefix[i-1][j-1]

def get_sum(x1, y1, x2, y2):
    return prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]

while True:
    coord = input().strip()
    if not coord:
        break
    x1, y1, x2, y2 = map(int, coord.split())
    print(get_sum(x1, y1, x2, y2))