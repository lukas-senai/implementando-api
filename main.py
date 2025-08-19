import requests
import webbrowser

print(r"""
 ██████╗  ██████╗ ██╗  ██╗███████╗██████╗ ███████╗██╗  ██╗
 ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗██╔════╝╚██╗██╔╝
 ██████╔╝██║   ██║█████╔╝ █████╗  ██║  ██║█████╗   ╚███╔╝ 
 ██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝  ██║  ██║██╔══╝   ██╔██╗ 
 ██║     ╚██████╔╝██║  ██╗███████╗██████╔╝███████╗██╔╝ ██╗
 ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝
""")

def mostrar_nome(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        print("Nome:", dados["name"])
    else:
        print("Pokémon não encontrado!")
        return None

# Função pela metade
def mostrar_peso(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        # peso = 

# Crie a função para mostrar a altura

# Outra função pela metade
def mostrar_habilidades(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        # Exibir todas as habilidades do pokemon.
        # Dica: elas estão na lista dados["abilities"]
        
def mostrar_imagem(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        imagem_url = dados["sprites"]["front_default"]
        print("Imagem:", imagem_url)
        webbrowser.open(imagem_url)

def mostrar_evolucoes(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    response = requests.get(url)
    if response.status_code != 200:
        return
    dados = response.json()

    # 1. Buscar species para pegar a URL da evolution_chain
    species_url = dados["species"]["url"]
    response = requests.get(species_url)
    if response.status_code != 200:
        print("Não foi possível buscar informações da espécie.")
        return
    
    species_data = response.json()
    evolution_url = species_data["evolution_chain"]["url"]

    # 2. Buscar a cadeia evolutiva
    response = requests.get(evolution_url)
    if response.status_code != 200:
        print("Não foi possível buscar a cadeia evolutiva.")
        return

    chain = response.json()["chain"]

    # 3. Percorrer a cadeia de evoluções
    evolucoes = []
    atual = chain
    while atual:
        evolucoes.append(atual["species"]["name"])
        if atual["evolves_to"]:
            atual = atual["evolves_to"][0]
        else:
            atual = None

    print("Evoluções:", " ➝ ".join(evolucoes))

def menu():
    pokemon = input("Digite o nome do Pokémon que deseja pesquisar: ")

    while True:
        print(f"\n=== POKÉDEX: {pokemon.upper()} ===")
        print("1 - Mostrar nome")
        print("2 - Mostrar peso")
        print("3 - Mostrar altura")
        print("4 - Mostrar habilidades")
        print("5 - Mostrar imagem")
        print("6 - Mostrar evoluções")
        print("7 - Pesquisar outro Pokémon")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Saindo da Pokédex...")
            break
        elif escolha == "1":
            mostrar_nome(pokemon)
        elif escolha == "2":
            mostrar_peso(pokemon)
        elif escolha == "3":
            mostrar_altura(pokemon)
        elif escolha == "4":
            mostrar_habilidades(pokemon)
        elif escolha == "5":
            mostrar_imagem(pokemon)
        elif escolha == "6":
            mostrar_evolucoes(pokemon)
        elif escolha == "7":
            pokemon = input("Digite o nome de outro Pokémon: ")
        else:
            print("Opção inválida!")

menu()
