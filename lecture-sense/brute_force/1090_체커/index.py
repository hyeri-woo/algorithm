# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline

# 입력
N = int(input())
position = [list(map(int, input().split())) for _ in range(N)]
MAX = int(1e9)

# 문제 풀이
# 모든 위치에서 모든 친구들의 자리를 계산해서 가장 작은 숫자를 구해라.

# 1번 아이디어: x의 거리, y의 거리를 구분해서 계산 해 준 뒤 합쳐서 최소값을 구해주면 된다.
# 2번 아이디어: 한 곳에서 모일 때, 비용을 최소화 하기 위해서는 점들 중 한 곳에서 모이면 된다.
# 3번 아이디어: n점이 모였을 때의 최소거리를 구하고 싶다면 해당 점에서 가까운 n점의 거리만 더해주면 된다.

# 1. 각 체커들이 모일 좌표를 선정한다
# 2. 선정한 좌표와 각 체커들의 거리를 계산하여 저장한다. 
# 3. 저장한 값을 오름차순으로 정렬한다. 
# 4. costs의 값을 순차적으로 더하면 체커들이 1개, 2개, 3개 ~ 모였을때 비용이 계산된다. 
# 5. 체커 갯수별 비용의 최저값이 가장 효율적인 위치가 된다. 

answer = [MAX] * N # 모일 체커 수 별로 값을 저장할 배열

for x in position: # x 좌표 후보
    for y in position: # y 좌표 후보
        costs = []
        for ix, iy in position: # 입력받은 좌표
            # 현재 x,y 좌표와 입력받은 좌표의 거리를 비교한 값을 costs 배열에 입력
            costs.append(abs(x[0] - ix) + abs(y[1] - iy))
        # costs를 정렬
        costs.sort()
        cost = 0
        for i in range(N):
            # cost 에 순차적으로 더하면서
            cost += costs[i]
            # 해당 인덱스의 값(answer[i])와 현재 좌표의 거리(cost)와 비교하여 작은 값을 저장
            answer[i] = min(answer[i], cost)

print(*answer)