import sys
from bisect import bisect_left
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

answer = 0

for i in range(n - 2):  # 3명을 고르기 위해 0 ~ n-3
    # 이분 탐색
    start = i + 1
    end = n - 1
    while start < end:
        result = numbers[i] + numbers[start] + numbers[end]
        if result > 0:  # 0보다 크면 end 감소
            end -= 1
        else:           # 0보다 작거나 같으면 start 증가
            if result == 0:
                # start에 위치한 수와, end에 위치한 수가 같으면 start와 end 사이의 모든 조합이 합이 0이므로, end-start
                if numbers[start] == numbers[end]:
                    answer += end - start
                # 다르다면, bisect_left를 사용하여, end와 같은 값을 가지는 첫번째 인덱스를 찾아, 그 범위 내의 경우의 수를 더함
                else:
                    idx = bisect_left(numbers, numbers[end])
                    answer += end - idx + 1
            start += 1

print(answer)