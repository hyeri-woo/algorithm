import sys

# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(edges, N):
    parent = list(range(N + 1))
    edges.sort(key=lambda x: -x[2])  # 무게 제한이 큰 순서대로 정렬
    mst = []
    
    for a, b, weight in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            mst.append((a, b, weight))
        
        if len(mst) == N - 1:
            break
    
    return mst

def max_pepero_count(N, s, e, mst):
    def dfs(node, parent, min_weight):
        if node == e:
            return min_weight
        
        for next_node, weight in graph[node]:
            if next_node != parent:
                result = dfs(next_node, node, min(min_weight, weight))
                if result != float('inf'):
                    return result
        
        return float('inf')
    
    graph = [[] for _ in range(N + 1)]
    for a, b, weight in mst:
        graph[a].append((b, weight))
        graph[b].append((a, weight))
    
    return dfs(s, -1, float('inf'))

# 입력 처리
N, M = map(int, input().split())
s, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# 최소 스패닝 트리 생성
mst = kruskal(edges, N)

# 결과 출력
print(max_pepero_count(N, s, e, mst))