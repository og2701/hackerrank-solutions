n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    op = input().split(' ') 
    exec(f's.{op[0]}({op[1]})' if 'pop' not in op else f's.{op[0]}()')
        
print(sum(s))
