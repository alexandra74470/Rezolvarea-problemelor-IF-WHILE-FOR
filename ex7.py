n=eval(input('introduceti un numar'))
s1=1
s2=1
m=0
for i in range(1,n+1):
    s1=s1*2+1
print('la varsta de ',n,'ani','Mihai a primit',s1,'dolari')
while s2<=100:
    m+=1
    s2=s2*2+m
print('cadoul era mai mare de 100 dolari la varsta de',m,'ani')