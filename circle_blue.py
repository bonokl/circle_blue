"""
Napisati program u programskom jeziku Python koji ispisuje brojeve 1 -
100 osim u ovim slučajevima:
– Ako je broj djeljiv s brojem 5 ispisuje riječ “Circle”
– Ako je broj djeljiv s brojem 7 ispisuje riječ “Blue”
– Ako je broj djeljiv s 5 i 7 ispisuje riječi “Circle Blue”.
• Program postaviti u datoteku circle_blue.py
"""


# - u pdfu se, ako je broj djeljiv s 5 ispisuje prvo 'Circle' pa ispod toga broj
#   pretpostavljam da je to greška? Ako je djeljiv s oba broja onda ispisati sva tri teksta?

# ispis kao mislim da bi trebalo ici iz teksta zadatka
def circle_blue_1():
    for i in range(1, 101):
        if i % 5 == 0 and i % 7 == 0:
            print('CircleBlue')
        elif i % 5 == 0:
            print('Circle')
        elif i % 7 == 0:
            print('Blue')
        else:
            print(i)


# ispis kao u primjeru
def circle_blue_2():
    for i in range(1, 101):
        if i % 5 == 0 and i % 7 == 0:
            print('CircleBlue')
        if i % 5 == 0:
            print('Circle')
        if i % 7 == 0:
            print('Blue')
        else:
            print(i)

