import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n, c = map(int, input().split())
house_position = [int(input()) for _ in range(n)]
house_position.sort()

def binary_search(start, end):
    answer = 0
    while (start <= end):
        mid = (start + end) // 2    # 현재 공유기 거리
        current = house_position[0]
        count = 1

        # 공유기 설치 몇 대 할 수 있는지 체크
        for i in range(1, n):
            if house_position[i] >= current + mid:
                count += 1
                current = house_position[i]
        
        if count >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer

start = 1   # 공유기 거리 최소
end = house_position[-1] - house_position[0]    # 공유기 거리 최대
print(binary_search(start, end))