from collections import defaultdict

dic=defaultdict(list)
stor=list(map(int,input().split()))
for i in range(stor[0]):
    ele=input()
    dic[ele].append(str(i+1))
for i in range(stor[1]):
    ele=input()
    if dic[ele]:
        print(' '.join(dic[ele]))
    else:
        print(-1)