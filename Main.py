import pickle

#print logo

print("                   ")
print("                    _____")
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

#Load Username with pickle

with open('Save.pkl', 'rb') as f:

    Username_loaded = pickle.load(f) # deserialize using load()
    input = input("The current User is "+ Username_loaded + ". Is this correct? y/n:")

if input = "y":
 Username = Username_loaded
else:
   input = input("Do you wish to erase all data and login? y/n:")
   if input = "y":
    Username = input("Input new username:")
   else:
      



with open('Save.pkl', 'wb') as f:  # open a text file
    pickle.dump(Username, f) # serialize the list

f.close

with open('Save.pkl', 'rb') as f:

    Username_loaded = pickle.load(f) # deserialize using load()
    print(Username_loaded)