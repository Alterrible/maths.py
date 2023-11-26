from math import*

# Saisi des termes
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))

# Calcul du discriminant
d=(b**2)-4*a*c
print("le discriminant est :",d)

# Tester le discriminant et calculer les solutions
if d>0 :
    x1=((-b)-sqrt(d))/(2*a)
    x2=((-b)+sqrt(d))/(2*a)
    print("x1 est:", x1," et x2 est:", x2)
    # forme factorisé
    print("la forme factorisé est : (x+",x1,")(x+",x1,")")
elif d==0 :
    x=(-b)/(2*a)
    print("x est:", x)
    # forme factorisé
    print("la forme factorisé est : (x+",x,")²")
elif d<0 :
    print("il n'y a pas de solution")

# calcul forme canonique
if a>1:
    alpha=b/a/2
    print("la forme canonique est :",a,"(x+",alpha,")+",c,"-",alpha,"²")
else:
    alpha2=b/2
    print(a,"(x+",alpha2,")+",c,"-",alpha2,"²")