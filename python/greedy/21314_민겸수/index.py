import sys
# input = sys.stdin.readline
f = open('test2.txt')
input = f.readline
numbers = input().strip()
max = ''
min = ''
m = 0

for n in numbers:
    if n == 'M':
        m += 1 
    elif n == 'K':
        if m:  # m 후에 k가 연속해서 나온 경우
            min += str(10 ** m + 5) # 최솟값의 경우 5를 더함
            max += str(5 * (10 ** m)) # 최댓값의 경우 5를 곱함
        else: # 만약 k만 두번 이상 연속된 경우
            min += "5"
            max += "5"
        m = 0

if m: # k없이 m들로 문자열이 끝난 경우
    min += str(10 ** (m-1))
    while m:
        max += "1"
        m -= 1

print(max)
print(min)
