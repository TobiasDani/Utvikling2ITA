import random


def terningkast():
    terning1 = 0
    terning2 = 0
    summen = 0

    while summen !=12:
        input("\nTrykk på en tast: ")
        terning1 = random.randint(1,6)
        terning2 = random.randint(1,6)
        print("\nTerning 1 =", terning1)
        print("\nTerning 2 =", terning2)
        summen = terning1 + terning2
        print("\nSummen er lik", summen)

    print("Hurra! Summen er", summen)

terningkast()

