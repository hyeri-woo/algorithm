import sys
# input = sys.stdin.readline
f = open('test1.txt')
input = f.readline
t = int(input())

def check_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        # left right 문자가 동일한 경우
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            # left right 다른 경우: 한 문자열 제거 후 회문 확인
            # 2-1. 오른쪽 문자열 제거한 경우 제거 후 회문이되는지 확인 
            if left < right - 1:
                temp = word[:right] + word[right + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            # 2-2. 왼쪽 문자열 제거한 경우 제거 후 회문이되는지 확인 
            if left + 1 < right:
                temp = word[:left] + word[left + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            # # 2-3. 회문이 안된 경우, 2리턴  
            return 2
    return 0


for _ in range(t):
    print(check_palindrome(str(input().strip())))
