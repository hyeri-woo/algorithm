# import sys
# input = sys.stdin.readline
f = open("test3.txt")
input = f.readline
n = int(input())
ingre = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')

def recur(idx, sour, bitter, use):
    global answer
    if idx == n:
        if use == 0: # 아무 재료도 사용하지 않았다면
            return
        answer = min(answer, abs(sour - bitter))
        return
    
    recur(idx+1, sour * ingre[idx][0], bitter + ingre[idx][1], use+1)
    recur(idx+1, sour, bitter, use)


recur(0, 1, 0, 0)

print(answer)