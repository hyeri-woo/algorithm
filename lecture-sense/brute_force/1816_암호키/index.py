# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline

# 입력받은 수가 적절한 암호키인지 확인하는 함수
def is_valid_secret_key(num):
    for i in range(2, 1_000_001):
        if num % i == 0:
            return False
    return True

# 입력
TC = int(input())
numbers = [int(input()) for _ in range(TC)]

# 문제 풀이 및 출력
for num in numbers:
    if is_valid_secret_key(num):
        print("YES")
    else:
        print("NO")