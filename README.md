# 🌌 O Despertar em Etherion - RPG CODEX

Um RPG de terminal desenvolvido em Python, com lore original, combate por turnos, gerenciamento de inventário e progressão narrativa interativa. Tudo isso com um sistema completo de fichas, evolução, atributos e criptografia de usuários.

---

## 🧩 Sobre o Projeto

**O Despertar em Etherion** é um jogo inspirado em estruturas clássicas de RPG, ambientado em uma torre ciberfantástica onde o jogador — um Eco, uma consciência digital — precisa desvendar enigmas e sobreviver a perigos para alcançar os andares finais.

> "Você não é carne, nem alma. É código, memória, ruído. E Etherion observa..."

---

## 🎮 Como Jogar

### ✅ Requisitos

- Python 3.10+
- Biblioteca `InquirerPy`
- Biblioteca `rich`

### 🔧 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/JpSeveroo/Rpg-Codex
cd rpg-codex
pip install -r requirements.txt
pip install rich
pip install Inquirerpy
🚀 Execução
bash
Copiar
Editar
python main.py

---Você poderá:

💠 Criar ou carregar fichas salvas
💠 Escolher raça, distribuir atributos e perícias
💠 Iniciar sua jornada pela torre Etherion
💠Enfrentar inimigos, resolver enigmas e evoluir

📁 Estrutura de Pastas
graphql
Copiar
Editar
📦 RPG-CODEX/
  📦 Code/
  ├── combate.py           # Sistema de combate completo
  ├── ficha.py             # Criação e manipulação de personagens
  ├── inimigos.py          # Criação, edição e combate com inimigos
  ├── inventario.py        # Sistema de inventário e equipamentos
  ├── interface.py         # Interface inicial, menus e seleções
  ├── item.py              # Base de dados de todos os itens
  ├── lore.py              # Eventos narrativos e desafios enigmáticos
  ├── utills.py            # Utilitários (print com delay, salvamento JSON, etc.)
  ├── users.py             # Sistema de usuários com login e criptografia
  ├── main.py              # Arquivo principal para rodar o jogo
  ├── jogo1.py, jogo2.py…  # Andares e cenas da jornada
├── lista_itens.json     # Dados de todos os itens disponíveis
├── lista_inimigos.json  # Dados de inimigos criados
├── personagem.json      # Dados salvos do personagem atual
├── usuarios.json        # Dados dos usuários cadastrados
├── README.md            # Este documento
├── requirements.txt     # Dependências do projeto

⚔️ Recursos:
 - Sistema de atributos e perícias (mira, acrobacia, diplomacia…)
 - Itens e poções com efeitos em tempo real
 - Equipamentos (Cabeça, Corpo, Pés, Mãos)
 - Enigmas lógicos adaptativos baseados na percepção do jogador
 - Sistema de morte e retorno com consequências narrativas
 - Interface interativa via terminal com menus do InquirerPy
 - Sistema de usuários com login e senhas criptografadas
 - Salvamento automático via JSON
 - Checkpoints e progressão de andares
 - Itens únicos como a Máscara da Inverdade

🌐 Tecnologias Usadas:
Python 3.10
InquirerPy
Rich
JSON (para salvamento de fichas, inimigos, itens e usuários)

🧠 Lore (Resumo):
Após a Queda do Éter, a matéria colapsou e consciência se fragmentou. Agora, você é um Eco, uma sombra de identidade vagando pelo Labirinto de Etherion, uma torre digital que guarda as últimas memórias da existência. Cada andar é um teste — de lógica, força, alma.

👨‍💻 Contribuição:
Se você quiser sugerir melhorias, corrigir bugs ou criar novos andares e eventos:
- Faça um fork
- Crie uma branch com a sua feature
- Faça um pull request

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

📫 Contato
Projeto criado por João Pedro Bento Severo e colaboradores da UPE.
Para dúvidas, sugestões ou colaborações, entre em contato por [e-mail ou GitHub].


