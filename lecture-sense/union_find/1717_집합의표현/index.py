# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0] * (n+1)

def _union(a, b): # 최대 높이 확인 후 합치기
    a = _find(a)
    b = _find(b)

    if a == b:
        return
    
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b] += 1

def _find(a):
    if parent[a] == a:
        return a
    else:
        # parent[a] = _find(parent[a])
        return _find(parent[a])

for _ in range(m):
    x, a, b = map(int, input().split())

    if x == 0:
        _union(a, b)
    else: 
        if _find(a) == _find(b):
            print("YES")
        else:
            print("NO")