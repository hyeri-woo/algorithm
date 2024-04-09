f = open("test3.txt", "r")
n = int(f.readline())
answer = [0] * n
signs = list(f.readline())  # 부호 조건이 저장될 리스트
sign = [[0 for _ in range(n)] for _ in range(n)]

# +, - 대신 1, -1을 저장해 solve()에서 해당 인덱스의 수에 부호를 쉽게 붙일 수 있도록 함
idx = 0
for i in range(0, n):
    for j in range(i, n):
        if signs[idx] == '+':
            sign[i][j] = 1
        elif signs[idx] == '-':
            sign[i][j] = -1
        idx += 1

# 현재 index 번째 수를 채울 때 sign[i][index]의 부호조건을 만족하는지 아닌지 검사하는 함수(역순)
def check(index):
    s = 0
    for i in range(index, -1, -1):
        s += answer[i]
        if sign[i][index] == 0 and s != 0:
            return False
        elif sign[i][index] < 0 and s >= 0:
            return False
        elif sign[i][index] > 0 and s <= 0:
            return False         
    return True

# 현재 index 번째 수를 채우는 함수
def solve(index):
    # check(index)를 만족해야 solve(index + 1)의 재귀호출이 가능하므로 index = n이면 sign 배열의 모든 부호 조건을 만족한 경우이므로 True 리턴
    if index == n:
        return True
    # recursive case 1: 현재 index 수가 n 미만이고 0이면 바로 조건 검사 후 재귀 호출
    if sign[index][index] == 0:
        answer[index] = 0
        return check(index) and solve(index+1)
    # recursive case 2: 현재 index 수가 n 미만이고 0이 아니면 index번째 부호를 붙인 후 조건 검사 후 재귀 호출
    for i in range(1, 11):
        answer[index] = i * sign[index][index]
        if check(index) and solve(index + 1):
            return True
    return False
    
solve(0)
print(' '.join(map(str, answer)))