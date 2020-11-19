import math
a=eval(input('introduceti primul numar'))
b=eval(input('introduceti al doilea numar'))
l=round(math.log(b,a))
if a**l==b:
    print(b,'este o putere a lui',a)
else:
    print(b,'nu este o putere a lui',a)