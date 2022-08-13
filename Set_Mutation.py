k=input()
num_set=input().split()
num_set=[int(x) for x in num_set]
set_A=set(num_set) #set A
itr=int(input())
for i in range(itr):
    cmd_str=input() 
    num_set.clear()             #reset our num_set type
    num_set=list(input().split())
    num_set=[int(x) for x in num_set]
    set_B=set(num_set)
    temp_list=cmd_str.split()
    if temp_list[0]=='intersection_update':         #check cmd
        set_A.intersection_update(set_B)
    elif temp_list[0] == 'update':
        set_A.update(set_B)
    elif temp_list[0] == 'symmetric_difference_update':
        set_A.symmetric_difference_update(set_B)
    elif temp_list[0]=='difference_update':
        set_A.difference_update(set_B)
print(sum(set_A))
    


