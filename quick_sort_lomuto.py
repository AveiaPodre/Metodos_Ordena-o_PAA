#Algoritmo de Lomuto
#Complexidade depende da escolha do pivot.
#O(N²) - Pior Caso. Escolha do pivot que divide o array em dois, um com 0 elementos e outro com n - 1 elementos.
#N*logN - Melhor Caso. Escolha do pivot que divide o array em dois, ambos com N/2 elementos.
#O melhor caso, no quicksort, é o predominante.
#Considerado o algortimo de ordenação mais rápido.
import random 

def quicksort_lomuto(A, inicio=0, fim=None):
    if fim is None:
        fim = len(A) - 1
    comparacoes = 0  
    
    if inicio < fim:
        p, comparacoes_partition = randomized_partition(A, inicio, fim)
        comparacoes += comparacoes_partition
        comparacoes += quicksort_lomuto(A, inicio, p - 1)[1]
        comparacoes += quicksort_lomuto(A, p + 1, fim)[1]
    
    return A, comparacoes  

def randomized_partition(A, p, r):
    aleatorio = random.randrange(p, r)
    A[aleatorio], A[r] = A[r], A[aleatorio]
    return partition(A, p, r)

def partition(A, inicio, fim):
    pivot = A[fim]
    i = inicio
    comparacoes = 0  
    
    for j in range(inicio, fim):
        comparacoes += 1  
        if A[j] <= pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[i], A[fim] = A[fim], A[i]
    return i, comparacoes