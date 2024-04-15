f = open("test1.txt", "r")
n = int(f.readline())
sets = set()

for _ in range(n):
    operation = f.readline().split()
    order = operation[0]
    if len(operation) == 1:
        if order == 'all':
            sets = set(range(1, 21))
        elif order == 'empty':
            sets = set()
    else:
        num = int(operation[1])
        if order == 'add':
            sets.add(num)
        elif order == 'remove':
            sets.discard(num)
        elif order == 'check':
            print(1 if num in sets else 0)
        elif order == 'toggle':
            if num in sets:
                sets.discard(num)
            else:
                sets.add(num)
    

# sets = 0
# def get_bit(num, i):
#     return num & (1 << i)

# def set_bit(num, i):
#     return num | (1 << i)

# def toggle_bit(num, i):
#     return num ^ (1 << i)

# def clear_bit(num, i):
#     return num & ~(1 << i)

# for i in operation:
#     order = i[0]
#     num = -1 if len(i) == 1 else int(i[1])
#     if order == 'add':
#         sets = set_bit(sets, num)
#     elif order == 'remove':
#         sets = clear_bit(sets, num)
#     elif order == 'check':
#         print(1 if get_bit(sets, num) else 0)
#     elif order == 'toggle':
#         sets = toggle_bit(sets, num)
#     elif order == 'all':
#         sets = ((1 << 20) - 1) << 1
#     elif order == 'empty':
#         sets = 0

