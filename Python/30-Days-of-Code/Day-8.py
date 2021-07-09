import sys

len_ = int(sys.stdin.readline())
namesAndNums = [sys.stdin.readline().split() for _ in range(len_)]
phoneBook = {name:num for name,num in namesAndNums}

while True:
    query = sys.stdin.readline().split()
    try: 
        query[0]
    except IndexError: break
    if(query[0] in phoneBook.keys()):
        print(f"{query[0]}={phoneBook[query[0]]}")
    else:
        print("Not found")
