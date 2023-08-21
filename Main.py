#print welcome
print("Welcome to PyRPG")

#ask for name and gender
print("Let´s start with some questions about you")

gender = int(input("What's your gender? 1 = man 2 = woman "))
name = input("What's your name? ")


#check if name and gender are correct
if gender == 1:
    genderCorrectMan = input("You are man, right? 1 = yes 2 = no ")
    if genderCorrectMan == "2":
        gender = 2
elif gender == 2:
    genderCorrectWoman = input("You are woman, right? 1 = yes 2 = no ")
    if genderCorrectWoman == "2":
        gender = 1
if gender == 1:
    genderWord = "man"
if gender == 2:
    genderWord = "woman"

#ask if the player wants a description of the story

storyDescription = input("Do you want a description of the story? 1 = yes 2 = no ")

#print a story description if the player wants it

if storyDescription == "1":
    print("You are a young", genderWord, ", 14 years old. You live in the UDSSR, in a small village to be exact. The UDSSR want to start a rocket to the mars, and they want a couple of teenagers to go with them. You are applying to be on the rocket. I wish you good luck on your journey to mars. Oh, by thw way, its 2369.")
if storyDescription == "2":
    print("Ok, let's start the game instead.")