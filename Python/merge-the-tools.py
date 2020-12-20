def merge_the_tools(string, k):
    split_string = [string[i:i+k] for i in range(0,len(string),k)]
    merged = list()
    for i in split_string:
        temp = set()
        merged.append([x for x in i if not (x in temp or temp.add(x))])    
    print('\n'.join([i for i in [''.join(j) for j in merged]]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
