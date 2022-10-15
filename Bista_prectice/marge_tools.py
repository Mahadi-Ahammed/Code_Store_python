s=input()
k=int(input())
dif=int(len(s)/k)
for i in range(0,len(s),k):
    u=s[i:i+k]
    # print(i+1,i+dif)
    ans=''
    for l in u:
        if l not in ans:
            ans+=l
    print(ans)

    