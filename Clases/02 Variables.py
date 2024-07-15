#Ahora aprendamos las variables
#Para tener una buena base y practica a la hora de escribir variables tenemos que tener en cuenta los siente ejemplos:
#Forma correcta:

first_mane='Pablo'
last_name='Acuña'
mun1=10

#Forma incorrecta(si quieres comprobar quita el comentario):
#last@name='Acuña'
#first-name='Pedro'
#1mun=8

#Podemos tener diferentes tipos de variables como:
tipo_string='Hola tengo'# 'str'
#Imprimimos  la varible con un print el nombre nombre de la variable sin las comillas
print(tipo_string) 

tipo_int=20 # 'int'
#Con los números igual 
print(tipo_int) 

tipo_bool=False
print(tipo_bool)
 
#Podemos llamar diferentes variables y escirbir lineas de texto, sin importar el tipo siempre y cuando estén separadas con comas
print(tipo_string,tipo_int,'este dato es',tipo_bool)

#Ahora probemos con cambiar los tipos de variables a str
edad=18
print(edad)
print(type(edad))

#Cambiemos este variable de int a str
string_edad=str(edad)
print(string_edad)
print(type(string_edad))

#Un boolean
python=True
print(type(python))

str_python=str(python)
print(str_python)
print(type(str_python))
#Cambiar un datos de str 