import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline

def find_lego_pair(x, n, pieces):
    pieces.sort()

    left = 0
    right = n - 1
    best_pair = None

    while left < right:
        curr_sum = pieces[left] + pieces[right]
        if curr_sum == x:
            if best_pair is None or abs(pieces[right] - pieces[left]) > abs(best_pair[1] - best_pair[0]):
                best_pair = (pieces[left], pieces[right])
            left += 1
            right -= 1
        elif curr_sum < x:
            left += 1
        else:
            right -= 1
    
    if best_pair:
        return f"yes {best_pair[0]} {best_pair[1]}"
    else:
        return "danger"

while True:
    x_str = input()
    if not x_str:
        break

    x = int(x_str) * 10**7
    n = int(input())
    pieces = [int(input()) for _ in range(n)]
    print(find_lego_pair(x, n, pieces))