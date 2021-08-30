
function addere() {

    tall1Addere = 5
    tall2Addere = 20

    summen = tall1Addere + tall2Addere
    console.log("Summen er", summen)

}

function multiplisere() {

    tall1Multiplisere = 5
    tall2Multiplisere = 20

    produktet = tall1Multiplisere * tall2Multiplisere
console.log("Produktet er", produktet)

}


valg = "Multiplisere"

if (valg == "Addere") {
    addere()
} else if (valg == "addere") {
    addere()
} else if (valg == "Multiplisere") {
    multiplisere()
} else if (valg == "multiplisere") {
    multiplisere()
} else {
    return;
}
