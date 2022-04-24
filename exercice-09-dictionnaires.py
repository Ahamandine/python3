# exercice-09-dictionnaires.py

# exo 9.1
# Créez un dictionnaire nommé `my_dict` associant :
# - une clé alphanumérique et un nombre entier
# - une clé alphanumérique et un nombre à virgule flottante
# - une clé alphanumérique et une chaîne de caractères
# - une clé alphanumérique et un booléen
# Puis affichez le résultat avec un simple `print()`

# réponse 9.1
print("Exercice 9.1")
my_dict = {
    "current_year" : 2022,
    "year_month" : 30.8,
    "my_rabbit" : "Her name is Navi",
    "want_a_holiday" : True
}
print(my_dict)

# exo 9.2
# Créez un dictionnaire nommé `my_dict` associant :
# - une clé booléenne et un nombre entier
# - une clé booléenne et un nombre à virgule flottante
# - une clé numérique et une chaîne de caractères
# - une clé alphanumérique et un booléen
# Puis affichez le résultat avec un simple `print()`

# réponse 9.2
print("Exercice 9.2")

my_dict = {
    True : 5,
    False : 4.9,
    6 : "birthday month",
    "british" : False
}
print(my_dict)

# exo 9.3
# Ajoutez au dictionnaire un élément qui associe la clé alphanumérique `ipsum` à la valeur `2.71`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.3
print("Exercice 9.3")

my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
my_dict["ispum"] = 2.71
print(my_dict)

# exo 9.4
# Affichez la valeur associée à la clé 'lorem' dans le dictionnaire de 9.3

# réponse 9.4
print("Exercice 9.4")
print(my_dict["lorem"])

# exo 9.5
# Supprimez du dictionnaire la clé `foo`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.5

print("Exercice 9.5")
my_dict.pop('foo')
print(my_dict)

# exo 9.6
# Remplacez la valeur du dictionnaire associée à la clé `foo` par `123`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.6
print("Exercice 9.6")
my_dict["foo"] = 123
print(my_dict)

# exo 9.7
# En utilisant une boucle `for`, affichez les clés (et pas les valeurs) qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.7
print("Exercice 9.7")
for key in my_dict:
    print(key)

# exo 9.8
# En utilisant une boucle `for` et sans utiliser la méthode `values()`, affichez les valeurs (et pas les clés) qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.8
print("Exercice 9.8")
print(my_dict.items())


# exo 9.9
# En utilisant une boucle `for` et sans utiliser la méthode `items()`, affichez les clés et les valeurs qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
# Exemple de résultat attendu :
# key: foo, value: 42
# key: bar, value: 3.14
# key: baz, value: lorem ipsum
# etc...

# réponse 9.9
#print("Exercice 9.9")
#for key, value in my_dict:
    #print(f"key: {key}, value: {value}")

# exo 9.10
# En utilisant une boucle `for` et la méthode `items()`, affichez les clés et les valeurs qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
# Exemple de résultat attendu :
# key: foo, value: 42
# key: bar, value: 3.14
# key: baz, value: lorem ipsum
# etc...

# réponse 9.10
print("Exercice 9.10")

for key, value in my_dict.items():
    print(f'key: {key}, value: {value}')
