n=eval(input('introduceti un numar'))
s=0
for i in range(1,n+1):
    m=1
    for n in range(1,i+1):
        m*=n
    s+=m
print('s=',s)