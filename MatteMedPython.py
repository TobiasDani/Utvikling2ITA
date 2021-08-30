

#Regner ut arealet av en firekant

høyde = int(input("\nHva skal høyden av firekanten være? "))
bredde = int(input("Hva skal bredden av firekanten være? "))

areal = høyde*bredde
omkrets = høyde+høyde+bredde+bredde

print("\nArealet av firekanten er:", areal, "\nOmkretsen av firekanten er:", omkrets, "\n")


#Regner ut arealet av en trekant

høyde = int(input("Hva skal høyden av trekanten være? "))
grunnlinje = int(input("Hva skal grunnlinja av trekanten være? "))

areal = (høyde*bredde)/2

print("\nArealet av trekanten er:", areal, "\n")

