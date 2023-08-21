#print welcome
print("Welcome to Pertokia")

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
    print("You are a young", genderWord, ", 14 years old. You live in the Kingdom of Pertokia, in a small village to be exact. The Kingdom of Pertokia wants to start a rocket to Mars, and they want a couple of teenagers to go with them. You are applying to be on the rocket. I wish you good luck on your journey to mars. Oh, by thw way, its 2369.")
if storyDescription == "2":
    print("Ok, let's start the game instead.")

#applying for the rocket

print("The form to apply to the rocket is in front of you.")
print("You have to fill it out. You have to answer 6 questions.")

#first question

print("The first question is: How old are you? You're 14, so you write that down, they said they'd be looking for teenagers, so you're perfect!")

#Second question

print("The second question is: What's your name? You write down", name ,"and you're done with the second question.")

#Third question

print("The third question is: Are you excited about the prospect of going to Mars?")
excitement_answer = input("1 = very excited, 2 = somewhat excited, 3 = unsure, 4 = not excited ")

#Fourth question

print("The fourth question is: Do you have any experience in science or engineering?")
experience_answer = input("1 = a lot, 2 = some, 3 = a little, 4 = none ")

#Fifth question

print("The fifth question is: How do you handle challenges and difficult situations?")
challenge_answer = input("1 = I thrive on challenges, 2 = I can handle them, 3 = I struggle but keep trying, 4 = I get discouraged easily ")

#Sixth question

print("The sixth question is: Did you lie in any of the previous questions?")
lie_answer = input("1 = yes, 2 = no 3 = maybe 4 = I don't know 5 = I don't want to answer 6 = some of them ")