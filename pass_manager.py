from cryptography.fernet import Fernet

master_pwd = input("Nastav hlavní heslo: ")



def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
def stare():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)
            #    print(line.rstrip())#rstrip zredukuje \n v textu

def nove():
    name = input("Jméno účtu: ")
    pwd = input("Heslo: ")

    with open("passwords.txt", "a") as f: #as f znamená název proměnné s kterou můžeme později pracovat ... f.write(), f.read(),...
    # s použitím with se nemusíme starat o zavření,
    #"w" --> write mode, vždycky přepíše náš file, "r" --> reda mode, jen pro čtení, "a" --> append mode, tedy připojí něco na konec filu, případně vytvoří nový, když file neexistuje
    # soubor se po použití sám zavře, jinak by byla syntax takto: file = open("xxxx.txt", "a") a na dalším řádku file.close()
        f.write(name + '|' + pwd + '\n')


while True:
    mode = input("Chceš přidat nové heslo, nebo vidět existující? (nove/stare), zmáčkni q pro konec: ").lower()

    if mode == "q":
        break
    if mode == "stare":
        stare()
    elif mode == "nove":
        nove()
    else:
        print("Neplatné")
        continue
