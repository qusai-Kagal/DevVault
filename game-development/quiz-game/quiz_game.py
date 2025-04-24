print("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's start the game.")
score = 0

answer = input("What does the CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'central processing unit'.")

answer = input("What does the GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'graphics processing unit'.")

answer = input("What does the RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'random access memory'.")

answer = input("What does the ROM stand for? ")
if answer.lower() == "read-only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'read-only memory'.")

answer = input("What does the PS stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is power supply'.")

print("You got " + str(score) + " out of 5 questions correct!")
print("Your score is " + str((score / 5) * 100) + "%")
print("Thanks for playing!")