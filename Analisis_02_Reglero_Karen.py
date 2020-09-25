# @Autor: Karen Rocío Reglero Crespo
# @Fecha: 25 de septiembre de 2020

#Código para obtener las rutas, transporte y países cque generan mayor valor para Synergy Logystics con base en el valor de las importaciones y la exportaciones.

#importar la librería csv
import csv
#lista que contendrá todos los datos contenidos en el csv
lista_datos = []
#Abrir el archivo csv con with sin tener que usar close despúes
with open("synergy_logistics_database.csv", "r") as archivo_csv:
  #variable que lee al archivo 
  lector = csv.reader(archivo_csv)
  #ciclo para leer lso datos contenidos en el archivo y agregarlos a lista_datos
  for linea in lector:  
    lista_datos.append(linea)
    #print(linea)

#Función para contar las rutas existentes con su valor total que recibe como parámetro dirección que será el valor de Exports e Imports
def rutas(direccion):

  #GENERAR RUTAS DE EXPORTACION
  #direccion = "Exports"
  #Contador para contar el numero de veces de cada ruta
  contador = 0
  #Lista que contendrá el valor de ruta actual para poder contar
  rutas_contadas = []
  #Lista que contendrá el resultado de contar cada una de las rutas y su valor total.
  conteo_rutas = []

 #Ciclo para contar dentro de lista_datos que contiene los datos del archivo csv
  for ruta in lista_datos:
    #Si el valor de ruta en la posición 1 es igual a Exports o Imports dependiendo de la llamada a la función:
      if ruta[1] == direccion:
        #la ruta actual será la ruta en la posicón de origen y destino respectivamente.
        ruta_actual = [ruta[2], ruta[3]]
        #Si la ruta actual no ha sido contabillizada:
        if ruta_actual not in rutas_contadas:
          #Se realiza otro ciclo para contar el numero de veces que se encuentra
          for movimiento in lista_datos:
            if ruta_actual == [movimiento[2], movimiento[3]]:
              #al contador se le sumará el valor de total_value en la posición 9
              contador += int(movimiento[9])
          #Se agrega a rutas_contadas la ruta actual
          rutas_contadas.append(ruta_actual)
          #Se agrega cada una de las rutas junto con su valor total
          conteo_rutas.append([ruta[2], ruta[3], contador])
          contador = 0 #reiniciar el contador
   #Se ordena la lista conforme el valor total de forma desdecendente
  conteo_rutas.sort(reverse = True, key = lambda x:x[2])
  #Se muestra en pantalla
  print("Las rutas con su valor total es: ", conteo_rutas)

#rutas("Exports")
#rutas("Imports")

#Esta función cuenta el número de veces que se encuentra el transporte para saber cual ha sido el mas usado y menos usado.
def transporte(direccion):
  #Conforme la información en el csv, se puso en forma de tabla los datos y se filtraron los valores en la columna transport_mode para construir la siguiente lista:
  transportes = ["Air", "Rail", "Road", "Sea"]
  #Contador para contar el número de veces que aparece cada transporte
  contador = 0
  #lista que contendrá el conteo de cada ruta
  totales = []
  #Ciclo para contar cuantas veces el transporte de la lista transportes aparece en lista_datos 
  for transporte in transportes:
    #archivo_csv.seek(0)
    for linea in lista_datos:
      #Si el transporte esta en la lista transportes y la dirección es Exports o Imports(dependiendo de la llamada de la función), entonces se agrega mas uno al valor de contador:
      if linea[7] == transporte and linea[1] == direccion:
        contador += 1
        #Se agregan los totales de cada conteo:
    totales.append([transporte, contador])
    contador = 0 #Se reinicia el contador
 #Se ordena la lista en forma desc
  totales.sort(reverse = True, key = lambda x:x[1])
  #Se imprime el resultado
  print("Los transportes son: ", totales)

