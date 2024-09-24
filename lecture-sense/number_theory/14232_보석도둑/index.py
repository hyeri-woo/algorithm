# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline

# 입력
k = int(input())

# 문제 풀이
# 약수 빠르게 구하기: sqrt(k)까지만 찾기
# 소인수분해: 에라토스테네스의 체
answer = []
for i in range(2, int(k ** 0.5) + 1):
    while k % i == 0:
        answer.append(i)
        k //= i

if k != 1:
    answer.append(k)

# 출력
print(len(answer))
print(*answer)