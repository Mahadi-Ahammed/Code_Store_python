m,n=map(int,input().split())
for i in range(1,m,2):
    t=int((n-(3*i))/2)
    t2=int((n-7)/2)
    print('{}{}{}'.format('-'*t,'.|.'*i,'-'*t))
print('{}WELCOME{}'.format('-'*t2,'-'*t2))
for i in range(m-2,0,-2):
    t=int((n-(3*i))/2)
    t2=int((n-7)/2)
    print('{}{}{}'.format('-'*t,'.|.'*i,'-'*t))
