# import sys
# input = sys.stdin.readline
f = open("test2.txt")
input = f.readline

# 입력 
N = int(input())

# 문제 풀이
# 제곱수의 합 = 백색이 위로 놓여있는 깃발의 수
answer = int(N ** 0.5)

# 출력
print(answer)