/*
*Disciplina: 2026-PCAP
*Projeto   :


*/

#include <stdio.h>

#define DONO "Gustavo Ribeiro"

void linha() {
    printf("======================================\n");
}

void titulo(char texto[]){
    linha();
    printf("    %s\n", texto);
    linha();
}


int ler_numero(char mensagem[], int minimo, int maximo) {
    int numero, lidos;

    printf("    %s: ", mensagem);
    lidos = scanf("%d", &numero);
    while (lidos != 1 || numero < minimo || numero > maximo){
        if (lidos != 1){
        scanf("%*s");
        }
     printf("opacao invalida! tente novamente: ");
     lidos = scanf("%d", &numero);
    }
    return numero;
}


void mostrar_menu() {
    linha();
    printf("    FLIPERAMA DO %s\n", DONO);
    linha();
    printf("[1] Adivinhe o Numero\n");
    printf("[2] Cadastrar Jogador\n");
    printf("[3] Listar jogadores\n");
    printf("[0] Sair\n");
    linha();
}


int main() {
    int opcao;

    mostrar_menu();
    opcao = ler_numero ("sua escolha", 0, 3);


    while (opcao != 0){
        if(opcao == 1 ) {
            printf("O jogo entrar na Fae #.\n");
        }else if (opcao == 2 ) {
            printf("O cadastro entra na fase 2.\n");
        }else {
            printf("A lista entra na Fase 2.\n");
                }

        mostrar_menu();
        opcao = ler_numero("sua escolha", 0, 3);
            }

    titulo("ate a proxima!");
     return 0;
}