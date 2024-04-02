f = open("test1.txt", "r")

def combinations(depth, start, n, nums, answer):
    if depth == n:
        print(' '.join(map(str, answer)))
        return
    for i in range(start, len(nums)):
        answer.append(nums[i])
        combinations(depth+1, i+1, n, nums, answer)
        answer.pop()

line = list(map(int, f.readline().split()))

while line[0] != 0:
    k = line[0]
    nums = line[1:]
    answer = []
    combinations(0, 0, 6, nums, answer)
    line = list(map(int, f.readline().split()))
    if line[0] == 0:
        break
    else:
        print()
