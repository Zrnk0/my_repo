import random
pozdrav = "Vítej ve hře kámen, papír, nůžky"
print(pozdrav+"\n"+"="*len(pozdrav))
user_wins = 0
computer_wins = 0
options = ["kámen", "papír", "nůžky"]
user_input_rock = 0
user_input_paper = 0
user_input_scissors = 0
pc_input_rock = 0
pc_input_paper = 0
pc_input_scissors = 0 

# Když uživatel vybere stejnou možnost víckrát po sobě, print nějakou zprávu, když vybere něco jiného, vynuluj counter
while True:
    user_input = input("Napiš kámen/papír/nůžky abys hrál, nebo q pro ukončení: ").lower()
    print("="*len("Napiš kámen/papír/nůžky abys hrál, nebo q pro ukončení: "+user_input))

    if user_input == "q":
        print("Skončil jsi!")
        break
    if user_input not in ["kámen", "papír", "nůžky"]:
        print("Příště vyber správně!")
        continue
    random_number = random.randint(0,2) # vyber číslo mezi 0-2 --> toto číslo pak odpovídá listu options
    computer_pick = options[random_number]
    print("Počítač vybral",computer_pick + ".")

    if user_input == "kámen":
        user_input_rock += 1
    if computer_pick == "kámen":
        pc_input_rock += 1
    if user_input == "papír": 
        user_input_paper += 1
    if computer_pick == "papír":
        pc_input_paper += 1
    if user_input == "nůžky": 
        user_input_scissors += 1
    if computer_pick == "nůžky":
        pc_input_scissors += 1

        
    if user_input == "kámen" and computer_pick == "nůžky":

        print("Vyhrál jsi!")
        print("="*len("Napiš kámen/papír/nůžky abys hrál, nebo q pro ukončení: "+user_input))
        user_wins += 1
        
    
    elif user_input == "papír" and computer_pick == "kámen":

        print("Vyhrál jsi!")
        print("="*len("Napiš kámen/papír/nůžky abys hrál, nebo q pro ukončení: "+user_input))
        user_wins += 1
        
        
    elif user_input == "nůžky" and computer_pick == "papír":
    
        print("Vyhrál jsi!")
        print("="*len("Napiš kámen/papír/nůžky abys hrál, nebo q pro ukončení: "+user_input))
        user_wins += 1
    elif user_input == computer_pick:
        print("Je to remíza, nikdo nedostane bod")
        print("="*len("Napiš kámen/papír/nůžky abys hrál, nebo q pro ukončení: "+user_input))
    else:
        print("Prohrál jsi!")
        print("="*len("Napiš kámen/papír/nůžky abys hrál, nebo q pro ukončení: "+user_input))
        computer_wins += 1

print("Hra skončila, tady máš výsledky:")
if user_wins == computer_wins:
    print("Je to remíza!")
elif user_wins > computer_wins:
    win = int(user_wins) - int(computer_wins)
    if win == 1:
        print("Vyhrál jsi o: " + str(win), "bod!")
        print("Skoro tě měl! ;)")
    elif win > 1 and win <= 4:
        print("Vyhrál jsi o: " + str(win), "body!")
        print("Tohle celkem ujde! ;)")
    else:
        print("Vyhrál jsi o: " + str(win), "bodů!")
        print("S takovým štestím si běž rovnou vsadit! ;)")
elif user_wins < computer_wins:
    win = int(computer_wins) - int(user_wins)
    if win == 1:
        print("Počítač vyhrál o: " + str(win), "bod!")
        print("Chyběl kousek ;)")
    elif win > 1 and win <= 4:
        print("Počítač vyhrál o: " + str(win), "body!")
        print("Příště se víc snaž ;)")
    else:
        print("Počítač vyhrál o: " + str(win), "bodů!")
        print("S takovou smůlou ani nevycházej z domu! ;)")

print("Tvoje statistika je: ","Kámen: " + str(user_input_rock),"Papír: " + str(user_input_paper),"Nůžky: " + str(user_input_scissors))
print("PC statistika je:    ","Kámen: " + str(pc_input_rock),"Papír: " + str(pc_input_paper),"Nůžky: " + str(pc_input_scissors))
