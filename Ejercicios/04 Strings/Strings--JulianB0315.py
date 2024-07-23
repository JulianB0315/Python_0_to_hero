#1. Crea una tabla de dos variables con todas las operaciones.
a = 32
b = 4
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
#2. Crea cadenas de texto con variables usado Formateo.
nombre = 'Julian'
apellido = 'Burga'
estudio = 'Ingeniería en software '
print('Hola soy %s %s y estudio %s.' %(nombre, apellido,estudio))
print('Hola soy {} {} y estudio {}.'.format(nombre,apellido,estudio))
print(f'Hola soy {nombre} y estudio {apellido} y {estudio} ')
#3. Crea una variable con tu nombre y desempaqueta letra por letra
yo='Julian'
a,b,c,d,e,f=yo
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)