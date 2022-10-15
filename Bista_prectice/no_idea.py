n,m = map(int,input().split())
main_li=list(map(int,input().split()))
listA=list(map(int,input().split()))
listB=list(map(int,input().split()))
happyness=0
for i in main_li:
    if i in listA:
        happyness+=1
    elif i in listB:
        happyness-=1
print(happyness)