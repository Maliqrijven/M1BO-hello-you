print (" welkom bij mijn tekstbased applicatie\n")

print (" eerst een kleine intro\n")

print ("jij en 2 andere professionele voetballers uit Nigeria, gaan een avondje op stap en worden gedrogeerd, jullie worden wakker in Zuid-Afrika en hebben geen idee heo jullie daar gekomen zijn. Wat jullie wel weten is dat jullie heel snel naar Nederland moeten voor het WK voetbal, maar jullie zijn wel beroofd van al jullie spullen. Dus hoe jullie naar Nederland gaan komen is de vraag... ")

def een():
    print("Gaan jullie reizen door Botswana of Namibië ? ")
    print("A: Botswana")
    print("B: Namibië ")
    antwoord = input(": ")
    if antwoord == "a":
        twee()
    elif antwoord == "b":
        drie()
    else: 
        print("Voer een geldig antwoord in. A/B")   

def twee():
    print(" Wat doen jullie ? ")
    print("A: Jullie maken een foto en rijden mee ")
    print("B: Jullie gaan liever niet op de foto en stappen uit ")
    antwoord = input(": ")
    if antwoord == "a":
        zes()
    elif antwoord == "b":
        vier()
    else: 
        print("Voer een geldig antwoord in. A/B")   
