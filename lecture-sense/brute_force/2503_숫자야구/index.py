# import sys
# input = sys.stdin.readline
f = open("test1.txt")
input = f.readline

# 입력
N = int(input())
hint = [list(map(int, input().split())) for _ in range(N)]

# 문제 풀이
# A가 정답으로 생각할 수 있는 모든 경우의 수를 넣어보기
# 그리고 B가 도전한 내용에 맞는지 확인하기

# 100 ~ 999
answer = 0
for a in range(1, 10): # 100의 자리수
    for b in range(10): # 10의 자리수
        for c in range(10): # 1의 자리수
            # 세 자리 숫자의 각 자릿수가 서로 다른지 확인
            if a == b or b == c or c == a:
                continue
            # 세 자리 숫자의 각 자릿수가 0일 아닌지 확인
            if b == 0 or c == 0:
                continue

            count = 0
            # 숫자가 정해졌다면 
            for [number, strike, ball] in hint: 
                number = str(number)
                a_str, b_str, c_str = str(a), str(b), str(c)
                
                strike_count = 0
                ball_count = 0

                if a_str == number[0]:
                    strike_count += 1
                elif a_str in number:
                    ball_count += 1

                if b_str == number[1]:
                    strike_count += 1
                elif b_str in number:
                    ball_count += 1

                if c_str == number[2]:
                    strike_count += 1
                elif c_str in number:
                    ball_count += 1

                if strike == strike_count and ball == ball_count:
                    count += 1
            
            if count == N:
                answer += 1
                print(a, b, c)
# 출력
print(answer)