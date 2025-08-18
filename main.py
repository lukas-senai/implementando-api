"""
Projeto - Consumindo a PokéAPI
"""

import requests  # biblioteca para fazer requisições HTTP

"""
Retorna apenas o nome do Pokémon.
(Função completa para exemplo)
"""
def buscar_nome(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        return dados["name"]
    else:
        return None

"""
Retorna o peso do Pokémon.
"""
def buscar_peso(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        # pegar o peso do pokemon, salvar na variável peso e retornar
        return peso
    else:
        return None


"""
# Retorna a primeira habilidade do Pokémon.
"""
def buscar_primeira_habilidade(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        # pegar o nome da primeira habilidade do pokemon, salvar na variável habilidade e retornar
        return habilidade
    else:
        return None


"""
Retorna os tipos do Pokémon (ex: fogo, água, planta).
"""
def buscar_tipos(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    response = requests.get(url)

    # completar

"""
Desafio:
Criar uma função chamada buscar_altura(pokemon) que retorne a altura
do Pokémon. A lógica é parecida com as outras funções já existentes.
"""

if __name__ == "__main__":
    print("=== Consulta PokéAPI ===")

    pokemon = input("Digite o nome de um Pokémon: ")

    print("Nome:", buscar_nome(pokemon))
    print("Peso:", buscar_peso(pokemon))
    print("Primeira habilidade:", buscar_primeira_habilidade(pokemon))
    print("Tipos:", buscar_tipos(pokemon))

    # TODO: criar e chamar a função buscar_altura
    # print("Altura:", buscar_altura(pokemon))
