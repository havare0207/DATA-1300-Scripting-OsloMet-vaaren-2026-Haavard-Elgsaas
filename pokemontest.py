while True:
    user_input = input("Press Enter or Space to continue...")

    if user_input == "" or user_input == " ":
        break
    else:
        print("Only Enter allowed.")


while True:
    user_input = input("Hello, welcome to the world of Pokemon!...")

    if user_input == "" or user_input == " ":
        print("My name is Professor Oke, " \
        "but everyone calls me the Pokemon professor...")
        break
    else:
        print("Only Enter allowed.")


while True:
    gender = input("First, tell me about yourself... are you a boy or a girl?")

    if gender == "boy" or gender == "Boy":
        break
    elif gender == "girl" or gender == "Girl":
        break
    else:
        print("You must write either boy/Boy or girl/Girl.")


while True:
    name = input(f"So, you are a {gender}? What is your name? ")

    #Denne teksten kan inneholde variabler og uttrykk som skal settes inn automatisk.
    #Uten f fungerer ikke {}

    if name == "" or name == " ":
        print("You must write a name.")
    else:
        print(f"So your name is {name}?")
        print("What a nice name!")
        break


while True:
    rival = input("And this is my grandson... what was his name again?")

    if rival == "" or rival == " ":
        print("You must write a name.")
    else:
        print(f"So his name is {rival}?... That was his name!")
        break


while True:
    playerspokemon = input("I let you start to choose your Pokémon... Will you choose Charmander, Squirtle or Bulbasaur?")

#if user_input == "" or user_input == " ":
        #print("You must write a name.")

#user_input finnes ikke, så Python sammenligner aldri det du faktisk skrev inn. 
# Derfor havner koden alltid i else.
#Jeg må derimot bruke playerspokemon.

    if playerspokemon == "" or playerspokemon == " ":
        print("You must write a name.")
    
    elif playerspokemon == "Charmander":
        rivalspokemon = "Squirtle"
        print(f"You choose {playerspokemon}! {rival} picked {rivalspokemon}!")
        print("Welcome to the world of Pokémon!")
        break

    elif playerspokemon == "Squirtle":
        rivalspokemon = "Bulbasaur"
        print(f"You choose {playerspokemon}! {rival} picked {rivalspokemon}!")
        print("Welcome to the world of Pokémon!")
        break

    elif playerspokemon == "Bulbasaur":
        rivalspokemon = "Charmander"
        print(f"You choose {playerspokemon}! {rival} picked {rivalspokemon}!")
        print("Welcome to the world of Pokémon!")
        break

    else :
        print("You must write the name of one of the starter Pokémon, either Charmander, Squirtle or Bulbasaur!")
     
#End of code...

#Endring