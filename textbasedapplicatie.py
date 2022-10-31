import os



def begin():
    print("welkom bij mijn tekstbased applicatie\n")
    print("Eerst een kleine intro:\n Jij en 2 andere professionele voetballers uit Nigeria, gaan een avondje op stap en worden gedrogeerd, jullie worden wakker in Zuid-Afrika en hebben geen idee heo jullie daar gekomen zijn. Wat jullie wel weten is dat jullie heel snel naar Nederland moeten voor het WK voetbal, maar jullie zijn wel beroofd van al jullie spullen. Dus hoe jullie naar Nederland gaan komen is de vraag... ")
    print("\n")
    beginnen = input("wil je hem spelen? ja/nee ")
    if beginnen == "ja":
        een()
    elif beginnen == "nee":
        print('oke ')


def dood1():
    os.system('clear')
    print("Het vliegtuig daalt steeds sneller en jullie storten neer. De spelers zijn dood en het spel is klaar.\n ")
    print("wil je het spel opnieuw spelen? ja/nee ")
    antwoord = input(": ")
    if antwoord == "ja":
        begin()
    elif antwoord == "nee":
        einde()
    else:
        print("geef een juist antwoord ja/nee") 

def dood2():
    os.system('clear')
    print("In alle haast doen jullie de parachutes om, maar hebben eigenlijk nog nooit een parachute gebruikt. Jullie springen uit het vliegtuig. De parachutes gaan niet open en jullie vallen neer. De spelers zijn dood en het spel is klaar.\n ")
    print("wil je het spel opnieuw spelen? ja/nee ")
    antwoord = input(": ")
    if antwoord == "ja":
        begin()
    elif antwoord == "nee":
        einde()
    else:
        print("geef een juist antwoord ja/nee") 

def dood3():
    os.system('clear')
    print("Tijdens de reis naar Egypte worden jullie aangehouden bij de grens van Zuid-Soedan. De politie is niet blij met jullie en vraagt om jullie legitimatie. Maar die hebben jullie niet en worden meegenomen naar het bureau. Hier worden jullie vast gehouden en zitten jullie 4 weken vast en missen het WK voetbal... het spel is afgelopen   ")
    print("wil je het spel opnieuw spelen? ja/nee ")
    antwoord = input(": ")
    if antwoord == "ja":
        begin()
    elif antwoord == "nee":
        einde()
    else:
        print("geef een juist antwoord ja/nee") 

def einde():
    os.system('clear')
    print("Bedankt voor het spelen van mijn tekstbased applicatie! ")



def einde1():
    os.system('clear')
    print("De keeper blijft staan in het midden en Nigeria heeft het WK voetbal GEWONNEN!!!! De spelers zijn veilig en Nigeria heeft het WK gewonnen dus is het spel klaar.\n  Bedankt voor het spelen van mijn tekstbased applicatie! ")

def einde2():
    os.system('clear')
    print("Jullie komen aan in Rome maar jullie gaan het niet meer halen om op tijd te komen voor het WK voetbal. je hebt het einde niet gehaald")
    print("wil je het spel opnieuw spelen? ja/nee ")
    antwoord = input(": ")
    if antwoord == "ja":
        begin()
    elif antwoord == "nee":
        einde()
    else:
        print("geef een juist antwoord ja/nee") 

def einde3():
    print("Na de medische check komen jullie erachter dat jullie nog niet kunnen spelen. Het Nigeriaanse elftal ligt erin de voorrondes uit... het spel is klaar ")
    print("wil je het spel opnieuw spelen? ja/nee ")
    antwoord = input(": ")
    if antwoord == "ja":
        begin()
    elif antwoord == "nee":
        einde()
    else:
        print("geef een juist antwoord ja/nee") 

def einde4():
    print("Jullie gaan meteen trainen en raken meteen geblesseerd einde opdracht ")
    print("wil je het spel opnieuw spelen? ja/nee ")
    antwoord = input(": ")
    if antwoord == "ja":
        begin()
    elif antwoord == "nee":
        einde()
    else:
        print("geef een juist antwoord ja/nee") 






