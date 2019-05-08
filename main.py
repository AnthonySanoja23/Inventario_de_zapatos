import os

zapatos = [
			{
				'Modelo':'zapTAN37',
				'Descripción':'Tacón alto negro  ',
				'talla':'  37',
				'precio':'95000.00',
				'cantidad':'  10',
				
				
			},

			{
				'Modelo':'zapTAN38',
				'Descripción':'Tacón alto negro  ',
				'talla':'  38',
				'precio':'95000.00',
				'cantidad':'  10',
				
				
			},

			{
				'Modelo':'zapTAN39',
				'Descripción':'Tacón alto negro  ',
				'talla':'  39',
				'precio':'95000.00',
				'cantidad':'  10',
				
				
			},

			{
				'Modelo':'zapTAM37',
				'Descripción':'Tacón alto marrón ',
				'talla':'  37',
				'precio':'92500.00',
				'cantidad':'  7 ',
				
				
			},

			{
				'Modelo':'zapTAM38',
				'Descripción':'Tacón alto marrón ',
				'talla':'  38',
				'precio':'92500.00',
				'cantidad':'  7 ',
				
				
			},

			{
				'Modelo':'zapTAM39',
				'Descripción':'Tacón alto marrón ',
				'talla':'  39',
				'precio':'92500.00',
				'cantidad':'  7 ',
				
				
			},

			{
				'Modelo':'zapTMN37',
				'Descripción':'Tacón medio negro ',
				'talla':'  37',
				'precio':'85000.00',
				'cantidad':'  12',
							
			},

			{
				'Modelo':'zapTMN38',
				'Descripción':'Tacón medio negro ',
				'talla':'  38',
				'precio':'85000.00',
				'cantidad':'  12',
							
			},

			{
				'Modelo':'zapTMN39',
				'Descripción':'Tacón medio negro ',
				'talla':'  39',
				'precio':'85000.00',
				'cantidad':'  12',
							
			},

			{
				'Modelo':'zapTMM37',
				'Descripción':'Tacón medio marrón',
				'talla':'  37',
				'precio':'83500.00',
				'cantidad':'  8 ',
					
			},

			{
				'Modelo':'zapTMM38',
				'Descripción':'Tacón medio marrón',
				'talla':'  38',
				'precio':'83500.00',
				'cantidad':'  8 ',
				
				
			},

			{
				"Modelo":"zapTMM39",
				"Descripción":"Tacón medio marrón",
				"talla":"  39",
				"precio":"83500.00",
				"cantidad":"  8 ",
			} 
			
]

def Fabricar(zapato_codigo,zapatos_a_fabricar):

	info_dic=next(item for item in zapatos if item['Modelo']==zapato_codigo)
	cantidad = int(info_dic["cantidad"])
	suma = str(cantidad + zapatos_a_fabricar)
	info_dic["cantidad"]="  "+suma+"" 
	print('Agregadas {} unidades del modelo {}'.format(zapatos_a_fabricar,zapato_codigo))
	print('Existencia del modelo {}: {}'.format(zapato_codigo,suma))




def Despachar(zapato_codigo,zapatos_a_despachar):

	info_dic=next(item for item in zapatos if item['Modelo']==zapato_codigo)
	cantidad = int(info_dic["cantidad"])
	
	if cantidad >= zapatos_a_despachar:
		resta = str(cantidad - zapatos_a_despachar)
		info_dic["cantidad"]="  "+resta+" " 
		print('Despachados {} unidades del modelo {}'.format(zapatos_a_despachar,zapato_codigo))
		print('Existencia del modelo {}: {}'.format(zapato_codigo,resta))
	else:
		print('La cantidad disponible de este modelo {} es de : {}'.format(zapato_codigo,cantidad))	
	
			


def listar_zapatos():
	
			print('\n')
			global zapatos
			print(' _'*33)
			print('|MODELO   |   Descripción        |  Talla  |  precio   | cantidad |')
			print(' _'*33)				 
			for idx, zapato in enumerate(zapatos):

					print('|{Modelo} | {Descripción}   | {talla}    | {precio}  | {cantidad}     |'.format(
					Modelo=zapato['Modelo'],
					Descripción=zapato['Descripción'],
					talla=zapato['talla'],
					precio=zapato['precio'],
					cantidad=zapato['cantidad']))
			print(' _'*33)



def Imprimir_informacion(zapato_codigo):

	info_dic=next(item for item in zapatos if item['Modelo']==zapato_codigo)
	print('El modelo selecionado es: Zapato {} '.format(info_dic))





def buscar_zapato(zapato_codigo):

	for zapato in zapatos:

			if zapato['Modelo'] != zapato_codigo:
				continue
			else:
				return True



def _obtener_codigo_zapato(zapato_campo):

		campo = None
	
		while not campo:
				campo = input('Cual es el codigo del zapato:')
	
		return campo




def _menu():

		os.system('clear')
		print('\t'+'*'*21)
		print('\t'+'* Menu de selecion * ')
		print('\t'+'*'*21)

		
		print('1. Entregar ')
		print('2. Fabricar ')
		print('3. Verificar Existencia de un modelo (por codigo)')
		print('4. Ver existencia total ')
		print('5. salir')      
 

if __name__=='__main__':

	while True:

		_menu()
		print('\n')
		comando = input('Digite su opción: ')  
		 
		if comando=='1':
			zapato_codigo = _obtener_codigo_zapato('Modelo')
			zapato_encontrado = buscar_zapato(zapato_codigo)

			if zapato_encontrado:
				Imprimir_informacion(zapato_codigo)
				zapatos_a_despachar=input('Indique la cantidad a despachar :')
				zapatos_a_despachar=int(zapatos_a_despachar)
				Despachar(zapato_codigo,zapatos_a_despachar)
			else:
				 print('El modelo que digito no esta en el inventario')

			input("Presione cualquier tecla para continuar")

		
		elif comando =='2':
			zapato_codigo = _obtener_codigo_zapato('Modelo')
			zapato_encontrado = buscar_zapato(zapato_codigo)

			if zapato_encontrado:
				Imprimir_informacion(zapato_codigo)
				zapatos_a_fabricar=input('Indique la cantidad a fabricar :')
				zapatos_a_fabricar=int(zapatos_a_fabricar)
				Fabricar(zapato_codigo,zapatos_a_fabricar)

			else:
				 print('El modelo que digito no esta en el inventario')

			input("Presione cualquier tecla para continuar")


		elif comando =='3':
			zapato_codigo = _obtener_codigo_zapato('Modelo')
			zapato_encontrado = buscar_zapato(zapato_codigo)

			if zapato_encontrado:
				Imprimir_informacion(zapato_codigo)
				
			else:
				 print('El modelo que digito no esta en el inventario')

			input("Presione cualquier tecla para continuar")

		elif comando =='4':
			listar_zapatos()
			input("Presione cualquier tecla para continuar ")

		elif comando =='5':
			print("Gracias por usar el sistema. Regrese pronto")
			break        
				
		else:
			print('Este comando no existe')
			input("Presione una tecla para continuar")