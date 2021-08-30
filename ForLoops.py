
def telle():
    for i in range(1,71):
        print(i)
        if i == 35:
            print("Du er halvveis")

        if i % 7 == 0:
            print('*')


def fruktDef():
    frukt = ["Eple", "Pære", "Sitron", "Melon"]

    frukt.append("Plomme")

    nfrukt = input("Skrive frukt: ")
    frukt.append(nfrukt)

    for i in frukt:
        print(i)


klasse = []
nklasse = ""

while nklasse != "Stop":
    nklasse = input("\nSkriv navnet eller Stop hvis du er ferdig: ")
    if nklasse != "Stop":
        klasse.append(nklasse)
        print("\n",nklasse, "er lagt til")

klasse.sort()

print("\nKlassen består av:")

for navn in klasse:
    print("", navn)

exit()

