#Company Logo
com_name="google"
com_name=''.join(sorted(com_name))
k={}
for i in com_name:
    if i not in k:
        k[i]=com_name.count(i)
for i in range(3):
    l=max(k,key=k.get)
    print(l,k[l])
    del k[l]
