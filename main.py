
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons (by total)")
    print("3. Top 10 weakest pokemons (by total)")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        pokemon_index = int(input("Which pokemon would you like to see?"))
        print(pokemons[pokemon_index])
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        pass
    elif choice == '2':
        def sorting(pokemons_strong):
            return int(pokemons_strong["total"])
        pokemons.sort(key = sorting, reverse = True)
        print(pokemons[0:10])

        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        def sorting(pokemons_weak):
            return int(pokemons_weak["total"])
        pokemons.sort(key = sorting)
        print(pokemons[0:10])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        computer_choice = random.randint(1,43)
        player_choice = int(input("Which pokemon would you like to choose?"))
        player_health = int(pokemons[player_choice].get("total"))
        computer_health = int(pokemons[computer_choice].get("total"))
        while player_health > 0 and computer_health > 0:
            player_damage = pokemons[player_choice].get("attack") - pokemons[computer_choice].get("defense") + random.randint(5,20)
            computer_damage = pokemons[computer_choice].get("attack") - pokemons[player_choice].get("defense") + random.randint(5,20)
            player_health = player_health - computer_damage
            computer_health = computer_health - player_damage
            print("Computer health left: ", computer_health)
            print("Player health left: ", player_health)


        
        

        
        
        

        

            
            

        # Battle
        # 
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health (total) - lost
        pass

    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")


