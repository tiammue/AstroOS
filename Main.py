import pickle
import math
import random

#print logo and start up text
print("Welcome to AstrOS!")
print("                 __/ o   \\")
print("                / _      |")
print(" _______________\\/_      |__________________")
print("|_____________                  ____________|")
print(" \\_____________     ASTRO      ____________/")
print("  \\ ____________             ____________ /")
print("   \\_______________       _______________/")
print("                   |     |")
print("                   |     |")
print("                   /     \\")
print("                  /       \\")
print("                 |/\\/\\/\\/\\/|")

print("         ©Endboy Interactive Studio 2023")
print("")
print("Loading User Accounts...")

#commented out the code below because it gave an error
#remove the 3 " at the start and end of the error code to uncomment the code
"""


#Load Username with pickle

with open('Save.pkl', 'rb') as f:

    Username_loaded = pickle.load(f) # deserialize using load()
    input = input("The current User is "+ Username_loaded + ". Is this correct? y/n:")

if input == "y":
 Username = Username_loaded
else:
   input = input("Do you wish to erase all data and login? y/n:")
   if input == "y":
    Username = input("Input new username:")
      #there was an "else" here but it gave an error so i removed it

# open a text file

with open('Save.pkl', 'wb') as f:  
    pickle.dump(Username, f) # serialize the list

f.close

with open('Save.pkl', 'rb') as f:

    Username_loaded = pickle.load(f) # deserialize using load()
    print(Username_loaded)

"""
