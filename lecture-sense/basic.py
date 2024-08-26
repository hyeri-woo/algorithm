######################## 입력과 출력
# case 1 : 단순 정수
number = int(input())

# case 2 : 수열
first, second, third = map(int, input().split())
list_number = list(map(int, input().split()))

# case 3 : 단순 문자
string = input()

# case 4 : 문자열
first, second, third = map(str, input().split())
list_string = list(map(str, input().split()))

# 출력
print(number, string)
print(*list_number)

######################## 반복문
# case 1 : for 문
for num in range(100): # 0 ~ 99
    print(num)

# case 2 : while 문
num = 0
while num < 10: # num이 10보다 작으면 반복, 넘버가 10이 되거나, 10보다 크면 멈춤
    print(num)
    num = num + 1

######################## 조건문
name = "jane"
if name == "jane":
    print("i am jane")
elif name == 'janie':
    print("i am janie")
else:
    print("i am not jane either janie")