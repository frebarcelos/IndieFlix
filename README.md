# 🎬 IndieFlix

**IndieFlix** é uma aplicação em Python com interface de terminal voltada para o gerenciamento de um catálogo de filmes. Com um toque divertido e nostálgico, traz menus interativos com animações em ASCII e opções para manipular uma lista de filmes salvos em JSON.

## ✨ Funcionalidades

- 📜 Listar todos os filmes do catálogo
- ➕ Adicionar novos filmes
- ✏️ Editar informações de um filme existente
- ❌ Excluir filmes
- 🔍 Buscar filmes por título, diretor ou gênero
- 💾 Persistência dos dados em arquivo JSON (`filmes.json`)
- 🎭 Animações em ASCII para tornar a experiência mais envolvente

## 📁 Estrutura do Projeto

IndieFlix/
├── menu.py # Script principal com o menu interativo
├── filmes.py # Classe Filme e persistência dos dados
├── catalogo.py # Lógica para adicionar, editar, excluir e listar filmes
├── busca.py # Funções de busca por filmes
├── funcutils.py # Funções utilitárias (validação de opções)
├── filmes.json # Base de dados local de filmes
├── view/
│ └── animacao.py # Funções de animação e estética no terminal

bash
Copiar
Editar

## ▶️ Como Executar

1. Clone o repositório:


git clone https://github.com/frebarcelos/IndieFlix.git
cd IndieFlix

Execute o projeto (Python 3.10+ recomendado):

python menu.py

Certifique-se de que o arquivo filmes.json esteja no mesmo diretório. Caso não exista, ele será criado automaticamente.

🛠️ Tecnologias Utilizadas
Python 3

ASCII Art para interface divertida

Armazenamento em JSON

Programação modular

📜 Licença
Este projeto está licenciado sob a MIT License.

👤 Autor
Desenvolvido por Frederico Barcelos

💼 Projeto pessoal com fins educacionais e diversão
