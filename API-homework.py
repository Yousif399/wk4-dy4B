import requests, json
poke_name= 'pikachu'
url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
response = requests.get(url)
# print(response.json())
if response.ok:
    data = response.json()
    char={}
    char['pok_name']=data['forms'][0]['name']
    char['pok_ability']=(data['abilities'][0]['ability']['name'])
    char['pok_experience']=data['base_experience']
    char['pok_spirit_img']=data['sprites']['front_shiny']
    print(char)
print('****************** \n')
    
poke_name= 'eevee'
url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
response = requests.get(url)
# print(response.json())
if response.ok:
    data = response.json()
    char={}
    char['pok_name']=data['forms'][0]['name']
    char['pok_ability']=(data['abilities'][0]['ability']['name'])
    char['pok_experience']=data['base_experience']
    char['pok_spirit_img']=data['sprites']['front_shiny']
    print(char)
print('****************** \n')
poke_name= 'snorlax'
url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
response = requests.get(url)
# print(response.json())
if response.ok:
    data = response.json()
    char={}
    char['pok_name']=data['forms'][0]['name']
    char['pok_ability']=(data['abilities'][0]['ability']['name'])
    char['pok_experience']=data['base_experience']
    char['pok_spirit_img']=data['sprites']['front_shiny']
    print(char)
print('****************** \n')
poke_name= 'charizard'
url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
response = requests.get(url)
# print(response.json())
if response.ok:
    data = response.json()
    char={}
    char['pok_name']=data['forms'][0]['name']
    char['pok_ability']=(data['abilities'][0]['ability']['name'])
    char['pok_experience']=data['base_experience']
    char['pok_spirit_img']=data['sprites']['front_shiny']
    print(char)
    
   