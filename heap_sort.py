#Complexidade: N*logN

def constroiHeapMax(A):
    tamHeap = len(A)
    i = tamHeap // 2 - 1
    comparacoes = 0  
    
    while i >= 0:
        comparacoes += refazHeapMax(A, i, tamHeap)
        i -= 1
    
    return comparacoes  

def refazHeapMax(A, i, tamHeap):
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    maior = i
    comparacoes = 0  
    
    if esquerda < tamHeap and A[esquerda] > A[maior]:
        maior = esquerda
    if direita < tamHeap and A[direita] > A[maior]:
        maior = direita
    
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        comparacoes += 1  # Incrementa a contagem de comparações
        comparacoes += refazHeapMax(A, maior, tamHeap)
    
    return comparacoes 

def heapsort(A):
    tamHeap = len(A)
    comparacoes = constroiHeapMax(A)
    i = tamHeap - 1
    
    while i > 0:
        A[i], A[0] = A[0], A[i]
        tamHeap -= 1
        comparacoes += refazHeapMax(A, 0, tamHeap)
        i -= 1
    
    return A, comparacoes

