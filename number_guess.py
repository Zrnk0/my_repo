import random
top_of_range = input("Type a number: ")

if top_of_range.isdigit(): #isdigit() je funkce, aby zkontroloval, zda je vstup číslo
    top_of_range = int(top_of_range) # převedení proměnné na int

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number larger than 0 next time")
    quit()
random_number = random.randint(0, top_of_range)
print(random_number)


guesses = 0
while True:
    guesses +=1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
       user_guess = int(user_guess)
    else:
        print("Please type a number larger than 0 next time")
        continue
    if user_guess == random_number:
       # print(random_number)
        print("You got it right!")
        break
    elif user_guess != random_number and guesses < 5:
        print("You got it wrong!")
    elif user_guess != random_number and guesses == 5:
        print("I will give you a hint from now on")
        if user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")
    else:
        if user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!") 
        
print("You got it in", guesses, "guesses") 
    
