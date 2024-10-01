import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n = int(input())
mp, mf, ms, mv = map(int, input().split())
nutrients = [list(map(int, input().split())) for _ in range(n)]

answer_idx = []
answer = float('inf')

def recur(idx, p, f, s, v, c, length):
    global answer_idx, answer
    # 영양소 조건이 만족되면 더 이상 탐색하지 않고 종료
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if answer > c:
            answer = c
            answer_idx = idx[:-1]
        return
    # 재료를 다 확인한 경우 종료
    if length == n:
        return

    new_idx = idx[-1]
    _p, _f, _s, _v, _c = nutrients[new_idx]
    # 현재 재료를 선택하는 경우
    recur(idx + [new_idx + 1], p + _p, f + _f, s + _s, v + _v, c + _c, length+1)
    # 현재 재료를 선택하지 않는 경우
    recur(idx[:-1] + [new_idx + 1], p, f, s, v, c, length+1)
    
recur([0], 0, 0, 0, 0, 0, length=0)

if answer == float('inf'):
    print(-1)
    sys.exit()

answer_idx = [i + 1 for i in answer_idx]
print(answer)
print(*answer_idx)

# answer_idx = []
# answer = float('inf')

# def recur(idx, p, f, s, v, c, selected):
#     global answer, answer_idx
    
#     # 영양소 조건이 만족되면 더 이상 탐색하지 않고 종료
#     if p >= mp and f >= mf and s >= ms and v >= mv:
#         if c < answer:
#             answer = c
#             answer_idx = selected[:]
#         return
    
#     # 재료를 다 확인한 경우 종료
#     if idx == n:
#         return
    
#     # 현재 재료를 선택하는 경우
#     recur(idx + 1, p + nutrients[idx][0], f + nutrients[idx][1], s + nutrients[idx][2], v + nutrients[idx][3], c + nutrients[idx][4], selected + [idx + 1])
    
#     # 현재 재료를 선택하지 않는 경우
#     recur(idx + 1, p, f, s, v, c, selected)

# recur(0, 0, 0, 0, 0, [])

# if answer == float('inf'):
#     print(-1)
# else:
#     print(answer)
#     print(*answer_idx)