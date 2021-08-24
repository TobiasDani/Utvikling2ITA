

while True:
    print("\nHei, hva vil du vite om meg? \n1 -- Navnet mitt \n2 -- Alderen min \n3 -- Hobbyene mine \n4 -- Teknologier jeg jobber med")

    valg = (input("\nHva velger du? "))

    if valg == "1":
        print("\nJeg heter Tobias Danielsen. \n")
    elif valg == "2":
        print("\nJeg er 16 år gammel. \n")
    elif valg == "3":
        print("\nJeg liker å trene, spille piano og programmere. \n")
    elif valg == "4":
        print("\nJeg har jobbet med mange forskjellige teknologier, men jeg har jobbet mest med å programmere i et språk som heter Lua. \n")
    else: print("\nDet du skrev er ikke et gyldig svar. \n")

    mer = str(input("Vil du vite noe mer? Ja eller Nei? "))

    if mer == "Ja":
        print("")
    elif mer == "ja":
        print("")
    else: exit()
    
