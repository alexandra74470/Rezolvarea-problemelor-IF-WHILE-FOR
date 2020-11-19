from fractions import Fraction
a=eval(input('introduceti primul numitor'))
b=eval(input('introduceti al doilea numitor'))
c=eval(input('introduceti primul numarator'))
d=eval(input('introduceti al doilea numarator'))
c!=0 and d!=0
x=Fraction(a,c)
y=Fraction(b,d)
print(x+y)
print(x*y)