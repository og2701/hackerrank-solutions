from itertools import combinations

len_ = int(input())
letters = input().split()
k = int(input())

num = 0
den = 0
for i in combinations(letters,k):
    den += 1
    if 'a' in i:
        num += 1

print(num/den)
