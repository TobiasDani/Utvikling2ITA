
while True:
    def addere():
        #Regner ut summen

        tall1Addere = input("\nHva er ditt første tall? ")

        tall2Addere = input("Hva er ditt andre tall? ")

        summen = int(tall1Addere) + int(tall2Addere)

        print("\nSummen er", summen)


    #Regner ut produktet
    def multiplisere():
        tall1Multiplisere = input("\nHva er ditt første tall? ")

        tall2Multiplisere = input("Hva er ditt andre tall? ")

        produktet = int(tall1Multiplisere) * int(tall2Multiplisere)

        print("\nProduktet er", produktet)

    valg = input("\nVil du addere, multiplisere eller ingenting? ")

    if valg == "addere":
        addere()
    elif valg == "Addere":
        addere()
    elif valg == "multiplisere":
        multiplisere()
    elif valg == "Multiplisere":
        multiplisere()
    elif valg == "ingenting":
        exit()
    elif valg == "Ingenting":
        exit()