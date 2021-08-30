import random


def terningkast():
    terning1 = 0
    terning2 = 0
    summen = 0

    while summen !=12:
        input("Trykk på en tast: ")
        terning1 = random.randint(1,6)
        terning2 = random.randint(1,6)
        print("Terning 1 =", terning1)
        print("Terning 2 =", terning2)
        summen = terning1 + terning2
        print("Summen er lik", summen)

    print("Hurra!")

terningkast()