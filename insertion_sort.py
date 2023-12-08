# Complexidade: O(N²) - Pior Caso
# Número de operações: N*(N-1)/2

def insertion(vetor):
    n = len(vetor)
    comparacoes = 0  
    
    for i in range(1, n):
        j = i
        while j > 0:
            comparacoes += 1
            if vetor[j] < vetor[j - 1]:
                aux = vetor[j]
                vetor[j] = vetor[j - 1]
                vetor[j - 1] = aux
            j -= 1
    
    return vetor, comparacoes
