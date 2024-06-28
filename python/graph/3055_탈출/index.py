import sys
import copy
from collections import deque
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def escape():
    queue = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'D':   #도착지 좌표기록 후 루프 탈출 조건에 사용
                D = [i,j]                
            elif graph[i][j] == '*':    #물 위치 기록 후 큐에 먼저 넣는다.
                queue.append([i,j,'*'])
            elif graph[i][j] == 'S':
                graph[i][j] == 1
                S = [i, j, 0]       
    queue.append(S)            #물이 모두 큐에 들어간 이후에 고슴도치를 넣는다.
  
    while queue:
        x, y, count = queue.popleft()
        if [x, y] == D:     # 도착지라면 count print
            print(count)
            break
        else:
            for dx, dy in directions:  #물과 고슴도치의 인접영역으로 이동 가능 여부 확인 후 이동
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                # 현재 영역이 물이고, 다음 영역이 X나 D나 물이 아닌 경우, 다음 영역을 물로 만들고, queue에 삽입
                if count == '*' and graph[nx][ny]!='X' and graph[nx][ny]!='D' and graph[nx][ny]!='*':  
                    graph[nx][ny]='*'
                    queue.append([nx,ny,'*'])
                # 현재 영역이 고슴도치 위치이고, 다음 영역이 .이거나 도착지인 경우, count를 올리고, queue에 삽입
                elif type(count)==int and (graph[nx][ny]=='.' or graph[nx][ny]=='D'):
                    graph[nx][ny]=count+1
                    queue.append([nx,ny,count+1])
        if len(queue)==0:
            print('KAKTUS')
            break     

escape()

