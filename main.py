import os
import csv
import time
from bubble_sort import *
from insertion_sort import *
from merge_sort import *
from heap_sort import *
from quick_sort_original import *
from quicksort_insertion import *

#criação de um dicionário que guarda o nome dos arquivos de entrada dos vetores
vetores = {
    'aleatorio': {
        100: 'vetor_aleatorio_100.txt',
        1000: 'vetor_aleatorio_1000.txt',
        5000: 'vetor_aleatorio_5000.txt',
        30000: 'vetor_aleatorio_30000.txt',
        50000: 'vetor_aleatorio_50000.txt',
        100000: 'vetor_aleatorio_100000.txt',
        150000: 'vetor_aleatorio_150000.txt',
        200000: 'vetor_aleatorio_200000.txt'
    },
    'crescente': {
        100: 'vetor_crescente_100.txt',
        1000: 'vetor_crescente_1000.txt',
        5000: 'vetor_crescente_5000.txt',
        30000: 'vetor_crescente_30000.txt',
        50000: 'vetor_crescente_50000.txt',
        100000: 'vetor_crescente_100000.txt',
        150000: 'vetor_crescente_150000.txt',
        200000: 'vetor_crescente_200000.txt'
    },
    'decrescente': {
        100: 'vetor_decrescente_100.txt',
        1000: 'vetor_decrescente_1000.txt',
        5000: 'vetor_decrescente_5000.txt',
        30000: 'vetor_decrescente_30000.txt',
        50000: 'vetor_decrescente_50000.txt',
        100000: 'vetor_decrescente_100000.txt',
        150000: 'vetor_decrescente_150000.txt',
        200000: 'vetor_decrescente_200000.txt'
    }
}
#definição dos arquivos de entrada baseado no input do usuário
os.system('cls')
print("Qual o tamanho do arquivo desejado a ser ordenado:")
print("1- 100 elementos")
print("2- 1k elementos")
print("3- 5k elementos")
print("4- 30k elementos")
print("5- 50k elementos")
print("6- 100k elementos")
print("7- 150k elementos")
print("8- 200k elementos")
print("0- Sair do programa")

while(True):
    resp = int(input())
    match resp:
        case 1:
            tamanho_arquivo = 100
            os.system('cls')
            break
        
        case 2:
            tamanho_arquivo = 1000
            os.system('cls')
            break

        case 3:
            tamanho_arquivo = 5000
            os.system('cls')
            break

        case 4:
            tamanho_arquivo = 30000
            os.system('cls')
            break

        case 5:
            tamanho_arquivo = 50000
            os.system('cls')
            break

        case 6:
            tamanho_arquivo = 100000
            os.system('cls')
            break

        case 7:
            tamanho_arquivo = 150000
            os.system('cls')
            break

        case 8:
            tamanho_arquivo = 200000
            os.system('cls')
            break

        case 0:
            quit()

        case default:
            print("Valor inválido, insira o valor novamente")

os.system('cls')
print("Qual a distribuição do arquivo desejado:")
print("1- Aleatório")
print("2- Crescente")
print("3- Decrescente")
print("0- Sair do programa")

while(True):
    resp = int(input())
    match resp:
        case 1:
            distribuicao_arquivo = 'aleatorio'
            os.system('cls')
            break
        
        case 2:
            distribuicao_arquivo = 'crescente'
            os.system('cls')
            break

        case 3:
            distribuicao_arquivo = 'decrescente'
            os.system('cls')
            break

        case 0:
            quit()

        case default:
            print("Valor inválido, insira o valor novamente")

#leitura do arquivo contendo os valores a serem ordenados
caminho_txt = vetores[distribuicao_arquivo][tamanho_arquivo]
print(caminho_txt)
with open(caminho_txt, 'r') as arquivo:
    dados = arquivo.read().split()
    dados = [int(numero) for numero in dados]

#execução do algoritmo desejado junto da contagem do tempo de execução
print("Qual algoritmo deseja ser utilizado:")
print("1- Bubble Sort")
print("2- Insertion Sort")
print("3- Merge Sort")
print("4- Heap Sort")
print("5- Quick Sort(original)")
print("6- Quick Sort com Inserção")
print("0- Sair do programa")

while(True):
    resp = int(input())
    match resp:
        case 1:
            caminho_csv = 'tempo_execucao_bubble.csv'
            inicio = time.perf_counter()
            _, comparacoes = bubblesort(dados)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            break
        
        case 2:
            caminho_csv = 'tempo_execucao_insertion.csv'
            inicio = time.perf_counter()
            _, comparacoes = insertion(dados)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            break

        case 3:
            caminho_csv = 'tempo_execucao_merge.csv'
            inicio = time.perf_counter()
            _, comparacoes = mergesort(dados)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            break

        case 4:
            caminho_csv = 'tempo_execucao_heap.csv'
            inicio = time.perf_counter()
            _, comparacoes = heapsort(dados)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            break
        
        case 5:
            caminho_csv = 'tempo_execucao_quick_original.csv'
            inicio = time.perf_counter()
            _, comparacoes = quicksort_original(dados)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            break

        case 6:
            caminho_csv = 'tempo_execucao_quick_insertion.csv'
            inicio = time.perf_counter()
            _, comparacoes = quicksort_insertion(dados)
            fim = time.perf_counter()
            tempo_execucao = fim - inicio
            tempo_execucao = f'{tempo_execucao:.10f}'
            break

        case 0:
            quit()

        case default:
            print("Valor inválido")

#amostragem do tempo de execução e do número de comparações
print(tempo_execucao)
print(comparacoes)

#salvamento do tempo de execução em arquivo csv
linha = [tamanho_arquivo, distribuicao_arquivo, tempo_execucao, comparacoes]
with open(caminho_csv, 'a', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(linha)