f = open("test1.txt", "r")
n = int(f.readline())
numbers = list(map(int, f.readline().split()))
answer = []
visited = [False] * n
max_num = 0

def calculate_max(numbers):
    sum = 0
    for i in range(n-1):
        sum += abs(numbers[i+1] - numbers[i])
    return sum

def solve(depth, n):
    global max_num
    if depth == n:
        partial_sum = calculate_max(answer)
        if max_num < partial_sum:
            max_num = partial_sum
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(numbers[i])
            solve(depth+1, n)
            answer.pop()
            visited[i] = False

solve(0, n)
print(max_num)