# import sys
# input = sys.stdin.readline
f = open("test3.txt")
input = f.readline
n, m = map(int, input().split())

def recur(length, output):
    if length == m:
        print(' '.join(map(str, output)))
        return
    for i in range(1, n+1):
        if not i in output:
            output.append(i)
            recur(length+1, output)
            output.pop()

recur(0, [])