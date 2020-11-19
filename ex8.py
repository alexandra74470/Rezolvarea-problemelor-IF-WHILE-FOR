a=eval(input('introduceti primul numar'))
b=eval(input('introduceti al doilea numar'))
c=eval(input('introduceti al treilea numar'))
if a<(c+b) and b<(c+a) and c<(a+b):
    if a==b and a==c and c==b:
        print('triunghiul ABC este echilateral')
    if a==b or b==c or c==a:
        print('triunghiul ABC este isoscel')
    else:
        print('triunghiul ABC este scalen')
else:
    print('triunghiul nu poate fi format')