def een():
    os.system('clear')
    print("Gaan jullie reizen door Botswana of Namibië ? ")
    print("A: Botswana")
    print("B: Namibië ")
    antwoord = input(": ")
    if antwoord == "a":
        twee()
    elif antwoord == "b":
        veertien()
    else: 
        print("Voer een geldig antwoord in. A/B")   

def twee():
    os.system('clear')
    print("\n")
    print("Jullie komen iemand tegen die jullie herkend en biedt jullie een lift aan richting Botswana \n ")
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

def drie ():
    os.system('clear') 
    print('\n')
    print('De man brengt jullie naar Botswana maar moet zelf door naar Soedan, hij biedt jullie aan om nog mee te rijden maar op een voorwaarde... Hij wilt een foto met jullie 3 voor zijn zoons  ')
    print('Wat doen jullie ')
    print('A: Jullie maken een foto en rijden mee ')
    print('B: Jullie gaan liever niet op de foto en stappen uit')
    antwoord = input(': ')
    if antwoord == "a":
        ()
    elif antwoord == "b":
        ()
    else: 
        print("Voer een geldig antwoord in. A/B") 

def vier ():
    os.system('clear') 
    print('\n')
    print("Jullie zijn in Botswana Jullie lopen langs een vuilnisbelt en zien dat er veel auto’s staan en besluiten met de mensen die daar werken te gaan praten en jullie verhaal uitleggen. Hij zegt dat hij nog wel een auto heeft staan die niemand gebruikt en dat jullie die wel kunnen gebruiken. “Ja die auto’s worden toch nooit meer gebruikt dus pak deze maar” jullie zijn erg blij en willen de man eigenlijk bedanken maar hebben nog maar een klein beetje geld. ")
    print("\n")
    print(' Wat doen jullie? ')
    print('A: Bedanken de man maar houden jullie laatste geld ')
    print('B: Jullie geven de man een beetje geld als bedankje')
    antwoord = input(': ')
    if antwoord == "a":
        zes()
    elif antwoord == "b":
        zes()
    else: 
        print("Voer een geldig antwoord in. A/B")  


def vijf ():
    os.system('clear') 
    print('\n')
    print('Jullie lopen door Zuid-Afrika richting het noorden... Jullie lopen langs een vuilnisbelt en zien dat er veel auto’s staan en besluiten met de mensen die daar werken te gaan praten en jullie verhaal uitleggen. Hij zegt dat hij nog wel een auto heeft staan die niemand gebruikt en dat jullie die wel kunnen gebruiken. “Ja die auto’s worden toch nooit meer gebruikt dus pak deze maar” jullie zijn erg blij en willen de man eigenlijk bedanken maar hebben nog maar een klein beetje geld.\n ')
    print('Wat doen jullie?')
    print('A: Bedanken de man maar houden jullie laatste geld')
    print('B: Jullie geven de man een beetje geld als bedankje ')
    antwoord = input(': ')
    if antwoord == "a":
        zes()
    elif antwoord == "b":
        zes()
    else: 
        print("Voer een geldig antwoord in. A/B")   

def zes ():
    os.system('clear') 
    print('\n')
    print('Jullie rijden met de auto richting Soedan en jullie komen aan in Soedan en bedenken hoe jullie zo snel mogelijk naar Nederland kunnen komen. Jullie komen met het plan om ieder geval een slaapplek te regelen voor vanavond. Om ergens te slapen hebben jullie sowieso geld nodig, dus willen jullie wat geld gaan verdienen vandaag. \n ')
    print('Hoe gaan jullie geld verdienen vandaag')
    print('A: Jullie gaan een bal regelen en trucjes doen op een plein voor geld')
    print('B: Jullie gaan auto’s wassen voor geld')
    antwoord = input(': ')
    if antwoord == "a":
        zeven()
    elif antwoord == "b":
        acht()
    else: 
        print("Voer een geldig antwoord in. A/B")   

