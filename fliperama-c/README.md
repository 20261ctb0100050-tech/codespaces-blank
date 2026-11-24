# Fliperama em C (MeuApp v3.0)
**Disciplina:** 2026-PCAP  
**Dev:** Gustavo Ribeiro

Este projeto é a evolução do meu jogo em Python para a linguagem C. Ele junta um sistema simples de cadastro de jogadores (salvando tudo em um arquivo externo) com um joguinho de adivinhar o número secreto.

---

## 🚀 Como testar o projeto

Para compilar e rodar direto no terminal, é só usar os comandos abaixo:

```bash
gcc -Wall fliperama.c -o fliperama
./fliperama
```

## 📂 O que tem no repositório

**fliperama.c**: Todo o código do programa (menus, validações de entrada, lógica do jogo e leitura/escrita do arquivo).
**jogadores.csv**: Onde os dados ficam guardados no formato `nome,partidas`. Se o arquivo não existir, o programa cria sozinho ao sair.

---

## 🔄 O que mudou de Python para C?

Passar o código para C me fez perceber como a linguagem exige muito mais atenção com a memória e o tipo de dado. Olha a diferença prática na hora de resolver os mesmos problemas:

| O que eu precisava fazer | Como era no Python | Como ficou no C | Linha no código |
| :--- | :--- | :--- | :---: |
| **Salvar um novo jogador** | `jogadores.append(novo)` | `strcpy(apelidos[qtd], novo);` | l. 81 |
| **Comparar os apelidos** | `if nome == procurar:` | `if (strcmp(apelidos[i], procurando) == 0)` | l. 56 |
| **Verificar se o arquivo existe** | `exists(ARQUIVO)` | `if (arquivo == NULL)` | l. 138 |

### Perrengues e decisões que precisei tomar em C:
|1. **Memória limitada:** No Python as coisas crescem sozinhas. No C, tive que definir um limite fixo de 50 jogadores (`CAPACIDADE`) e no máximo 19 letras para o nome (`TAM_APELIDO`), usando travas como `%19s` para o programa não quebrar.
|2. **Buffer do scanf:** Se o usuário digitasse uma letra onde o programa esperava um número, o menu entrava em loop infinito. Resolvi isso limpando o buffer com `scanf("%*s")` na linha 30 sempre que a entrada dá erro.

---

## 📈 Minha Autoavaliação

Fiz o código de forma organizada e modularizada. Abaixo mostro onde estão os critérios pedidos na disciplina:

**1. Estrutura, compilação e Git (Conceito: Excelente)**
*Onde prova:* O arquivo `fliperama.c` está limpo, bem identado e roda sem warnings do GCC (l. 1-182).
**2. Cadastro, menu e vetores (Conceito: Excelente)**
*Onde prova:* Funções de busca e inserção organizadas usando matriz de char e vetores paralelos (l. 52-61, l. 63-84, l. 86-96).
**3. Jogo e controle de partidas (Conceito: Excelente)**
*Onde prova:* Lógica do jogo de adivinhação atualizando o número de partidas do jogador correto (l. 98-128).
**4. Persistência de dados (Conceito: Excelente)**
*Onde prova:* Funções `salvar` e `carregar` manipulando o arquivo CSV com ponteiros `FILE*` (l. 130-149).
**5. Documentação (Conceito: Excelente)**
*Onde prova:* Este próprio arquivo `README.md` explicando o projeto de forma clara.
