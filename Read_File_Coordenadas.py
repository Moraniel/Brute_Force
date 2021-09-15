def readFileCoord(filename):
    arq = open(filename, 'r')  # abre o arquivo
    texto = []  
    matriz = []  
  
    texto = arq.readlines()  # Quebra as linhas do arquivo em vetores
  
    for i in range(len(texto)):  # Esse for percorre a posições dp vetor texto
      
        matriz.append(texto[i].split())
    for j in range(len(matriz)):      # Aqui a lista de coordenadas são transformadas em float
      for k in range(len(matriz[j])):
        matriz[j][k]=(float(matriz[j][k]))



    arq.close()  # Comando para fechar o arquivo

    return matriz
