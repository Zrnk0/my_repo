welcome = 'Welcome to my computer quiz!'
print(welcome)
print('='*len(welcome))
print('')

playing = input("Do you want to play? ").lower()
print(playing)
if playing != "yes":
    quit()
    
print("Okay! Let's play :) ")
i = 0
count_answers = 0
answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    count_answers+=1
    print("Correct!")
    i+=1
    
else:
    print("Incorrect!")

answer = input("What does GPU snads for? ").lower()
count_answers+=1
if answer == "graphics processing unit":
    
    print("Correct!")
    i+=1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
count_answers+=1
if answer == "random access memory":
    
    print("Correct!")
    i+=1
else:
    print("Incorrect!")

answer = input("What does PSU stant for? ").lower()
count_answers+=1
if answer == "power supply":
    
    print("Correct!")
    i+=1
else:
    print("Incorrect!")


print("You have " + str(int(i/count_answers*100)) + "% score")
