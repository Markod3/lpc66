import requests
#
# Nombre: Marco Antonio Hernandez Iracheta
# Matricula: 1568448
# Script en python que consulta el api de pokemon
# para listar los nombres de pokemon pero se le agrego
# interaccion para que listaras mas pokemon segun se vaya requiriendo
# Contribuyo: Marco Hernandez
# 08/09/2022
def get_pokemon (url='http://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset':offset} if offset else{}

    response = requests.get(url, params=args)

    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results',[])

        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)
        next = input ("Continuar listando? [Y/N]").lower()
        if next == 'y':
            get_pokemon(offset=offset+20)
if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon-form/'
    get_pokemon()
