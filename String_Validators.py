string=input()
an=False
n=False
a=False
l=False
u=False
for i in string:
    if i.isalpha() and a==False:
        a=True
        an=True
    if i.isdigit() and n==False:
        n=True
        an=True
    if i.islower() and l==False:
        l=True
    if i.isupper() and u==False:
        u=True
print(an)
print(a)
print(n)
print(l)
print(u)