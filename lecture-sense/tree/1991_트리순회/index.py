# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline
n = int(input())
graph = [[] for _ in range(130)]

for _ in range(n):
    a, b, c = map(str, input().strip().split())
    # 아스키 코드
    a, b, c = ord(a), ord(b), ord(c)

    graph[a].append(b)
    graph[a].append(c)

answer = [''] * 3
def preorder(node):
    if node == 46:
        return
    answer[0] += chr(node)
    preorder(graph[node][0])
    preorder(graph[node][1])

def inorder(node):
    if node == 46:
        return
    inorder(graph[node][0])
    answer[1] += chr(node)
    inorder(graph[node][1])

def postorder(node):
    if node == 46:
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    answer[2] += chr(node)


preorder(65)
inorder(65)
postorder(65)

print('\n'.join(answer))