import sys
import math
input = sys.stdin.readline
f = open("test7.txt")
n, m = map(int, f.readline().split())
graph = [list(map(int, f.readline().strip())) for _ in range(n)]

def is_square_number(number):
    if math.sqrt(number) % 1 == 0:
        return True
    return False

answer = -1

for i in range(n):
    for j in range(m):
        for diff_x in range(-n, n):
            for diff_y in range(-m, m):
                number = ''
                x, y = i, j
                if diff_x == 0 and diff_y == 0:
                    continue
                while 0 <= x < n and 0 <= y < m:
                    number += str(graph[x][y])
                    if is_square_number(int(number)):
                        answer = max(answer, int(number))
                    x += diff_x
                    y += diff_y

print(answer)