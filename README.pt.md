*[Leia em Inglês](./README.md)*
#  Sistema Bancário Avançado em Python

Este projeto foi desenvolvido como parte do Bootcamp de Python na DIO ([Suzano - Python Developer](https://www.dio.me/bootcamp/suzano-python-developer)). É uma evolução do [sistema bancário simples](https://github.com/gtovichins/basic-python-banking-system) e simula um sistema bancário mais avançado, com múltiplos usuários, contas e regras de negócio realistas.

##  Funcionalidades
  -  Cadastro de Usuários

  - Nome Completo: não pode conter números

  - Data de Nascimento: formato DD/MM/AAAA

  - CPF: documento brasileiro, formato XXX.XXX.XXX-XX, único por usuário

  - Endereço: formato Rua, Número - Bairro, Cidade/UF
  -- Exemplo: Rua Principal, 123 - Centro, São Paulo/SP

##  Gerenciamento de Contas

  - Usuários podem ter múltiplas contas

  - Cada conta possui número sequencial e agência fixa

  - Cada conta está vinculada a um único usuário

##  Operações Bancárias

  - Depósito: entrada validada, atualiza saldo e registra transação com data e hora

  - Saque: entrada validada, respeita limite máximo de saque, limite diário de saques e máximo de saques por dia

  - Limite de Transações: cada conta possui limite diário de 10 transações, com aviso das transações restantes

##  Extrato da Conta

  - Mostra cada transação com data e hora

  - Exibe saldo atual, número de saques e transações restantes

##  Exclusão de Usuário

  - Usuários podem ser deletados com confirmação

  - Ao deletar um usuário, todas as contas associadas também são removidas

##  Reset Diário

  - Contagem de saques e transações são reiniciadas automaticamente a cada dia

##  Tecnologias

  - Python 3.x

  - Estruturas condicionais e loops

  - Funções para modularização

  - Biblioteca datetime para registro de data e hora das transações

  - Expressões regulares para validação de entradas

##  Estrutura do Projeto
  - improved-dio-banking-system-project 📁 Pasta raiz
  - improved-dio-banking-system-project.py 📝 Script principal em Python
  - README.md 📄 Documentação em inglês
  - README.pt.md 📄 Documentação em português

##  Observações
Este projeto demonstra:

  - Programação modular com funções dedicadas para cada operação

  - Validação robusta de entradas com mensagens claras para o usuário

  - Suporte para múltiplos usuários e contas

  - Regras bancárias realistas, incluindo limites diários de transações

  - Reset diário automático de limites para simular restrições bancárias reais
