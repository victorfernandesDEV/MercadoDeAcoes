# calcula o valor das ações
def calcular_acaoes(valores):
	# define uma lista com os valores de cada operação
    acoes = list()
    for indice, valor in enumerate(valores):
        i = len(valores) - 1
        while i >= indice:
        	# se o valor da venda for maior que o valor da compra, armazena o valor em uma lista
        	if valores[i] > valores[indice]:
        		acoes.append(valores[i] - valores[indice])
        	i -= 1
        if len(acoes) > 0:
        	# retorna o maior valor obtido na venda
        	return max(acoes)

    return 0

if __name__ == '__main__':
	while True:
		try:
			valor = calcular_acaoes(list(map(int, input().split(','))))
			print(valor)
		except:
			break