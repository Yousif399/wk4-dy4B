import requests, json
# print(response.json())
def pokemon_info(name):
    poke_name = name
    url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        char={}
        char['pok_name']=data['forms'][0]['name']
        char['pok_ability']=(data['abilities'][0]['ability']['name'])
        char['pok_experience']=data['base_experience']
        char['pok_spirit_img']=data['sprites']['front_shiny']
        return(char)
print(pokemon_info('pikachu'))
print(pokemon_info('charizard'))
print(pokemon_info('eevee'))
print(pokemon_info('snorlax'))
print(pokemon_info('joseph'))


print('****************** \n')
