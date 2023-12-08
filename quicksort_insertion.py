def insertion_sort(arr, inicio, fim):
    for i in range(inicio + 1, fim + 1):
        chave = arr[i]
        j = i - 1
        while j >= inicio and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def partition(arr, inicio, fim):
    pivot = arr[(inicio + fim) // 2]
    i = inicio - 1
    j = fim + 1
    comparacoes = 0

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
            comparacoes += 1
        
        j -= 1
        while arr[j] > pivot:
            j -= 1
            comparacoes += 1
        
        if i >= j:
            return j, comparacoes
        
        arr[i], arr[j] = arr[j], arr[i]

def quicksort_insertion(arr, inicio=0, fim=None, threshold=50):
    if fim is None:
        fim = len(arr) - 1
    comparacoes = 0

    while inicio < fim:
        if fim - inicio < threshold:
            insertion_sort(arr, inicio, fim)
            return arr, comparacoes + (fim - inicio + 1) * (fim - inicio) // 2
        
        pivot_index, comparacoes_particao = partition(arr, inicio, fim)
        comparacoes += comparacoes_particao
        
        comparacoes += 1  # Incremento para a comparação do pivot
        
        if pivot_index - inicio < fim - pivot_index:
            comparacoes += quicksort_insertion(arr, inicio, pivot_index, threshold)[1]
            inicio = pivot_index + 1
        else:
            comparacoes += quicksort_insertion(arr, pivot_index + 1, fim, threshold)[1]
            fim = pivot_index
    
    return arr, comparacoes

