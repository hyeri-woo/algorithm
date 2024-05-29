import sys
from itertools import combinations
import math
input = sys.stdin.readline
f = open('test6.txt')
n = int(f.readline())
expression = list(f.readline().strip())

# 수식 계산
def calculate_expression(expressions):
    sum = int(expressions[0])
    for e in range(1, len(expressions), 2):
        exp = expressions[e]
        num = int(expressions[e + 1])
        if exp == '+':
            sum += num
        elif exp == '-':
            sum -= num
        elif exp == '*':
            sum *= num
    return sum

# 수식에서 Bracket_index의 괄호만 계산 후 수식 반환
def calculate_bracket(bracket_index, expressions):
    for i in range(len(bracket_index)):
        index = bracket_index[i] - (i * 2)
        result = calculate_expression(expressions[index:index+3])
        expressions = expressions[:index] + [str(result)] + expressions[index+3:]
    return expressions

# 주어진 인덱스들에 중첩되지 않고 괄호를 추가할 수 있는지 확인
def is_valid_bracket(numbers):
    for i in range(len(numbers)-1):
        if numbers[i]+4 > numbers[i+1]:
            return False
    return True


# 아무 괄호 없이 계산
answer = calculate_expression(expression)

# 가능한 괄호의 조합만큼 수식 계산
for i in range(1, math.floor((n+1)/4)+1):
    for comb in combinations(range(0, n - 2, 2), i):
        if is_valid_bracket(comb):
            removed_bracket_expression = calculate_bracket(comb, expression)
            answer = max(calculate_expression(removed_bracket_expression), answer)

# 결과 출력
print(answer)