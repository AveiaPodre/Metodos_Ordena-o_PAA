# Complexidade: O(N*logN) - Pior Caso

def mergesort(A, inicio=0, fim=None):
    if fim is None:
        fim = len(A)
    comparacoes = 0  
    
    if (fim - inicio > 1):
        meio = (inicio + fim) // 2
        comparacoes += mergesort(A, inicio, meio)[1] 
        comparacoes += mergesort(A, meio, fim)[1] 
        comparacoes += merge(A, inicio, meio, fim)  
    
    return A, comparacoes  

def merge(A, inicio, meio, fim):
    left = A[inicio:meio]
    right = A[meio:fim]
    i, j, comparacoes = 0, 0, 0  
    
    for k in range(inicio, fim):
        if i >= len(left):
            A[k] = right[j]
            j += 1
        elif j >= len(right):
            A[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            A[k] = left[i]
            i += 1
            comparacoes += 1  
        else:
            A[k] = right[j]
            j += 1
            comparacoes += 1  
    
    return comparacoes
