num=int(input())
num_set=input().split()
num_set=[int(x) for x in num_set]
num_set=set(num_set)

cmd_num = int(input())
for i in range(cmd_num):
    cmd_inp=input()
    if 'pop' in cmd_inp:
        if num_set!={}:
            num_set.pop() 
    elif 'remove' or 'discard' in cmd_inp:
        tempList=cmd_inp.split()
        itm=int(tempList[1])
        num_set.discard(itm)
    
print(sum(num_set))
