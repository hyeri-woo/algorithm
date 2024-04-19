f = open("test2.txt")
n, m = map(int, f.readline().split())
data = [list(map(int, f.readline().split())) for _ in range(m)]
graph = {}
for u, v in data:
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

# def dfs(graph, start):
#     checked = []
#     will_check = [start]
#     while will_check:
#         node = will_check.pop()
#         if node not in checked:
#             checked.append(node)
#             if node in graph:
#                 will_check.extend(reversed(graph[node]))
#     return checked
        
def dfs(graph, start, visited=None, answer=None):
    if visited is None:
        visited = set()
    if answer is None:
        answer = []

    visited.add(start)
    answer.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, answer)

    return answer

count = 0
visited = []
for i in range(1, n+1):
    if i not in visited:
        visited.extend(dfs(graph, i))
        count += 1

print(count)

# 시작 노드 설정
# start_node = 1

# print(dfs(graph, start_node))