#Función para conocer los países que más exportan e importan conforme el valor total, recibe como parámetro la dirección (Exports)
def paisesExportados(direccion):

  #Nota: El código es parecido a la función de rutas por lo que sólo algunas cosas serán comentadas:

  #GENERAR RUTAS DE EXPORTACION
  #direccion = "Exports"
  contador = 0
  paises_contados = []
  conteo_paises = []

  for pais in lista_datos:
      if pais[1] == direccion:
        #Si país en la posición actual es el que se encuentra en la posición de Origen 
        pais_actual = [pais[2]]

        if pais_actual not in paises_contados:
          for movimiento in lista_datos:
            if pais_actual == [movimiento[2]]:
              contador += int(movimiento[9])

          paises_contados.append(pais_actual)

          conteo_paises.append([pais[2], contador])
          contador = 0 #reiniciar el contador

  conteo_paises.sort(reverse = True, key = lambda x:x[1])
  print("Los países que exportan con su valor total es: ", conteo_paises)

#Función para conocer los países que más exportan e importan conforme el valor total, recibe como parámetro la dirección (Imports)
def paisesImportados(direccion):

  #Nota: El código es parecido a la función de paises exportados por lo que sólo algunas cosas serán comentadas:

  #GENERAR RUTAS DE EXPORTACION
  #direccion = "Exports"
  contador = 0
  paises_contados = []
  conteo_paises = []

  for pais in lista_datos:
      if pais[1] == direccion:
        #Si país en la posición actual es el que se encuentra en la posición de Destino:
        pais_actual = [pais[3]]

        if pais_actual not in paises_contados:
          for movimiento in lista_datos:
            if pais_actual == [movimiento[3]]:
              contador += int(movimiento[9])

          paises_contados.append(pais_actual)

          conteo_paises.append([pais[3], contador])
          contador = 0 #reiniciar el contador

  conteo_paises.sort(reverse = True, key = lambda x:x[1])
  print("Los países que importan con su valor total es: ", conteo_paises)

#Menú para el usuario
menu = """ -----------Bienvenido a Synergy Logistics----------

Selecciona la opción que deseas ver:

  1. Rutas de exportación
  2. Rutas de importación
  3. Transporte de exportación
  4. Transporte de importación
  5. Paises que exportan 
  6. Paises que importan
  """
print(menu)
elección = int(input("Elige una opción:   "))
#Rutas de exportación con su valor total
if elección == 1:
    rutas("Exports")
#Rutas de importación con su valor total
elif elección == 2:
    rutas("Imports")
#Tranporte usado en exportación
elif elección == 3:
  transporte("Exports")
#Tranporte usado en importación
elif elección == 4:
  transporte("Imports")
#Países que exportan (Valor tomado de origen)
elif elección == 5:
  paisesExportados("Exports")
#Países que importan (Valor tomado de destino)
elif elección == 6:
  paisesImportados("Imports")

#Código de prueba xD 
'''
for ruta in lista_datos:
  if ruta[1] == direccion:
    ruta_actual = [ruta[2], ruta[3]]

    if ruta_actual not in rutas_contadas:
      for movimiento in lista_datos:
        if ruta_actual == [movimiento[2], movimiento[3]]:
          contador += 1

      rutas_contadas.append(ruta_actual)

      conteo_rutas.append([ruta[2], ruta[3], contador])
      contador = 0 #reiniciar el contador

conteo_rutas.sort(reverse = True, key = lambda x:x[2])
print(conteo_rutas)

for ruta in lista_datos:
    if ruta[1] == direccion:
      ruta_actual = [ruta[2], ruta[3]]

      if ruta_actual not in rutas_contadas:
        for movimiento in lista_datos:
          if ruta_actual == [movimiento[2], movimiento[3]]:
            contador += int(movimiento[9])

        rutas_contadas.append(ruta_actual)

        conteo_rutas.append([ruta[2], ruta[3], contador])
        contador = 0 #reiniciar el contador

  conteo_rutas.sort(reverse = True, key = lambda x:x[2])
  print(conteo_rutas)

  '''