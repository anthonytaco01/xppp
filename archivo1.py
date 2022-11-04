#opcion 1 leer el archivo
print('hola bienvenido a mi biblioteca')
print('quieres ver mis libros haz lo siguiente pon (libros.csv)')
nombre=input('ingrese el libro(no olvides lo de arrriba):')
archivo=open (nombre)
lineas=archivo.readlines()
print(lineas)
for linea in lineas:
  print(linea)
archivo.close()