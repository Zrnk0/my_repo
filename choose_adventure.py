import random

user_name = input("Type name of your character: ")
print("Welcome", user_name, "to this adventure!")

answer = input("""You are on a dirt road, it has come to an end and you can go left or right
               Where do youu want to go? """).lower()

if answer == "left":
    answer = input("You come to a river, you can walk around or swim accross. Type walk to walk around and swim to swim ")

    if answer == "swim":
        print("Crocodiles ate you, didn't I tell you about them?)
    elif answer == "walk":
        print("You came acros )
    else:
        print("You loose again")
elif answer == "right":
    print()
else:
    print("You tried to go your way, but you got badly injured and you died")
