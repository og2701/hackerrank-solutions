def even_odd_indexes(s):
    result = [[],[]]
    for i in range(len(s)):
        if i%2 == 0:
            result[0].append(s[i])
        elif i%2 != 0:
            result[1].append(s[i])
    for i in range(len(result)):
        result[i] = ''.join(result[i])
    print(' '.join(result))
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        even_odd_indexes(s)
