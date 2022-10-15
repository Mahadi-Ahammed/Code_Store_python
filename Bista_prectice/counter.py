from collections import Counter

shoe_num=int(input())
shoes = list(map(int,input().split()))
cnt=Counter(shoes)
case=int(input())
profit=0
for i in range(case):
    customer=[]
    customer=list(map(int,input().split()))
    if cnt[customer[0]]!= 0:
        cnt[customer[0]]-=1
        profit+=customer[1]
print(profit) 