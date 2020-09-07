import itertools
# General(Hipotesis)

G = ['?', '?', '?' ]

#Especifico(hipotesis)

S = [None, None, None]

# atributos
AV = [('Rojo','Azul','Verde','?'),('Cuadrado','Redondo','?'),('Grande','Pequeno','?')]

# Ejemplo:
#print(type(AV))
lista=[]
combinaciones = ("\n".join(" ".join(item) for item in itertools.product(*AV)))


lista = combinaciones.split('\n')

h=[]
for salida in lista:
	list_aux = salida.split(" ")
	h.append(list_aux)

D1 = [('Rojo','Cuadrado','Grande' ),('Verdadero')]
D2 = [('Azul', 'Cuadrado', 'Grande' ), ('Verdadero')]
D3 = [ ('Rojo','Redondo', 'Pequeno' ), ('Falso')]
D4 = [('Verde', 'Cuadrado','Pequeno' ), ('Falso')]
D = [D1 , D2 , D3 , D4]
def consistencia(entrenamiento):
	hipotesis = ['rojo','?','?']
	#Cambiar hipotesis
	#ejemplo = [('azul','cuadrado','grande'),(False)]
	clasificado = True
	for campo in entrenamiento[0]:
		if(hipotesis[i] != campo and hipotesis[i] != '?' ):
			clasificado = False
	if(clasificado == ejemplo[1]):
		return True#consistencia
	else:
		return False#consistencia

	"""
	for i in range(0,len(hipotesis)):
		if(hipotesis[i] != ejemplo[0][i] and hipotesis[i] != '?' ):
			clasificado = False
	if(clasificado == ejemplo[1]):
		return True#consistencia
	else:
		return False#consistencia
	"""
	
	
print(consistencia())
	



consistente_general = 0
especifico_positivo = 0
clasifica_negativo = 0
generales = []
aux = []
for entrenamiento in D:
	if(entrenamiento[1] == 'Verdadero'):
		for i in range(0,(len(G))):			
			if(entrenamiento[0][i] == G[i] or G[i] == '?'):
				consistente_general +=1
			if(S[i] == None):#siempre inconsistente
				S[i] = entrenamiento[0][i]
			elif(S[i] == entrenamiento[0][i] or S[i] == '?'):
				especifico_positivo +=1
			elif(S[i] != entrenamiento[0][i]):
				S[i] = '?'
	elif(entrenamiento[1] == 'Falso'): #problemas NO FUNCIONA
		for i in range(0,len(S)):
			if(S[i] != entrenamiento[0][i]):
				clasifica_negativo +=1
			if(consistencia(entrenamiento)):
				
			else():
				
			#if(G[i] == entrenamiento[0][i] or G[i] == '?'):
			#	if(entrenamiento[0][i] == S[i]):
			#		print("algo")
				#elif(entrenamiento[0][i] != S[i]):
			#general final = < '?' , '?' , grande>		

print("Especifica",S)
print("General",G)
"""parametros_comparados_G = 0
terminado_G = []
finalizada_S = []
finalizada_S = h
print("\n\n\nVERDADEROS \n\n\n")
for final in h:
	#print(len(final))
	for i in range(0,len(G)):
		if(G[i] != '?'):
			if(final[i] == G[i]):
				parametros_comparados_G = parametros_comparados_G+1	
	if(parametros_comparados_G == parametros_definidos_G):
		final.append("Verdadero")
		terminado_G.append(final)
		#print(final)
	parametros_comparados_G = 0

#print(terminado_G)

print("\n\n\nFALSOS \n\n\n")
terminado_S = []
parametros_comparados_S = 0
for final in finalizada_S:
	for i in range(0,len(S)):
		if(final[i] == S[i]):
			parametros_comparados_S = parametros_comparados_S+1
	if(parametros_comparados_S > 1 and len(final)<7):
		final.append("Falso")
		terminado_S.append(final)
		#print(final)
	parametros_comparados_S = 0
#print(terminado_S)
"""
