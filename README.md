# PlanusFit

## - Projeto Integrador - Senac
Este é um projeto integrador desenvolvido por estudantes do curso de **Análise e Desenvolvimento de Sistemas** do **Senac**. O objetivo principal é criar um software funcional que auxilie os usuários no controle e acompanhamento de treinos, informações físicas e suplementação alimentar.

## 💡 Objetivo
O **PlanusFit** é um sistema desktop que fornece uma experiência personalizada para usuários que desejam:
- Registrar seus dados físicos e corporais
- Consultar vídeos de treinos e canais recomendados
- Acessar informações sobre suplementos
- Escolher treinos para definição e hipertrofia
- Acompanhar suas métricas

## - Tecnologias utilizadas
- **Python 3**
- **PyQt5** (para interfaces gráficas)
- **MySQL** (como banco de dados relacional)
- **Qt Designer** (para construção das telas `.ui`)
- **Webbrowser** (para abrir links externos de vídeos e conteúdos)

## - Funcionalidades principais

### Cadastro e Login
- O usuário pode se cadastrar informando nome, sobrenome, email, senha, peso, altura e percentual de gordura.
- Após o login, o sistema direciona para a tela principal com as opções de navegação.

### Telas disponíveis
- **Página Inicial (topicos.ui)**: Menu principal do sistema
- **Perfil**: Exibição de informações do usuário
- **Treino em casa**: Sugestões de treinos e vídeos do YouTube
- **Treinos focados**: Divididos em definição e hipertrofia, com foco em grupos musculares específicos
- **Suplementos**: Informações sobre os principais suplementos utilizados em academias
- **Informações adicionais**: Benefícios dos treinos e suplementos

### Banco de Dados
O sistema se conecta ao banco **MySQL** para persistência dos dados de cadastro.
