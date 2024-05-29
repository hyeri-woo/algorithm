import sys
input = sys.stdin.readline
f = open('test4.txt')
n, m = map(int, f.readline().split())
paper = [list(map(int, f.readline().strip())) for _ in range(n)]
max_num = pow(2, n*m)

# 0인 값을 가로로 취급하여 가로 값 전부를 더한 값 계산
def get_horizontal_sum(arr):
    sum = 0
    for i in range(n):
        partial_num = '0'
        for j in range(m):
            if arr[i][j] == 0:
                partial_num += str(paper[i][j])
            else:
                sum += int(partial_num)
                partial_num = '0'
        sum += int(partial_num)
    return sum

# 1인 값을 세로로 취급하여 세로 값 전부를 더한 값 계산
def get_vertical_sum(arr):
    sum = 0
    for i in range(m):
        partial_num = '0'
        for j in range(n):
            if arr[j][i] == 1:
                partial_num += str(paper[j][i])
            else:
                sum += int(partial_num)
                partial_num = '0'
        sum += int(partial_num)
    return sum

# 가로/세로 값 전부 계산
def get_sum(arr):
    return get_horizontal_sum(arr) + get_vertical_sum(arr)

answer = 0
for i in range(max_num):
    bin_num = list(map(int, bin(i)[2:].zfill(n * m).strip()))
    bin_num_arr = [bin_num[i: i+m] for i in range(0, len(bin_num), m)] 
    answer = max(get_sum(bin_num_arr), answer)

print(answer)