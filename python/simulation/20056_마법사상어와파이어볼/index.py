import sys
# input = sys.stdin.readline
f = open('test4.txt')
input = f.readline
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)] # 방향 

def append_fireball(fireball_list, fireball):
    r, c, m, s, d = fireball
    key = str(r)+" "+str(c)
    if key in fireball_list:
        fireball_list[key].append((m, s, d))
    else:
        fireball_list[key] = [(m, s, d)]

def move(r, c, fireball):
    m, s, d = fireball
    new_r = (r + direction[d][0] * s) % n
    new_c = (c + direction[d][1] * s) % n
    return (new_r, new_c, m, s, d)
    

def merge_and_divide(fireballs):
    sum_m = sum([f[0] for f in fireballs])
    sum_s = sum([f[1] for f in fireballs])
    d_all_odd = all(f[2] % 2 != 0 for f in fireballs)
    d_all_even = all(f[2] % 2 == 0 for f in fireballs)

    if sum_m < 5:  # 질량이 0인 경우
        return []

    new_fireballs = []
    for i in range(4):
        if d_all_odd or d_all_even:
            new_fireballs.append((int(sum_m / 5), int(sum_s / len(fireballs)), 2 * i))
        else:
            new_fireballs.append((int(sum_m / 5), int(sum_s / len(fireballs)), 2 * i + 1))
    return new_fireballs

def simulate_once(fireball_list):
    new_fireball_list = {}
    for key, fireball in fireball_list.items():
        r, c = map(int, key.split())
        while fireball:
            new_fireball = move(r, c, fireball.pop(0))
            append_fireball(new_fireball_list, new_fireball)

    for key, fireball in new_fireball_list.items():
        if len(fireball) > 1:
            new_fireball = merge_and_divide(fireball)
            new_fireball_list[key] = new_fireball

    return new_fireball_list

def get_sum(fireball_list):
    sum_fireball = 0
    for _, fireball in fireball_list.items():
        sum_fireball += sum([f[0] for f in fireball])
    return sum_fireball

# 입력
n, m, k = map(int, input().split())
fireball_list = {}
for _ in range(m):
    fireball = map(int, input().split())
    append_fireball(fireball_list, fireball)

# 문제 풀이
for _ in range(k):
    fireball_list = simulate_once(fireball_list)

# 출력
print(get_sum(fireball_list))
