## **Ejercicio 1: Diccionario de mascota**
pet = {"name": "Fido", "type": "dog", "age": 5, "color": "brown"}
print(pet)

pet["owner"] = "Juan"
pet["age"] += 1
del pet["color"]
print(pet)


## **Ejercicio 2: Información personal**
person = {"first_name": "Maria", "last_name": "Gomez", "age": 30, "city": "Lima"}
print(person["city"])

person["phone"] = "987654321"
person["age"] += 5
del person["phone"]
print(person)


## **Ejercicio 3: Almacén de productos**
product = {"name": "Laptop", "price": 1500, "quantity": 20}
product["quantity"] += 10
print(product["price"])

product["category"] = "Electronics"
del product["price"]
print(product)


## **Ejercicio 4: Libro favorito**
book = {"title": "Cien años de soledad", "author": "Gabriel Garcia Marquez", "year": 1967, "pages": 471}
book["pages"] += 20
book["genre"] = "Magical realism"

print(book["title"], "por", book["author"])
del book["year"]
print(book)


## **Ejercicio 5: Diccionario de comida**
food = {"name": "Apple", "type": "Fruit", "calories": 95}
food["is_healthy"] = True
food["calories"] -= 50
del food["type"]
print(food)


## **Ejercicio 6: Actualización de contactos**
contact = {"name": "Carlos", "email": "carlos@example.com", "phone": "123456789"}
contact["phone"] = "987654321"
contact["address"] = "123 Main St"
del contact["email"]
print(contact)
