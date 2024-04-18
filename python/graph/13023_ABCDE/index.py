import sys
f = open("test3.txt", "r")
result = 0
n, m = map(int, f.readline().split())
network = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a,b = map(int, f.readline().split())
    network[a].append(b)
    network[b].append(a)

print(network)
# n, m = map(int, f.readline().split())
# s = [list(map(int, f.readline().split())) for _ in range(m)]
# relations = [[] for _ in range(n)]
# result = 0
# visited = [False] * n

# for ss in s:
#     start, end = ss
#     relations[start].append(end)
#     relations[end].append(start)

# # def dfs(adj_list, start, depth=1, max_depth=0):
# #     checked = set()
# #     will_check = [(start, depth)]
    
# #     while will_check:
# #         node, depth = will_check.pop()
# #         if node not in checked:
# #             checked.add(node)
# #             max_depth = max(max_depth, depth)
# #             for neighbor in adj_list[node]:
# #                 will_check.append((neighbor, depth + 1))
    
# #     return max_depth


# # # 최대 깊이 확인
# # for i in range(n):
# #     max_depth = dfs(relations, i)
# #     if max_depth >= 5:
# #         print(1)
# #         sys.exit()
# # print(0)
    
# def dfs(start, cnt):
#     global result
#     visited[start] = True
#     cnt += 1
#     if cnt == 5:
#         result = 1
#         return
#     for f in relations[start]:
#         if not visited[f]:
#             visited[f] = True
#             dfs(f, cnt)

# for i in range(n):
#     if result == 1:
#         break
#     dfs(i, 0)

# print(result)