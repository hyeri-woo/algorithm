# import sys
# input = sys.stdin.readline
f = open("test4.txt")
input = f.readline
n = int(input())
interview = [list(map(int, input().split())) for _ in range(n)]

answer = -1 * float('inf')

def recur(idx, price):
    global answer
    if idx == n:
        answer = max(answer, price)
        return
    if idx > n:
        return
    # 상담을 한다면
    recur(idx + interview[idx][0], price + interview[idx][1])
    # 상담을 안한다면
    recur(idx + 1, price)

recur(0, 0)

print(answer)