def zeven ():
    os.system('clear') 
    print('\n')
    print('Na de hele middag op een pleintje ergens in een stadje te hebben gevoetbald, geld hebben opgehaald komt er iemand naar jullie toe die het nieuws heeft gevolgd en heeft gezien dat jullie vermist zijn. Hij vraagt om jullie naam maar weten niet of jullie hem kunnen vertrouwen \n')
    print('Vertrouwen jullie hem')
    print('A: Ja, we geven onze naam  ')
    print('B: Nee, we wachten af wat hij van plan is')
    antwoord = input(': ')
    if antwoord == "a":
        tekst1 ()
    elif antwoord == "b":
        tekst1 ()
    else: 
        print("Voer een geldig antwoord in. A/B")   

def acht():
    os.system('clear') 
    print('\n')
    print('Jullie hebben de hele middag auto’s gewassen en hebben best wel lekker verdiend. Jullie weten niet wat jullie kunnen doen en het begint al later te worden dus moet er wel nagedacht worden over een slaapplek. Tijdens het zoeken naar een slaapplek worden jullie herkend op straat door een vaag, maar wel aardig figuur. Jullie raken aan de praat en hij wil jullie helpen. De man werkt bij een transportbedrijf en zegt dat hij jullie kan helpen om naar Spanje te vliegen. Jullie zijn best wel moe en hebben geen beter plan voor ogen, maar... \n')
    print('Vertrouwen jullie hem')
    print('A: Ja en jullie gaan die avond met de man mee')
    print('B: Nee jullie vertrouwen het niet en bedanken de man voor het aanbod  ')
    antwoord = input(': ')
    if antwoord == "a":
        negen()
    elif antwoord == "b":
        tekst2()
    else: 
        print("Voer een geldig antwoord in. A/B")   



def tekst1(): 
    os.system('clear') 
    print(" Hij belt met de politie in Soedan en de politie komt jullie ophalen en zorgt dat jullie naar naar spanje kunnen vliegen. ")
    print("type 'ja'of 'j' om verder te spelen")
    antwoord = input(": ")
    if  antwoord == "ja": 
        elf() 
    elif antwoord == "j":
        elf()
    else:
        print("typ 'ja' of 'j' om verder te spelen") 



def negen():
    os.system('clear') 
    print('\n')
    print('De man zegt dat ze auto om de hoek staat en jullie gaan met hem mee. Het is een halfuurtje rijden naar het vliegveld waar een groot, oud vrachtvliegtuig staat, maar de man klinkt heel vriendelijk en jullie vertrouwen hem. Jullie willen in het vliegtuig stappen maar aarzelen een beetje ')
    print('Wat doen jullie?')
    print('A: Jullie gaan mee in het vliegtuig')
    print('B: Jullie besluiten om weg te rennen op het laatste moment  ')
    antwoord = input(': ')
    if antwoord == "a":
        tien()
    elif antwoord == "b":
        tekst2()
    else: 
        print("Voer een geldig antwoord in. A/B")   
 
def  tien():
    os.system('clear') 
    print('\n')
    print(' en nemen plaats achter de cockpit. Tijdens het opstijgen komen er wat gekke geluiden over van de motor... en plots valt een motor uit.  jullie beginnen steeds harder neer te storten en het ziet er niet goed uit. Jullie zien nog een optie op overleven en dat is uit het vliegtuig springen met de parachutes  ')
    print('Wat doen jullie?')
    print('A: Jij en de andere blijven zitten')
    print('B: Jullie doen een parachute om te springen ')
    antwoord = input(': ')
    if antwoord == "a":
        dood1()
    elif antwoord == "b":
        dood2()
    else: 
        print("Voer een geldig antwoord in. A/B") 


def tekst2():
    os.system('clear') 
    print("In de stad lopen jullie een beetje levenloos rond het is al avond. Dan lopen jullie langs een politiebureau en besluiten naar binnen te gaan om hulp te vragen. Het verloopt eerst een beetje stroef omdat jullie geen legitimatie hebben, maar ze komen er snel achter wie jullie zijn en ze regelen een vlucht naar Spanje voor de volgende dag ")
    print("type 'ja'of 'j' om verder te spelen")
    antwoord = input(': ')
    if  antwoord == "ja": 
        elf() 
    elif antwoord == "j":
        elf()
    else:
        print("typ 'ja' of 'j' om verder te spelen") 

