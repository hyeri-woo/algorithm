# import sys
# input = sys.stdin.readline
f = open("test2.txt")
input = f.readline
gcd, lcm = map(int, input().split())

def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)

divide = lcm // gcd
for i in range(1, int(divide ** 0.5) + 1):
    if divide % i != 0:
        continue
    a = i
    b = divide // i
    if get_gcd(a, b) == 1:
        answerA, answerB = a, b

print(answerA * gcd, answerB * gcd)