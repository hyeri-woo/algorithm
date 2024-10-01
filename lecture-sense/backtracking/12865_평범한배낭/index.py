# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

answer = -1 * float('inf')

def recur(idx, weight, value):
    global answer
    if weight > k:
        return
    if idx == n:
        answer = max(answer, value)
        return

    # 배낭을 가지고 간다면
    recur(idx + 1, weight + items[idx][0], value + items[idx][1])

    # 배낭을 안 가지고 간다면
    recur(idx + 1, weight, value)

recur(0, 0, 0)
print(answer)