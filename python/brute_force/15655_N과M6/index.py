f = open('test3.txt', 'r')
n, m = map(int, f.readline().split())
numbers = list(f.readline().split())
numbers.sort()
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start, n):
        if numbers[i] not in temp:
            temp.append(numbers[i])
            dfs(i + 1)
            temp.pop()

dfs(0)
