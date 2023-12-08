#Algoritmo de Hoare
#Pivô: sempre elemento do meio do vetor 
#Algoritmo de Lomuto pode ocasionar em uma divisão do array discrepante em vetores decrescentes e crescentes 

def quicksort_original(A):
    comparacoes = [0]  # Inicializa a variável para contar as comparações
    
    def _quicksort(A, inicio, fim):
        if inicio < fim:
            p, comparacoes_partition = partition(A, inicio, fim)
            comparacoes[0] += comparacoes_partition
            
            _quicksort(A, inicio, p - 1)
            _quicksort(A, p + 1, fim)
    
    _quicksort(A, 0, len(A) - 1)
    return A, comparacoes[0]

def partition(A, inicio, fim):
    indice_pivot = (inicio + fim) // 2 
    valor_pivot = A[indice_pivot]
    i = inicio 
    j = fim 
    comparacoes_partition = 0  # Inicializa a variável para contar as comparações
    
    while i < j:
        while A[i] < valor_pivot:
            i += 1
            comparacoes_partition += 1
        while A[j] > valor_pivot:
            j -= 1
            comparacoes_partition += 1
        if i < j:
            A[j], A[i] = A[i], A[j]
    
    return j, comparacoes_partition