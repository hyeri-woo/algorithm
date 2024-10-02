# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline

n = int(input())
cards = sorted(list(map(int, input().split())))

m = int(input())
numbers = list(map(int, input().split()))

def search(num):
    s, e = 0, n -1

    while s <= e:
        mid = (s + e) // 2
        if cards[mid] == num:
            return True
        elif cards[mid] > num:
            e = mid - 1
        else:
            s = mid + 1
    return False

answer = []
for i in numbers:
    if search(i):
        answer.append(1)
    else:
        answer.append(0)
print(*answer)