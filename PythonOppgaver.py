import random


def oppgave1():
    #Lag er program som bytter ut verdiene på i variabelene
    frukt = "agurk"
    gronnsak = "eple"
    print("\nFrukt er lik " + frukt + ", og gronnsak er lik " + gronnsak)
    print("Bytter på variabelene...")
    temp = frukt
    frukt = gronnsak
    gronnsak = temp
    print("Frukt er lik " + frukt + ", og gronnsak er lik " + gronnsak + "\n")


def oppgave2():
    navn = "Marte"
    alder = 22
    if navn=="Maren" and alder==24:
        print("Du heter Maren og er 24 år gammel")
    elif navn=="Maren" or alder==22:
        print("Du heter Maren eller er 22 år")
    else:
        print("Du heter ikke Maren")


def oppgave3a():
    tall1 = 14
    tall2 = 7

    if tall1 > tall2:
        print("\nTall:1 (" + str(tall1) + ") er større enn Tall:2 (" + str(tall2) + ")\n")
    elif tall1 < tall2:
        print("\nTall1 (" + str(tall1) + ") er mindre enn Tall2 (" + str(tall2) + ")\n")


def oppgave3b():
    tall1 = 14
    tall2 = 7
    tall3 = 11

    if tall1 > tall2 and tall1 > tall3:
        print("\nTall1 (" + str(tall1) + ") er størst\n")
    elif tall2 > tall1 and tall2 > tall3:
        print("\nTall2 (" + str(tall2) + ") er størst\n")
    elif tall3 > tall1 and tall3 > tall2:
        print("\nTall3 (" + str(tall3) + ") er størst\n")


def oppgave4():
    navnEn = "Jonathan"
    navnTo = "Tobias"

    if len(navnEn) > len(navnTo):
        print(navnEn, "har lengere navn enn", navnTo + ". Han har", len(navnEn), "bokstaver i navnet.")
    elif len(navnEn) < len(navnTo):
        print(navnTo, "har lengere navn enn", navnEn + ". Han har", len(navnEn), "bokstaver i navnet.")


def oppgave5a():
    start = 1
    slutt = 12
    for i in range(start, slutt):
        print(i)


def oppgave5b():
    start = 1
    slutt = 12
    for i in range(slutt, start, -1):
        print(i)


def oppgave6():
    
    tallet = 0

    while tallet != 571:
        input("Trykk på en tast for å skrive ut et tall")
        tallet = random.randint(1, 999)
        print(tallet)
    
    print("Gratulerer! Tallet ble:", tallet)


def oppgave7a():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    for tall in a:
        print(tall)


def oppgave7b():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    for tall in a:
        if tall < 5:
            print(tall)


def oppgave7c():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    for tall in a:
        if tall % 2 == 0:
            print(tall)


def oppgave7d():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []

    for tall in a:
        if tall > 5:
            b.append(tall)
    
    print(b)


def oppgave8():
    cm = int(input("Hva er høyden din i cm: "))
    vekt = int(input("Hva er vekten din i kg: "))
    m = cm/100
    bmi = vekt / (m * m)

    print("Din kroppsmasseindeks (BMI) er",bmi)
    
    if bmi > 17.5 and bmi < 23.9:
        print("Du er normal vekt")
    elif bmi < 17.5:
        print("Du er undervektig")
    elif bmi > 23.9:
        print("Du er overvektig")

oppgave8()