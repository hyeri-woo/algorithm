# import sys
# input = sys.stdin.readline
f = open("test2.txt")
input = f.readline
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)

answer = 0
for i in range(n-1):
    a, b = numbers[i], numbers[i+1]
    # 최대 공약수가 1이라면 패스
    if get_gcd(a, b) == 1:
        continue
    # 최대 공약수가 1이 아니라면 
    for j in range(a+1, b):
        if get_gcd(a, j) == 1 and get_gcd(j, b) == 1:
            answer += 1
            break
        if j == b - 1:
            answer += 2

print(answer)