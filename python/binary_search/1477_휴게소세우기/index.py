import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n, m, l = map(int, input().split())
positions = list(map(int, input().split()))
positions.append(0)
positions.append(l)
positions.sort()

# 해당 distance가 주어졌을때 총 몇개의 휴게소를 지을 수 있는지 계산
def num_placable_areas(distance):
    diff = list(map(lambda i: positions[i] - positions[i-1] - 1, range(1, len(positions))))
    count = 0
    for d in diff:
        count += d // distance
    return count

def search(start, end):
    result = end
    while start <= end:
        mid = (start + end) // 2
        count = num_placable_areas(mid)
        if count <= m:
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1
    return result
        
print(search(1, l-1))