""""1. Crea 4 tuples sobre web, program, database y framework."""

web = ('HTML', 'CSS', 'JavaScript', 'HTTP')
program = ('Python', 'Java', 'C++', 'JavaScript')
database = ('MySQL', 'PostgreSQL', 'SQLite', 'MongoDB')
framework = ('Django', 'Flask', 'Spring', 'React')

""""Con el tuples web accede a sus artículos con indexación positiva y negativa."""
elemento_1_positivo = web[0] 
elemento_2_positivo = web[1]  

elemento_1_negativo = web[-1]  
elemento_2_negativo = web[-2]  

print("Elementos de la tupla web (positiva):", elemento_1_positivo, elemento_2_positivo)
print("Elementos de la tupla web (negativa):", elemento_1_negativo, elemento_2_negativo)

""""Con el program convertirlo de una lista y elimina."""
program_lista = list(program)
program=tuple(program_lista)
del program

""""Y con las listas database únela con framework."""
database_framework= database + framework

print(database_framework)