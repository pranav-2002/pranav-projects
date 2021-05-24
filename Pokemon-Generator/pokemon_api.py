'''POKEMON GENERATOR'''

import requests

# API
url = 'https://pokeapi.co/api/v2/pokemon/'

# Checking the status code
if (requests.get(url).status_code == 200):

    while(True):
        # Getting the input from user
        user_input = input("Enter A Pokemon (or 'q' to quit): ").lower()
        if user_input == "q":
            print()
            print("____Thank You For Using This Application____")
            break
        updated_url = url+user_input
        try:
            # DATA extraction
            json_data = requests.get(updated_url).json()

            pokemon_name = json_data['forms'][0]['name']
            pokemon_ability = json_data['abilities'][1]['ability']['name']
            effects_url = json_data['abilities'][0]['ability']['url']
            effects_json = requests.get(effects_url).json()
            pokemon_effect = effects_json['effect_entries'][1]['effect']
            pokemon_exp = json_data['base_experience']
            pokemon_height = json_data['height']
            pokemon_type = json_data['types'][0]['type']['name']

            # Printing the data
            print("______________POKEMON INFO_______________")

            print("\nPokemon Name: ", pokemon_name)
            print("\nPokemon Type: ", pokemon_type)
            print("\nPokemon Height(m): ", pokemon_height)
            print("\nPokemon Experience: ", pokemon_exp)
            print("\nPokemon Ability: ", pokemon_ability)
            print("\nPokemon Ability Effect: ", pokemon_effect)
            print("__________________________END__________________________________")
            print()
        except:
            print()
            print("___Pokemon Does Not Exist___")

else:
    print("SORRY, THE API IS BROKEN")
