import sys
from itertools import combinations
# input = sys.stdin.readline
f = open('test7.txt')
input = f.readline
n, m, h = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(m)]
# 사다리 입력: 0 = 사다리 설치 가능, 1 = 사다리 이미 존재, -1 = 사다리 설치 불가능
ladder = [[0] * (n+1) for _ in range(h + 1)]
for i in range(h+1):
    ladder[i][0] = -1
    ladder[i][n] = -1

for i in range(n+1):
    ladder[0][i] = -1

# 이미 주어진 사다리 정보 입력 및 이미 설치된 사다리 양옆 설치 불가 설정
def install_ladder(ladder, position):
    new_ladder = [row[:] for row in ladder]
    for x, y in position:
        new_ladder[x][y] = 1
        if y - 1 >= 0:
            new_ladder[x][y-1] = -1
        if y + 1 <= n:
            new_ladder[x][y+1] = -1
    return new_ladder

# start 사다리에서 시작해 해당 Ladder 정보로 goal을 계산
def find_goal(start, ladder):
    curr_x = start
    for curr_y in range(1, h+1):
        if ladder[curr_y][curr_x-1] == 1:   # 자기 왼쪽에 사다리가 있다면 curr_x 감소
            curr_x -= 1
        elif ladder[curr_y][curr_x] == 1:   # 자기 오른쪽에 사다리가 있다면 curr_x 증가
            curr_x += 1
    return curr_x

# 설치 가능한 사다리 포지션을 전부 반환
def get_all_valid_ladder_position(ladder):
    position = []
    for i in range(h+1):
        for j in range(n+1):
            if ladder[i][j] == 0:
                position.append((i, j))
    return position

# 주어진 사디리 포지션들이 가능한지 확인
def is_valid_ladder(position):
    grouped_by_x = {}
    for x, y, in position:
        if x not in grouped_by_x:
            grouped_by_x[x] = set()
        grouped_by_x[x].add(y)
    
    for y_values in grouped_by_x.values():
        for y in y_values:
            if y + 1 in y_values or y - 1 in y_values:
                return False
    return True

# 모든 i번째 사다리의 골이 i번째로 끝이 나는지 확인
def check_all_match_ladder(ladder):
    for i in range(1, n+1):
        if i != find_goal(i, ladder):
            return False
    return True

# 주어진 정보로 사다리 설치 및 추가 설치 없이 성공하는지 확인
initial_ladder = install_ladder(ladder, lines)
if check_all_match_ladder(initial_ladder):
    print(0)
    sys.exit()

available_position = get_all_valid_ladder_position(initial_ladder)
for i in range(1, 4):
    for comb in combinations(available_position, i):
        if(is_valid_ladder(comb)):
            new_ladder = install_ladder(initial_ladder, comb)
            if check_all_match_ladder(new_ladder):
                print(i)
                sys.exit()
print(-1)