#Vybrat pouze z nabídky (1 - 6),
#přepočítat cenu, pokud bude sleva,
#pracovat pouze s křestním jménem,
#zakázat uživatelům mladším 18 let nakupovat,



# vstupni hodnoty
MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
SLEVY = ("Olomouc","Svitavy","Ostrava")
CENY = (150, 200, 120, 120, 100, 180)
domeny = ("seznam.cz","gmail.com","hotmail.com","email.com")

ODDELOVAC = "=" * 35
# uvitani uzivatele
print('VÍTEJTE U NAŠÍ APLIKACE DESTINATIO!')
print(ODDELOVAC)
print('1 - ', MESTA[0], '\t\t| ', CENY[0])
print('2 - ', MESTA[1], '\t\t| ', CENY[1])
print('3 - ', MESTA[2], '\t| ', CENY[2])
print('4 - ', MESTA[3], '\t| ', CENY[3])
print('5 - ', MESTA[4], '\t\t| ', CENY[4])
print('6 - ', MESTA[5], '\t| ', CENY[5])
print(ODDELOVAC)
# vkladani udaju
vyber_lokality = int(input('VYBERTE ČÍSLO LOKALITY: ')) - 1

if vyber_lokality > 5:
    print('Toto město není v nabídce')
    quit()  # Ukončí skript


cele_jmeno = input('CELÉ JMÉNO: ')
jmeno, prijmeni = cele_jmeno.split(' ')


rok_narozeni = int(input('ROK NAROZENÍ: '))

if ((2022 - rok_narozeni) < 18):
    print('Smůla, ještě na to nemáš věk. Ukončuji program.')
    quit()

#ověřovat mailové adresy.
email = input('EMAIL: ')
if ("@" not in email) or (email.split('@')[1] not in domeny):
    print("Neplatný email!")
    quit()

#heslo = input('HESLO: ')
print(ODDELOVAC)


# uprava zadanych hodnot
vybrane_mesto = MESTA[int(vyber_lokality)]
cena_listku = CENY[int(vyber_lokality)]


if vyber_lokality == 2 or vyber_lokality == 3 or vyber_lokality == 5:
    cena = 0.75 * cena_listku
    cena_listku = cena
   # print(cena)




# vypisovani vystupu
print(f"""LÍSTEK DO: {vybrane_mesto} ZA CENU: {cena_listku} 
DĚKUJEME, {jmeno}, NA MAIL: {email} 
VÁM PŘÍJDE KRÁTKÝ DOTAZNÍK A INFORMACE O LÍSTKU """)