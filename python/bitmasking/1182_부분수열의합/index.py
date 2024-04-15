f = open('test1.txt', 'r')
n, s = map(int, f.readline().split())
nums = list(map(int, f.readline().split()))
answer = 0

masks = [ 1 << i for i in range(n)]
for i in range(1 << n):
    subset = [ss for ss, mask in zip(nums, masks) if mask & i]
    if len(subset) > 0 and sum(subset) == s:
        answer += 1

print(answer)