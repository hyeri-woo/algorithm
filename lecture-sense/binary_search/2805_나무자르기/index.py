# import sys
# input = sys.stdin.readline
f = open("test2.txt")
input = f.readline
n, m = map(int, input().split())
trees = sorted(list(map(int, input().split())))

min_tree = float('inf')
answer = 0
s, e = 0, max(trees)
while s <= e:
    mid = (s + e) // 2
    sum_tree = sum(max(t - mid, 0) for t in trees)
    if sum_tree >= m:
        if min_tree > sum_tree:
            min_tree = sum_tree
            answer = mid
        s = mid + 1
    else:
        e = mid - 1

print(answer)