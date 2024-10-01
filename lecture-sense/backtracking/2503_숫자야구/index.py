# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n = int(input())
hint  = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def count_strike_ball(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    strike, ball = 0, 0
    for i in range(3):
        if num1[i] == num2[i]:
            strike += 1
        elif num1[i] in num2:
            ball += 1
    return strike, ball

def is_all_diff_numbers(num):
    d1 = num // 100
    d2 = (num % 100) // 10
    d3 = num % 10
    if d1 == d2 or d1 == d3 or d2 == d3:
        return False
    return True


def is_valid(hint_idx, num1):
    if not is_all_diff_numbers(num1):
        return False
    num2, s, b = hint[hint_idx]
    strike, ball = count_strike_ball(num1, num2)
    if s == strike and b == ball:
        return True
    return False 

def recur(hint_idx, number):
    global answer
    if hint_idx == n:
        answer += 1
        recur(0, number+1)
        return
    if number == 1000:
        return
    # 만약에 힌트에 통과했다면
    if is_valid(hint_idx, number):
        recur(hint_idx+1, number)
    # 만약에 힌트에 통과하지 않았다면
    else:
        recur(0, number+1)

recur(0, 100)

print(answer)