import random


lista = [i for i in range(1, 101)]
x = random.choice(lista)


def guess(x):
    try:
        los = int(input("Zgadnij liczbe: "))
        if los == x:
            return "Brawo zgadłeś"
        elif los < x:
            print("Za mało!")
            return guess(x)
        else:
            print("Za dużo!")
            return guess(x)
    except ValueError:
        print("Podaj liczbę naturalną!")
        return guess(x)


print(guess(x))
