# 📘 Projeto PokéAPI

## 🔎 O que é uma API?
API significa **Application Programming Interface** (Interface de Programação de Aplicações).  
É um conjunto de **regras e padrões** que permitem que diferentes softwares se comuniquem entre si.

➡️ Em outras palavras: uma API é como um **garçom em um restaurante**:
- Você (usuário) faz um pedido.  
- O garçom (API) leva seu pedido para a cozinha (sistema).  
- A cozinha prepara a comida (dados).  
- O garçom traz a comida pronta para você.  

Assim, você **não precisa entrar na cozinha** nem entender como tudo funciona por dentro.  

---

## 🎯 Para que serve uma API?
- **Acessar dados externos** (ex.: clima, notícias, vídeos, estatísticas).  
- **Integrar sistemas** (ex.: integrar um app de delivery com sistemas de pagamento).  
- **Automatizar processos** (ex.: bots, relatórios automáticos).  
- **Desenvolver novas aplicações** aproveitando dados já disponíveis.  

---

## 🐱‍👓 O que é a PokéAPI?
A [PokéAPI](https://pokeapi.co/) é uma API pública que fornece dados do universo Pokémon.  
Com ela, podemos consultar:  
- Nome, peso e altura dos Pokémon.  
- Habilidades e tipos.  
- Imagens e evoluções.  

Exemplo de requisição:  
```
https://pokeapi.co/api/v2/pokemon/pikachu
```
Retorna um **JSON** com todas as informações do Pikachu.  

---

## 🖥️ O que nosso código faz?
Nosso projeto é um **programa em Python** que:  
1. Permite ao usuário digitar o nome de um Pokémon.  
2. Consulta a PokéAPI.  
3. Mostra informações como nome, peso, habilidades e tipos.  

👉 O código foi feito em formato **esqueleto**, com algumas funções incompletas para os alunos praticarem.

---

## ⚙️ Como rodar o projeto
### 1. Instalar dependências
O projeto usa a biblioteca `requests`.  
Instale com:
```bash
pip install -r requirements.txt
```

### 2. Executar o programa
```bash
python main.py
```

### 3. Exemplo de uso
```
=== Consulta PokéAPI ===
Digite o nome de um Pokémon: pikachu

Nome: pikachu
Peso: 60
Primeira habilidade: static
Tipos: ['electric']
```

---

## 📜 Estrutura do Código
### Funções disponíveis
- `buscar_nome(pokemon)` → já implementada (exemplo pronto).  
- `buscar_peso(pokemon)` → deve ser completada.  
- `buscar_primeira_habilidade(pokemon)` → deve ser completada.  
- `buscar_tipos(pokemon)` → deve ser completada.  
- `buscar_altura(pokemon)` → desafio: criar do zero.  

---

## 📚 Explicando o código
Trecho principal:
```python
url = BASE_URL + pokemon.lower()
response = requests.get(url)
```
➡️ Monta a URL e faz a requisição.  

```python
if response.status_code == 200:
    dados = response.json()
```
➡️ Verifica se deu certo (status 200 = sucesso) e transforma a resposta em um **dicionário Python**.  

```python
habilidade = dados["abilities"][0]["ability"]["name"]
```
➡️ Acessa a primeira habilidade do Pokémon dentro do JSON.  

```python
tipos = [t["type"]["name"] for t in dados["types"]]
```
➡️ Usa **list comprehension** para listar todos os tipos (ex.: fogo, água).  

---

## 🏆 Desafios sugeridos
1. Implementar a função `buscar_altura(pokemon)`.  
2. Mostrar **todas as habilidades**, não apenas a primeira.  
3. Exibir a **imagem do Pokémon** (campo `sprites["front_default"]`).  
4. Criar um loop para consultar **vários Pokémon seguidos**.  
5. Criar um menu interativo para o usuário escolher o que deseja consultar.  

---

## 🤔 Por que isso é importante?
- Entender como funciona uma API é **fundamental** para desenvolvedores modernos.  
- Quase todos os sistemas atuais dependem de **integração com outros serviços**.  
- Esse projeto mostra como **consumir dados reais da internet** de forma simples e prática.
