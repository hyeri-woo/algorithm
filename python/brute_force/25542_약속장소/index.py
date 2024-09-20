import sys
# input = sys.stdin.readline
f = open('test2.txt')
input = f.readline

# 입력
n, l = map(int, input().split())
candidates = [input().strip() for _ in range(n)]

# 첫 번째 단어로 초기화
answer = list(candidates[0])

# answer과 candidate의 알파벳 차이수가 1개 이하인지 확인
def check_valid(answer, candidate):
    cnt_diff = 0
    for i in range(l):
        if candidate[i] != answer[i]:
            cnt_diff += 1
        if cnt_diff > 1:
            return False
    return True

for i in range(l):
    is_found = False
    for c in range(ord('A'), ord('Z') + 1):
        answer[i] = chr(c)
        is_valid = True
        for candidate in candidates:
            is_valid = check_valid(answer, candidate)
            if not is_valid:
                break
        if is_valid:
            is_found = True
            break
    # 원래의 문자로 복원
    if not is_found:
        answer[i] = candidates[0][i]
    
# 정답과 각 후보의 차이 개수 세기
is_valid = True
for candidate in candidates:
    is_valid = check_valid(answer, candidate)
    if not is_valid:
        break

if is_valid:
    print("".join(answer))
else:
    print("CALL FRIEND")