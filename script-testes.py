import random
import numpy as np

#arquivo dedicado à geração dos vetores, salvando-os em 3 diferentes arquivos txt 
#define uma semente fixa
seed = 42
random.seed(seed)

#vetor decrescente de 500 elementos (ajustar a quantidade de acordo com a necessidade)
vetor_decrescente = sorted(random.sample(range(1, 300000), 200000), reverse=True)

#vetor aleatório de 500 elementos (ajustar a quantidade de acordo com a necessidade)
vetor_aleatorio = random.sample(range(1, 300000), 200000)

#vetor crescente de 500 elementos (ajustar a quantidade de acordo com a necessidade)
vetor_crescente = sorted(random.sample(range(1, 300000), 200000), reverse=False)

#caminho para salvar os arquivos de texto
caminho_arquivo_decrescente = 'vetor_decrescente_200000.txt'
caminho_arquivo_aleatorio = 'vetor_aleatorio_200000.txt'
caminho_arquivo_crescente = 'vetor_crescente_200000.txt'

#salva os vetores em arquivos de texto
np.savetxt(caminho_arquivo_decrescente, vetor_decrescente, fmt='%d')
np.savetxt(caminho_arquivo_aleatorio, vetor_aleatorio, fmt='%d')
np.savetxt(caminho_arquivo_crescente, vetor_crescente, fmt='%d')