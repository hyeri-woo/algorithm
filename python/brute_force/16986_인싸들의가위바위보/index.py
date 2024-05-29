import sys
from itertools import permutations
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
N,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
p2 = list(map(int,input().split()))
p3 = list(map(int,input().split()))
jiwo = [i+1 for i in range(N)]

def dfs(py1, py2, win, index, player):
    global result
    # 지우가 우승했을 경우 result를 1로 설정 후 return
    if win[0] == K:
        result = 1
        return
    # 경희나 민호가 우승했을 경우 그냥 return
    if win[1] == K or win[2] == K:
        return
    # 지우의 플레이 횟수가 n이 됐을 경우 그냥 return
    if index[0] == N:
        return
    
    py3 =  3 - (py1+py2)
    pv1 = player[py1][index[py1]] - 1   # py1의 손동작
    pv2 = player[py2][index[py2]] - 1   # py2의 손동작
    index[py1] += 1
    index[py2] += 1
    # pv1가 이겼을 경우 
    if board[pv1][pv2] == 2 or (board[pv1][pv2] == 1 and py1 > py2): 
        win[py1] += 1
        dfs(py1, py3, win, index, player)
    # pv2가 이겼을 경우 
    elif board[pv1][pv2] == 0 or (board[pv1][pv2] == 1 and py1 < py2):
        win[py2] += 1
        dfs(py2, py3, win, index, player)

for p1 in permutations(jiwo, N):
    player = [p1,p2,p3]
    win = [0,0,0]
    index = [0,0,0]
    result = 0
    dfs(0, 1, win, index, player)
    if result == 1:
        print(1)
        break
else:
    print(0)