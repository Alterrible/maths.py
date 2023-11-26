from math import*

# Saisi des termes
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))

# Calcul du discriminant
d=(b**2)-4*a*c
print("le discriminant est :", d)

# Tester le discriminant et calculer les solutions
if d>0 :
    x1=((-b)-sqrt(d))/(2*a)
    x2=((-b)+sqrt(d))/(2*a)
    print(f"x1 est: {x1} et x2 est: {x2}")
    # forme factorisé
    if x1<0 :
        print(f"la forme factorisé est : (x{x1})(x+{x2})")
    elif x2<0 :
        print(f"la forme factorisé est : (x+{x1})(x{x2})")
    elif x1 and x2 <0:
        print(f"la forme factorisé est : (x{x1})(x{x2})")
    else:
        print(f"la forme factorisé est : (x+{x1})(x+{x2})")
elif d==0:
    x=(-b)/(2*a)
    print("x est:", x)
    # forme factorisé
    if x<0:
        print(f"la forme factorisé est : (x{x})²")
    else:
        print(f"la forme factorisé est : (x+{x})²")
elif d<0:
    print("il n'y a pas de solution")

# calcul forme canonique
if a>1:
    alpha=b/a/2
    chiffre=c-(alpha**2)
    if alpha<0 :
        print(f"la forme canonique est : {a}(x{alpha})+{chiffre}")
    elif chiffre<0 :
        print(f"la forme canonique est : {a}(x+{alpha}){chiffre}")
    elif alpha and chiffre <0:
        print(f"la forme canonique est : {a}(x{alpha}){chiffre}")
    else:
        print(f"la forme canonique est : {a}(x+{alpha})+{chiffre}")
else:
    alpha2=b/2
    chiffre2=c-(alpha2**2)
    if alpha2<0 :
        print(f"la forme canonique est : {a}(x{alpha2})+{chiffre2}")
    elif chiffre2<0 :
        print(f"la forme canonique est : {a}(x+{alpha2}){chiffre2}")
    elif alpha2 and chiffre2 <0:
        print(f"la forme canonique est : {a}(x{alpha2}){chiffre2}")
    else:
        print(f"la forme canonique est : {a}(x+{alpha2})+{chiffre2}")