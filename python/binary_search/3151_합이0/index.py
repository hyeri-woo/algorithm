import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

def search(start, end):
    
    while start <= end:
        mid = (start + end) // 2
        

for i in range(n-2):
    for j in range(i+1, n-1):
        target = -(numbers[i] + numbers[j])
        print(numbers[i], numbers[j], target)

# def count_zero_sum_triplets(arr):
#     # 정렬된 배열
#     arr.sort()
#     n = len(arr)
#     count = 0

#     for i in range(n - 2):
#         for j in range(i + 1, n - 1):
#             target = -(arr[i] + arr[j])
#             # 이분 탐색
#             left, right = j + 1, n - 1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if arr[mid] == target:
#                     count += 1
#                     break
#                 elif arr[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1

#     return count

# # 예시 입력
# A = [-1, 2, -1, 1, 0, -4]
# print(count_zero_sum_triplets(A))  # 결과는 2여야 합니다.