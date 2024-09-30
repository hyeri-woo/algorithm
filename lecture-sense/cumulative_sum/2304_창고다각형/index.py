# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n = int(input())
pillars = [0] * 1001

for _ in range(n):
    l, h = map(int, input().split())
    pillars[l] = h

max_height = max(pillars)
max_index = pillars.index(max_height)

area = 0
current_height = 0
# 왼쪽에서부터 최대 기둥의 면적 계산
for i in range(max_index+1):
    current_height = max(current_height, pillars[i])
    area += current_height

# 오른쪽에서부터 마지막 기둥까지의 면적 계산
current_height = 0
for i in range(1000, max_index, -1):
    current_height = max(current_height, pillars[i])
    area += current_height

print(area)