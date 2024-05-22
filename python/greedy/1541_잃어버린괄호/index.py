import sys
import re
from collections import deque
input = sys.stdin.readline
f = open('test3.txt')
expression = deque(re.findall(r'\d+|[+-]', f.readline()))
stack = [int(expression.popleft())]

while expression:
    right = expression.popleft()
    if right == '-':
        stack.append(int(expression.popleft()))
    elif right == '+':
        stack.append(int(expression.popleft()) + int(stack.pop()))

answer = stack[0]
for n in stack[1:]:
    answer -= n

print(answer)