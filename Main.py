#print welcome
print("Welcome to PyRPG")

#ask for name and gender
gender = int(input("What's your gender? 1 = male 2 = female "))
name = input("What's your name? ")

#check if name and gender are correct
if gender == 1:
    genderCorrectMale = input("You are male, right? 1 = yes 2 = no ")
    if genderCorrectMale == "2":
        gender = 2
elif gender == 2:
    genderCorrectFemale = input("You are female, right? 1 = yes 2 = no ")
    if genderCorrectFemale == "2":
        gender = 1
        
if gender == 1:
    print("Welcome to the world of PyRPG, male", name, "!")
elif gender == 2:
    print("Welcome to the world of PyRPG, female", name, "!")
