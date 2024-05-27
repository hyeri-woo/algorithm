import sys
from collections import deque

input = sys.stdin.readline
f = open("test1.txt")
T = int(f.readline())

# 동전을 뒤집을 수 있는 경우의 수
flip_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# 동전을 최소로 뒤집을 수 있는 수 계산
def game(coins):
    visited = [False] * 512
    visited[int(coins, 2)] = True
    queue = deque([(int(coins, 2), 0)])
    while queue:
        coin, cnt = queue.popleft()
        if coin == 0 or coin == 511:    # coin이 전부 H 이거나 T일때 count 반환
            return cnt
        for p in flip_positions:
            new = flip(list(bin(coin)[2:].zfill(9)), p)     # 이진수로 바꾼 뒤 flip
            idx = int(new, 2)
            if not visited[idx]:                            # 해당 수에 visited하지 않았을때만 
                visited[idx] = 1
                queue.append((idx, cnt + 1))
    return -1

# flip_pos대로 코인들을 뒤집기
def flip(coin, flip_pos):
    for p in flip_pos:
        coin[p] = '1' if coin[p] == '0' else '0'
    return ''.join(coin)

# 테스트 케이스 수대로 반복
for t in range(T):
    coins = []
    for _ in range(3):
        coins.extend('1' if i == 'H' else '0' for i in f.readline().split())
    print(game(''.join(coins)))