def  elf():
    os.system('clear') 
    print('\n')
    print('Jullie komen aan in Spanje en de Spaanse politie heeft de Nigeriaanse voetbalbond ge contact. Hun zijn ingelicht en komen jullie ophalen. Jullie worden zo snel mogelijk opgehaald, maar voor dat jullie opgehaald worden. Hebben jullie nog een paar uurtjes in Madrid en besluiten alvast naar het vliegveld te gaan. Op het vliegveld is er heel veel aandacht voor jullie en de pers is aanwezig. Tijdens een interview vraagt iemand van de pers \n ')
    print('“Hoe voelde het voor jullie om de voorbereiding op het WK te missen en dus heel laat zijn en eventueel niet kunnen spelen”\n ')
    print('A: Het was een hel om niet te kunnen voorbereiden, we voelen ons nog niet helemaal fit, maar met de korte tijd die we hebben moet het denk ik wel goed komen.')
    print('B: Buiten wat er is gebeurd natuurlijk, was het wel een avontuurlijke reis en hebben we er eigenlijk wel van genoten en gelukkig overleefd ')
    antwoord = input(': ')
    if antwoord == "a":
        twaalf()
    elif antwoord == "b":
        twaalf()
    else: 
        print("Voer een geldig antwoord in. A/B")


def  twaalf():
    os.system('clear') 
    print('\n')
    print('Jullie stappen en vliegtuig in en komen aan in Nederland. De coach is blij om jullie te zien en laat jullie meteen medisch checken. Na een anderhalve week voorbereiding en heel veel aandacht en interviews begint het WK voetbal en staan jullie in de basis. Jullie bereiken de finale wat voor Nigeriaanse begrippen een erg goed resultaat is. In de finale loopt het uit op penalty’s. Jij moet je penalty nemen \n')
    print('Welke hoek schiet je de penalty? ')
    print('A: links ')
    print('B: rechts')
    antwoord = input(': ')
    if antwoord == "a":
        einde1()
    elif antwoord == "b":
        einde1()
    else: 
        print("Voer een geldig antwoord in. A/B")   


def veertien():
    os.system("clear")
    print('\n')
    print('Jullie lopen richting het noorden naar Namibië en komen bij het eerste kleine stadje in Namibië ‘Warmbad’ jullie verkennen het stadje en zien en zien een klein zielig vrouwtje met haar kinderen op straat zitten ze vraagt om een beetje geld  \n')
    print('Wat doen jullie?')
    print('A: Geven jullie laatste geld aan de vrouw ')
    print('B: Steunen de vrouw maar houden jullie geld ')
    antwoord = input(': ')
    if antwoord == "a":
        vijftien()
    elif antwoord == "b":
        vijftien()
    else: 
        print("Voer een geldig antwoord in. A/B")   

def vijftien():
    os.system("clear")
    print('\n')
    print('Tijdens het lopen komen jullie iemand tegen die jullie herkend en jullie graag helpt. Hij werkt in het kleine haventje van Warmbad en wilt jullie een lift bieden via de boot  ')
    print('Wat doen jullie?')
    print('A: Jullie gaan mee op de boot en varen naar Karasburg')
    print('B: Jullie bedanken de man voor het aanbod maar gaan toch verder te voet Jullie liften en lopen door naar Karasburg   ')
    antwoord = input(': ')
    if antwoord == "a":
        zestien()
    elif antwoord == "b":
        zeventien()
    else: 
        print("Voer een geldig antwoord in. A/B") 

def zestien():
    os.system("clear")
    print('\n')
    print('Jullie komen aan in Karasburg en bedanken de man voor het meevaren. Er is nog geen plan verder, dus jullie slenteren door Karasburg. In de stad vinden jullie een portemonnee liggen op de grond')
    print('Wat doen jullie?')
    print('A: Geven het geld uit aan vervoer naar Egypte ')
    print('B: Geven het geld uit aan eten en water want jullie hebben honger ')
    antwoord = input(': ')
    if antwoord == "a":
        dood3()
    elif antwoord == "b":
        zeventien()
    else: 
        print("Voer een geldig antwoord in. A/B")  

