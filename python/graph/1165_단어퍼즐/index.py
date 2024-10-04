import sys
import heapq
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n = 5
board = [list(input().split()) for _ in range(n)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

result = set()
    
def go_one_direction(y, x, d, word, result):
    if y < 0 or y >= n or x < 0 or x >= n:
        return
    result.add(word)
    ey, ex = d
    ny, nx = y + ey, x + ex 
    if 0 <= ny < n and 0 <= nx < n:
        go_one_direction(y-1, x, d, word+board[y-1][x], result)

for y in range(n):
    for x in range(n):
        for d in direction:
            go_one_direction(y, x, d, board[y][x], result)

print(result)