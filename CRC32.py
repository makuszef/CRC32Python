
def zapisz_crc_plik(crc): #dopisz crc do pliku
    tmp = ""
    for x in crc:
        tmp += str(x)
    nazwa_pliku = input("Podaj nazwe pliku do ktorego zostanie dopisane crc: ")
    nazwa_pliku += ".txt"
    try:
        filetest = open(nazwa_pliku, "a")
    except:
        print("Problem z otwarciem pliku")
        exit()
    filetest.write(tmp)
    filetest.close()

def zapisz_dane_plik(tmp): #przepisz dane w formie binarnej z pliku wejsciowego do pliku crc.txt
    nazwa_pliku = input("Podaj nazwe pliku do ktorego zostana zapisane dane: ")
    nazwa_pliku += ".txt"
    try:
        filetest = open(nazwa_pliku, "w")
    except:
        print("Problem z otwarciem pliku")
        exit()
    filetest.write(tmp)
    filetest.close()
def oblicz_crc(wielomian_generujacy,uzupelniony_wektor_informacyjny, ROZMIAR_WIELOMANU_GENERUJACEGO):
    while (len(uzupelniony_wektor_informacyjny) > ROZMIAR_WIELOMANU_GENERUJACEGO - 1):
        for i in range(ROZMIAR_WIELOMANU_GENERUJACEGO):
            uzupelniony_wektor_informacyjny[i] = (uzupelniony_wektor_informacyjny[i] + wielomian_generujacy[i]) % 2 #dodawanie modulo 2 odpowiednich bitow
        for i in range(ROZMIAR_WIELOMANU_GENERUJACEGO):
            if (i < len(uzupelniony_wektor_informacyjny) and len(uzupelniony_wektor_informacyjny) > ROZMIAR_WIELOMANU_GENERUJACEGO - 1):
                if (uzupelniony_wektor_informacyjny[0] == 0): #usun z listy zerowe bity zaczynajac od poczatku listy do napotkania 1
                    uzupelniony_wektor_informacyjny.pop(0)
                else:
                    break
    return uzupelniony_wektor_informacyjny #zwroc crc
def sprawdz_integralnosc(wielomian_generujacy, ROZMIAR_WIELOMANU_GENERUJACEGO):
    wektor_z_pliku = []
    nazwa_pliku = input("Podaj nazwe pliku dla ktorego zostanie sprawdzona integralnosc danych dane w postacji binarnej: ")
    nazwa_pliku += ".txt"
    try:
        f = open(nazwa_pliku, "r")
    except:
        print("Problem z otwarciem pliku")
        exit()
    mytext = f.read()
    for mychar in mytext: #czytaj z pliku
        if (mychar not in ['0', '1']):
            print("Plik nie ma odpowiedniego formatu")
            exit()
        wektor_z_pliku.append(int(mychar))
    f.close()
    crc = oblicz_crc(wielomian_generujacy, wektor_z_pliku, ROZMIAR_WIELOMANU_GENERUJACEGO)
    if (sum(crc) == 0): #sprawdz czy crc wynosi 0
        print("Nie doszlo do przeklaman danych")
    else:
        print("Doszlo do przeklaman danych")

#main function
ROZMIAR_WIELOMANU_GENERUJACEGO =33
wektor_z_pliku = []
nazwa_pliku = input("Podaj nazwe pliku ktory zostanie przekonwertowany: ")
nazwa_pliku += ".txt"
try:
    f = open(nazwa_pliku, "r") # otworz plik z ktorego proces bedzie czytal znaki
except:
    print("Problem z otwarciem pliku")
    exit()

mytext = f.read() #czytaj z pliku
tmp = ""
for mychar in mytext:
    for mybin in bin(ord(mychar))[2:-1]: # zamien na zapis binarny usun '0b'
        wektor_z_pliku.append(int(mybin))
        tmp += mybin

crc = []
wielomian_generujacy = []
for i in range(ROZMIAR_WIELOMANU_GENERUJACEGO): #wypelnij zerami liste crc i wielomian generujacy
    wielomian_generujacy.append(0)
    crc.append(0)
crc.pop() #usun element z crc
#wielomian generujacy CRC-32-IEEE 802.3, RCR-32 CCITT x^32+x^26+x^23+x^22+x^16+x^12+x^11+x^10+x^8+x^7+x^5+x^4+x^2+x+1
for i in range(ROZMIAR_WIELOMANU_GENERUJACEGO): #wypelnij wielomian generujacy
    if i in [0, 1, 2, 4, 5, 7, 8, 10, 11, 12, 16, 22, 23, 26, 32]:
        wielomian_generujacy[i] = 1
    else:
        wielomian_generujacy[i] = 0

for x in crc: #uzupelnij wektor o zerowe crc
    wektor_z_pliku.append(0)
zapisz_dane_plik(tmp) #odkomentowanie jesli nie dodalismy crc
zapisz_crc_plik(oblicz_crc(wielomian_generujacy, wektor_z_pliku, ROZMIAR_WIELOMANU_GENERUJACEGO)) #odkomentowanie jesli nie dodalismy crc
sprawdz_integralnosc(wielomian_generujacy, ROZMIAR_WIELOMANU_GENERUJACEGO)