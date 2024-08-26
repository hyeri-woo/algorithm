# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline

# 입력
N = int(input())

# 문제 풀이
answer = 0
for nam in range(1, N):
    for young in range(1, N - nam):
        taek =  N - nam - young
        if nam - young >= 2 and taek % 2 == 0:
            answer += 1
# 출력
print(answer)
