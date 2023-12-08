# Complexidade: O(N²) - Pior Caso

def bubblesort(vetor):
    n = len(vetor)
    comparacoes = 0 
    
    for i in range(n - 1):
        for j in range(n - 1):
            comparacoes += 1 
            if vetor[j] > vetor[j + 1]:
                aux = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = aux
    
    return vetor, comparacoes
