import sys
import copy
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 배열의 앞 또는 뒤를 length - len(arr) pad_char로 채워주는 함수
def pad_array(s, position='start', length=n, pad_char=0):
    if position == 'start':
        return [pad_char] * (length - len(s)) + s
    return s + [pad_char] * (length - len(s))

# 블록을 위로 이동시켜주는 함수
def move_up(board):
    for i in range(n):
        new_block = []
        just_merged = False 
        for j in range(n):
            if board[j][i] == 0:    # block이 비었을 경우 skip
               continue
            if len(new_block) != 0 and not just_merged and new_block[-1] == board[j][i]:    # new_block이 비지 않고, 전에 바로 병합되지 않고, 전의 값이 현재의 값이 같을때
               new_block.append(new_block.pop() + board[j][i])
               just_merged = True
            else: 
                new_block.append(board[j][i])
                just_merged = False 
        new_block = pad_array(new_block, position='end')
        for w in range(n):
            board[w][i] = new_block[w]

# 블록을 밑으로 이동시켜주는 함수
def move_down(board):
    for i in range(n):
        new_block = []
        just_merged = False 
        for j in range(n-1, -1, -1):
            if board[j][i] == 0:
               continue
            if len(new_block) != 0 and not just_merged and new_block[-1] == board[j][i]:
               new_block.append(new_block.pop() + board[j][i])
               just_merged = True
            else: 
                new_block.append(board[j][i])
                just_merged = False 
        new_block = pad_array(list(reversed(new_block)))
        for w in range(n):
            board[w][i] = new_block[w]

# 블록을 오른쪽으로 이동시켜주는 함수
def move_right(board):
    for i in range(n):
        new_block = []
        just_merged = False 
        for j in range(n-1, -1, -1):
            if board[i][j] == 0:
               continue
            if len(new_block) != 0 and not just_merged and new_block[-1] == board[i][j]:
               new_block.append(new_block.pop() + board[i][j])
               just_merged = True
            else: 
                new_block.append(board[i][j])
                just_merged = False 
        board[i] = pad_array(list(reversed(new_block)))

# 블록을 왼쪽으로 이동시켜주는 함수
def move_left(board):
    for i in range(n):
        new_block = []
        just_merged = False 
        for j in range(n):
            if board[i][j] == 0:
               continue
            if len(new_block) != 0 and not just_merged and new_block[-1] == board[i][j]:
               new_block.append(new_block.pop() + board[i][j])
               just_merged = True
            else: 
                new_block.append(board[i][j])
                just_merged = False
        board[i] = pad_array(new_block, position='end')

# block 중 가장 큰 것을 찾아주는 함수
def find_max_block(board):
    return max(max(row) for row in board)

def dfs(board, depth):
    global answer
    if depth == 5:
        answer = max(answer, find_max_block(board))
        return
    
    # 현재 상태를 저장
    original_board = copy.deepcopy(board)

    # 네 방향으로 이동
    for move in [move_up, move_down, move_left, move_right]:
        move(board)
        dfs(board, depth + 1)
        board = copy.deepcopy(original_board)  # 이동 후 원래 상태로 복원

answer = -1
dfs(board, 0)
print(answer)