def zeventien():
    os.system("clear")
    print('\n')
    print('Jullie zijn in Karasburg  en bedenken hoe jullie zo snel mogelijk naar Nederland kunnen komen. Jullie komen met het plan om ieder geval een slaapplek te regelen voor vanavond. Om ergens te slapen hebben jullie sowieso geld nodig, dus willen jullie wat geld gaan verdienen vandaag.  ')
    print('Hoe gaan jullie geld verdienen vandaag ')
    print('A: Jullie gaan een bal regelen en trucjes doen op een plein voor geld ')
    print('B: Jullie gaan auto’s wassen voor geld')
    antwoord = input(': ')
    if antwoord == "a":
        achttien()
    elif antwoord == "b":
        achttien()
    else: 
        print("Voer een geldig antwoord in. A/B")  

def achttien():
    os.system("clear")
    print('\n')
    print('Na de hele middag een beetje geld verdiend te hebben komen jullie een man tegen die ziet  dat jullie voetballers zijn en jullie leggen jullie verhaal uit aan deze zeer rijke man en hij wiltja jullie graag helpen en geeft jullie al het geld wat hij bij zich heeft. Jullie bedanken de man. ')
    print('Wat doen jullie met het geld? ')
    print('A: Jullie pakken een bus naar Marokko')
    print('B: Jullie pakken de bus naar Tunesië ')
    antwoord = input(': ')
    if antwoord == "a":
        negentien()
    elif antwoord == "b":
        twintig()
    else: 
        print("Voer een geldig antwoord in. A/B") 

def negentien():
    os.system("clear")
    print('\n')
    print('Aangekomen in Marokko willen meteen door naar Spanje. Jullie gaan naar de boten richting Spanje ')
    print('wat gaan jullie doen?')
    print('A: Jullie verhaal uitleggen totdat er iemand jullie meeneemt. ')
    print('B: Gewoon betalen voor de boot met jullie laatste geld ')
    antwoord = input(': ')
    if antwoord == "a":
        tekst3()
    elif antwoord == "b":
        tekst3()
    else: 
        print("Voer een geldig antwoord in. A/B")  

def tekst3():
    print("Jullie komen aan in Spanje en jullie regelen een lift naar Parijs ")
    print("type 'ja'of 'j' om verder te spelen")
    antwoord = input(": ")
    if  antwoord == "ja": 
        eenentwintig() 
    elif antwoord == "j":
        eenentwintig()
    else:
        print("typ 'ja' of 'j' om verder te spelen") 

def twintig():
    os.system("clear")
    print('\n')
    print('Jullie komen aan in Tunesië en de tijd begint te dringen voor het WK voetbal dus jullie willen snel door en hebben nog wat geld over dus gaan naar het vliegveld.  ')
    print('Waar gaan jullie heen? er is tijdnood!')
    print('A: Parijs')
    print('B: Rome')
    antwoord = input(': ')
    if antwoord == "a":
        eenentwintig()
    elif antwoord == "b":
        einde2()
    else: 
        print("Voer een geldig antwoord in. A/B")   

def eenentwintig():
    os.system("clear")
    print('\n')
    print('Jullie komen aan in Parijs en worden zo snel mogelijk opgehaald, maar voor dat jullie opgehaald worden. Hebben jullie nog een paar uurtjes in Parijs en besluiten alvast naar het vliegveld te gaan. Op het vliegveld is er heel veel aandacht voor jullie en de pers is aanwezig. Jullie komen aan in Nederland en schrikken van hoe plat Nederland is. Ook in Nederland is er heel veel aandacht voor jullie. Het is nieuws in heel Europa dat jullie terug zijn. In Nederland gaan jullie naar het trainingscomplex. ')
    print('Wat gaan jullie doen? ')
    print('A: Eerst een medische check  ')
    print('B: meteen trainen')
    antwoord = input(': ')
    if antwoord == "a":
        einde3()
    elif antwoord == "b":
        einde4()
    else: 
        print("Voer een geldig antwoord in. A/B")   


  
 

  














begin ()
