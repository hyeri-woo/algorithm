import sys
# input = sys.stdin.readline
f = open('test3.txt')
input = f.readline
MAX_PT = 30
n, m = map(int, input().split())
a = list(map(int, input().split()))

def get_rider_cnt(m, a, time):
    sum_p = m
    for c in a:
        sum_p += time // c
    return sum_p

def get_time(n, m, a, MAX_PT):
    time = 0
    start = 0
    end = n // m * MAX_PT

    while start <= end:
        mid = (start + end) // 2
        sum_p = get_rider_cnt(m, a, mid)
        if sum_p >= n:
            end = mid - 1
            time = mid
        else:
            start = mid + 1
    return time
    
def get_last_ride(n, m, a, time):
    rider_cnt = get_rider_cnt(m, a, time - 1)
    for i in range(m):
        if time % a[i] == 0:
            rider_cnt += 1
        if rider_cnt == n:
            return i + 1
    
time = get_time(n, m, a, MAX_PT)
if time == 0:
    print(n)
else:
    print(get_last_ride(n, m, a, time))