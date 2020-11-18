n=eval(input("introduceti anul"))
if (n % 12 )== 0:
    s = "maimuta"
elif (n % 12 ) == 1:
    s = "cucos"
elif (n % 12 )== 2:
    s = "caine"
elif (n % 12 )== 3:
    s = "porc"
elif (n % 12 )== 4:
    s = "sobolan"
elif (n % 12 )== 5:
    s = "bou"
elif (n % 12 )== 6:
    s = "tigru"
elif (n % 12 )== 7:
    s = "iepure"
elif (n % 12 )== 8:
    s = "dragon"
elif (n % 12 )== 9:
    s = "sarpe"
elif (n % 12 )== 10:
    s = "cal"
else:
    s = "oaie"
print("anul",n,"are semnul de",s)