import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
f = open("test2.txt")
n = int(f.readline())
graph = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)

for _ in range(n):
    start, end = map(int, f.readline().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(destination, start):
    checked = []
    will_check = [start]
    while destination not in will_check:
        node = will_check.pop()
        if node not in checked:
            checked.append(node)
            will_check.extend(reversed(graph[node]))
    return checked

longest_index = max(range(len(graph)), key=lambda i: len(graph[i]))

for i in range(n + 1):
    if len(graph[i]) > 0 and len(graph[i]) < 3:
        print(dfs(longest_index, i))
        answer[i] = len(dfs(longest_index, i))
       
print(answer)