import itertools


def consistencia(entrenamiento,hipotesis):
	#hipotesis = ['rojo','?','?']
	#Cambiar hipotesis
	#ejemplo = [('azul','cuadrado','grande'),(False)]
	clasificado = True
	i = 0
	for campo in entrenamiento[0]:
		if(hipotesis[0][i] != campo and hipotesis[0][i] != '?' ):
			clasificado = False
			#print(hipotesis[i] , campo)
			i= i+1
	if(clasificado == entrenamiento[1]):
		return True#consistencia
	else:
		return False#consistencia
def comparacion_especifica_pos(entrenamiento,S):
	
	for i in range(0,len(S)):
		if(entrenamiento[i] == S[i] or S[i] == "?"):
			None
		elif(entrenamiento[i] != S[i]):
			aux = list(S)
			aux[i] = "?"
			S = tuple(aux)
	return S
def clasificacion_general_neg(entrenamiento,G,S):
	#print(entrenamiento,G)
	aux = 0
	g_completo = []
	j = 0
	for n in range(0,len(G)):
		for i in range(0,len(G[n])):
			if(entrenamiento[i] == G[n][i] or G[n][i] == "?"):
				aux = aux+1
				if(G[n][i] == entrenamiento[i]):
						break
				else:
					if(S[i] != entrenamiento[i] and S[i] != "?"):
						g_aux = list(G[n])
						g_aux[i] = S[i]
						g_alt = tuple(g_aux)
						g_completo.append(g_alt)
			else:
				g_aux = list(G[n])
				g_aux[i] = S[i]
				g_alt = tuple(g_aux)
				g_completo.append(g_alt)
	return(g_completo)

# General(Hipotesis)

G = [('?', '?', '?' )]

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

D1 = [('Rojo','Cuadrado','Grande' ),(True)]
D2 = [('Azul', 'Cuadrado', 'Grande' ), (True)]
D3 = [ ('Rojo','Redondo', 'Pequeno' ), (False)]
D4 = [('Verde', 'Cuadrado','Pequeno' ), (False)]
D = [D1 , D2 , D3 , D4]

primero = 0
for entrenamiento in D:
	if(entrenamiento[1] == True):
		devuelto = consistencia(entrenamiento,G)
		#print("devuelve",devuelto)
		if(devuelto == entrenamiento[1]):
			print("consistente verdadero , mantengo D")
		if(primero == 0):
			primero = 1
			S = entrenamiento[0]
		elif(primero != 0):
			S = comparacion_especifica_pos(entrenamiento[0],S)
			
		
	elif(entrenamiento[1] == False):
		devuelto = consistencia(entrenamiento,S)
		if(devuelto == entrenamiento[1]):
			print("consistente Falso , mantengo D")
		G = clasificacion_general_neg(entrenamiento[0],G,S)
print("Especifica",S)
print("General",G)

#Falsos
#print(h)
print(len(h))
positivo_list = []
negativo_list = []
for comparacion in h:
	positivo = 0 #hago 0 por cada elemento de la lista h
	for i in range(0,len(comparacion)):
		if(S[i] == comparacion[i] or S[i] == "?"):
			positivo = positivo + 1
		if(G[0][i] == comparacion[i] or G[0][i] == "?"):
			positivo = positivo + 1
	if(positivo == 2*len(S)):
		#print("POSITIVO",comparacion)
		positivo_list.append(comparacion)
	else:
		#print("Negativo",comparacion)
		negativo_list.append(comparacion)
print("VERDADERO")
print(positivo_list)
print("\n\n FALSOS" )
print(negativo_list)