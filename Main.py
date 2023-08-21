#print welcome
print("Welcome to PyRPG")

#ask for name and gender

gender = input("What´s your gender? 1 = male 2 = female ")
name = input("What´s your name? ")

#check if name and gender are correct

if gender == 1:
<<<<<<< HEAD
   genderCorrectMale=input("You are male, right? 1 = yes 2 = no ")
if genderCorrectMale == 2:
    gender = 2
if gender == 2:
    genderCorrectFemale=input("You are female, right? 1 = yes 2 = no ")
if genderCorrectFemale == 2:
    gender = 1
=======
<<<<<<< HEAD
    gendercorrect=input("You are male, right? 1 = yes 2 = no")

=======
    print("You are male, right?")
    input("Press 1 to confirm")
    
>>>>>>> e4c4fefac4dfb156b5636c81fcb55150e0d45752
>>>>>>> 722baa9fd6e8afaff87b2b239a1a88687026af20


print("Welcome to the world of PyRPG.", name, "!")