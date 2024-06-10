import sys
# input = sys.stdin.readline
f = open('test3.txt')
input = f.readline
n, attack = map(int, input().split())
room_info = [list(map(int, input().split())) for _ in range(n)]

def simulate(room_info, attack, max_hp):
    curr_hp = max_hp
    curr_attack = attack
    for t, a, h in room_info:
        if t == 1:
            if h % curr_attack == 0:
                curr_hp -= (h / curr_attack - 1) * a 
            else:
                curr_hp -= (h // curr_attack) * a
        elif t == 2:
            curr_hp = min(max_hp, curr_hp + h)
            curr_attack += a
        if curr_hp <= 0:
            return False
    return curr_hp

def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        hp = simulate(room_info, attack, mid)
        if hp >= 1:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result

print(int(binary_search(1, n*1000000*1000000)))
        