# Fliperama em C++ (MeuApp v4.0)

## O que e
O programa é um sistema de fliperama de terminal que cadastra jogadores, roda o jogo "Adivinhe o Número" e contabiliza o histórico de partidas. Ele nasceu da evolução de um projeto escrito originalmente em C (v3.0), agora reescrito em C++ para aproveitar recursos modernos da linguagem.

## Como compilar e rodar
```bash
g++ -Wall fliperama.cpp -o fliperama
./fliperama
```

## Arquivos
- `fliperama.cpp`: Código-fonte principal que contém o menu, a lógica do jogo, o cadastro de jogadores e a manipulação de arquivos.
- `jogadores.csv`: Banco de dados em texto simples onde a primeira coluna guarda o apelido do jogador (texto) e a segunda guarda a quantidade de partidas jogadas (inteiro), separados por vírgula.

## C x C++: o que mudou

| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
| :--- | :--- | :--- |
| guardar um jogador | `strcpy(apelidos[qtd], novo)` (l. *) | `apelidos.push_back(novo)` (l. 66) |
| comparar apelidos | `strcmp(...) == 0` (l. *) | `==` (l. 39) |
| a funcao que cadastra | `int cadastrar(..., int qtd)` (l. *) | `void cadastrar(... &apelidos, ...)` (l. 62) |

*(Nota: substitua os `*` pelos números das linhas correspondentes do seu arquivo antigo `fliperama.c`).*

## O que o C++ decidiu por mim
Em C, eu precisava definir um tamanho máximo fixo para o vetor de jogadores e controlar manualmente o contador de quantidade (`qtd`) a cada inserção. Em C++, o `std::vector` gerencia o tamanho da lista dinamicamente e libera a memória sozinho ao final do programa.

## Autoavaliacao

| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
| :--- | :--- | :--- |
| 1. Estrutura, compilacao e Git | A | `fliperama.cpp` (l. 1-116, compila sem avisos com `-Wall`) |
| 2. Cadastro: vectors e referencia | A | `fliperama.cpp` (l. 62-68, `cadastrar` usa `&apelidos` e `push_back`) |
| 3. Jogo e partidas | A | `fliperama.cpp` (l. 78-100, `jogar_adivinhe` atualiza `partidas[pos]`) |
| 4. Persistencia | A | `fliperama.cpp` (l. 44-60, funções `salvar` e `carregar` com `jogadores.csv`) |
| 5. Documentacao e comparacao | A | `README.md` (documentação completa e tabela comparativa) |
