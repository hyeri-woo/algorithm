# import sys
# input = sys.stdin.readline
f = open("test2.txt")
input = f.readline
a, b = map(int, input().split())

def get_count(num):
    sum = num
    for i in range(1, 99):
        if num // (2**i) == 0:
            break
        sum += (num // (2**i)) * (2**(i-1))
    return sum

print(get_count(b) - get_count(a-1))