import heapq
from collections import deque
f = open("test1.txt")
input = f.readline
n, k = map(int, input().split())
max_pos = 100_001
def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [-1] * (max_pos)
    visited[start] = 0
    answer = 0
    while q:
        node = q.popleft()
        if node == end:
            answer = visited[node]
            break
        for d in [-1, 1, node]:
            next = d + node
            if 0 <= next < max_pos and visited[next] == -1:
                if next == node * 2:
                    q.appendleft(next)
                    visited[next] = visited[node]
                else:
                    q.append(next)
                    visited[next] = visited[node] + 1
    return answer

print(bfs(n, k))