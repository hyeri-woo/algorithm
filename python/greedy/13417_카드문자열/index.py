import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
t = int(input())

def get_smallest_string(char):
    answer = [char[0]]
    for i in range(1, len(char)):
        if answer[0] >= char[i]:
            answer.insert(0, char[i])
        else:
            answer.append(char[i])
    return ''.join(answer)

for _ in range(t):
    n = int(input())
    char = list(map(str, input().split()))
    print(get_smallest_string(char))