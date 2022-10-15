k=input()
num_set=input().split() #convert string to int list
num_set=[int(x) for x in num_set]
num_F=set(num_set)

k=input()
num_set2=input().split()
num_set2=[int(x) for x in num_set2]
num_E=set(num_set2)

print(num_F-num_E) 