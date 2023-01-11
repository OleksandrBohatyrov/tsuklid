from math import *
from random import *
from time import sleep
##09/01/23
#print("Arvuta peast! ...4*100-55")

#o_vastus=4*100-55

#vastus=int(input("Lahenda ülesanne ..."))

#k=1

#while vastus!=o_vastus:

#    print("Viga! Sisesta Õige vastus on ...", )

#    vastus=int(input("Sisesta vastus ..."))

#    k+=1

#print("Õige vastus! Katsed oli ...",k )

#2 variant while true abil
#print("Arvuta peast! ...4*100-55")
#o_vastus=4*100-55
#vastus=int(input("Lahenda ülesanne ..."))
#k=1
#while True:
#    if vastus==o_vastus:
#        break
#    else:
#        print("Viga! Sisesta Õige vastus on ...", )
#        vastus=int(input("Sisesta vstus ..."))
#        k+=1
#print("Õige vastus! Katsed oli...", k)
#print()

#x=0

#while True:
#    if x%2==1:
#        print(x, end=" ")
#    x+=1
#    if x==30:
#        break


#for x in range(30):
#    if x%2==1:
#        print(x, end=" ")



print("*** KUSIMUSTE MANGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisesta taisarv => "))) #eemaldas sulguri
        break
    except ValueError:
         print("See pole taisarv.")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole motet midagi teha.")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Maarake, kui palju on paaris- ja mitu paaritut numbrit")
    print()
    c=b=a #eemaldas topelt võrdsuse
    paaris=0 #eemaldas topelt võrdsuse
    paaritu=0 #eemaldas topelt võrdsuse
    while b > 0: #muutis käärsoole
        if b % 2==0: #lisas veel ühe võrdsuse
            paaris += 1 #parandas =+
        else:
            paaritu += 1 #parandas =+
        b = b // 10 #eemaldas topelt võrdsuse

    print("Paaris arvude kogus:", paaris) #lisas koma
    print("Paaritu on:", paaritu) #lisas koma
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Poorame sisestatud arvu umber")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #eemaldas lisatühiku
    print("Muudetud arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print(("Uurime Syracuse hüpoteesi"))
    print()
    if c % 2 == 0: #lisatud võrdsed 
        print(c," - Paaris arv, Jagame 2.") #tõstis esile komamuutuja
    else:
        print(c," - Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.") #tõstis esile komamuutuja
    while c != 1:
            if c % 2 == 0:
                    c = c / 2 #kaks korda võrdne
            else:
                    c = (3*c + 1) / 2
            print(round(c), end=" ") #lisas sulguri
    print()
    print("on tõestatud") 