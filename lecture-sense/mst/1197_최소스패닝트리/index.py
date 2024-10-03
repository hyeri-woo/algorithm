# import sys
# input = sys.stdin.readline
import heapq
f = open("test1.txt")
input = f.readline

n, m = map(int, input().split())

# 프림 - 다익스트라
# graph = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append([c, b])
#     graph[b].append([c, a])

# answer = 0
# count = 0


# q = []  # 가중치 없이 1에서 출발
# heapq.heappush(q, [0, 1])

# while q:
#     if count == n:
#         break
#     weight, node = heapq.heappop(q) # 최소 비용 꺼내기
#     if visited[node] == 0:
#         visited[node] = 1
#         answer += weight
#         count += 1

#         for next in graph[node]:
#             heapq.heappush(q, next)
        
# print(answer)

# 크루스칼 - 유니온 파인드
# 1. 모든 링크를 한번에 가져온다. 
# 2. 링크를 연결하면서 같은 집합으로 만들어 준다. 
# 3. 만약에 이미 같은 집합이라면 연결하지 않는다. 
link = [list(map(int, input().split())) for _ in range(m)]
link.sort(key=lambda x:x[2]) # 가중치 기준으로 정렬

parent = [i for i in range(10_001)]
rank = [0] * (10_001)

def _find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def _union(a, b):
    a = _find(a)
    b = _find(b)

    if a == b:
        return 
    elif rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b] += 1

answer = 0

for i in range(m):
    a, b, w = link[i]
    a = _find(a)
    b = _find(b)

    if a == b:
        continue
    _union(a, b)
    answer += w

print(answer)