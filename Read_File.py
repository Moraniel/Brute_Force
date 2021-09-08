def readFile(filename):
    arq = open(filename, 'r')  # Abre o arquivo
    texto = []  
    matriz = []  
    texto = arq.readlines()  # Quebra as linhas do arquivo em vetores
  

    for i in range(len(texto)):  # Percorre a posições do vetor texto
        
        matriz.append(texto[i].split())

    arq.close()  # Comando para fechar o arquivo

    return matriz
