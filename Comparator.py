
x = input("Scrieti primul numar: ")
x = int(x)
y = input("Scrieti al doilea numar: ")
y = int(y)

if x > y:
    print("Numarul", x ,"este mai mare decat", y)
elif x < y :
    print("Numarul", x ,"este mai mic decat", y)
elif x == y:
    print("Numerele", x ,"si", y ,"sunt egale")
else:
    print("Ati introdus un numar gresit")
