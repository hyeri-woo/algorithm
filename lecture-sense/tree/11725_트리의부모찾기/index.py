# import sys
# input = sys.stdin.readline
f = open("test2.txt")
input = f.readline
n = int(input())

graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def recur(node, prev):
    parent[node] = prev
    for next in graph[node]:
        if next == prev:
            continue
        recur(next, node)

recur(1, 0)
print('\n'.join(map(str, parent[2:])))