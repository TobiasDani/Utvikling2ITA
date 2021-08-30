
while True:
    def addere():
        #Regner ut summen

        tall1Addere = int(input("\nHva er ditt første tall? "))

        tall2Addere = int(input("Hva er ditt andre tall? "))

        summen = tall1Addere + tall2Addere

        print("\nSummen er", summen)


    #Regner ut produktet
    def multiplisere():
        tall1Multiplisere = int(input("\nHva er ditt første tall? "))

        tall2Multiplisere = int(input("Hva er ditt andre tall? "))

        produktet = tall1Multiplisere * tall2Multiplisere

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