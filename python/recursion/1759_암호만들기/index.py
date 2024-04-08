from itertools import combinations

f = open("test1.txt", "r")
l, c = map(int, f.readline().split())
chars = list(map(str, f.readline().split()))
result = []

def extract_vowels_consonants(arr):
    vowels = 'aeiou'
    vowels_arr = [char for char in arr if char in vowels]
    consonants_arr = [char for char in arr if char not in vowels]
    return vowels_arr, consonants_arr

vowel, consonants = extract_vowels_consonants(chars)

for i in range(1, l-1):
    v_combi = [list(x) for x in combinations(vowel, i)]
    c_combi = [list(x) for x in combinations(consonants, l-i)]
    products = ((x, y) for x in v_combi for y in c_combi)
    for u, v in products:
        result.append(''.join(sorted(''.join(u) + ''.join(v))))
        
print('\n'.join(sorted(result)))