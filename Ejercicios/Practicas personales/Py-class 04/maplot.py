import matplotlib.pyplot  as plt

a=[1,2,3,4,5]
b=[44,55,66,77,88]

plt.plot(a,b,label='Linea 1', color='red', linewidth=2)
plt.title('Grafico de linea')
plt.xlabel('Eje X')
plt.show()

x1=[3,4,5,6]
y1=[5,6,3,4]

x2=[2,5,8]
y2=[3,4,3]

plt.plot(x1,y1,label='Linea 1', color='red', linewidth=2)
plt.plot(x2,y2,label='Linea 2', color='blue', linewidth=2)
plt.title('Grafico de linea')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid()
plt.show()

x1=[0.25,1.25,3.25,2.25,4.25]
y1=[10,55,32,80,20]

x2=[0.75,1.75,2.75,3.75,4.75]
y2=[42,26,78,15,10]

plt.bar(x1,y1,label='Datos 1', width=0.5, color='blue')
plt.bar(x2,y2,label='Datos 2', width=0.5, color='orange')
plt.title('Grafico de barras')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.show()

a = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]
plt.hist(a,bins,histtype='bar',rwidth=0.8, color='red')
plt.title('Histograma')
plt.xlabel('Eje X')
plt.show()

x1=[0.25,1.25,2.25,3.25,4.25]
y1=[10,55,32,80,20]

x2=[0.75,1.75,2.75,3.75,4.75]
y2=[42,26,78,15,10]

plt.scatter(x1,y1,label='Datos 1', color='red')
plt.scatter(x2,y2,label='Datos 2', color='blue')
plt.title('Grafico de dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.show()

Ciclismo =[7,8,6,11,7]
Maraton =[2,3,4,3,2]
Futbol =[8,5,7,8,13]
Natacion =[6,7,8,9,10]
Divisiones = [1,2,3,4,5]

deportes=["Ciclismo","Maraton","Futbol","Natacion", "Otro"]
colores = ['red','blue','green','yellow','orange']

plt.pie(Divisiones,labels=deportes,colors=colores,startangle=90,shadow=True,explode=(0.1,0,0,0,0),autopct='%1.1f%%')
plt.axis('equal')
plt.title('Deportes favoritos')
plt.show()

x1=[0.25,1.25,2.25,3.25,4.25]
y1=[10,55,32,80,20]
y3=[10,55,32,80,20]

x2=[0.75,1.75,2.75,3.75,4.75]
y2=[42,26,78,15,10]
y4=[42,26,78,15,10]

plt.scatter(x1,y1,label='Datos 1', color='red')
plt.scatter(x2,y2,label='Datos 2', color='blue')
plt.plot(x1,y3,label='Linea 1', color='red', linewidth=2)
plt.plot(x2,y4,label='Linea 2', color='blue', linewidth=2)
plt.title('Grafico de dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.show()