import sys
from collections import deque

# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n, m = map(int, input().split())
s, e = map(int, input().split())
bridges = [list(map(int, input().split())) for _ in range(m)]

def can_reach(graph, start, end, pepero_count):
    visited = [False] * (len(graph) + 1)
    queue = deque([(start, pepero_count)])
    visited[start] = True

    while queue:
        current, remaining_pepero = queue.popleft()
        if current == end:
            return True
        
        for next_node, weight in graph[current]:
            if not visited[next_node] and remaining_pepero <= weight:
                visited[next_node] = True
                queue.append((next_node, remaining_pepero))
    
    return False

def max_pepero_count(N, M, s, e, bridges):
    graph = [[] for _ in range(N + 1)]
    for h1, h2, k in bridges:
        graph[h1].append((h2, k))
        graph[h2].append((h1, k))

    left, right = 0, 1000000
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_reach(graph, s, e, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

print(max_pepero_count(n, m, s, e, bridges))