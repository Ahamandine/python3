# exercice-10-fonctions.py

# exo 10.1
# Créer une fonction nommée `my_sum()` qui :
# - prend deux paramètres
# - additionne ces deux paramètres
# - renvoie le résultat
# Appelez la fonction et affichez le résultat

# réponse 10.1
print("Exercice 10.1")
def my_sum(a, b):
    return a + b

a = 2
b = 4
resultat = my_sum(a, b)
print(resultat)


# exo 10.2
# Créer une fonction nommée `my_diff()` qui :
# - prend deux paramètres de type `int`
# - soustrait `b` de `a`
# - renvoit le résultat de type `int`
# Notez bien le type hinting dans la déclaration de la fonction
# Appelez la fonction et affichez le résultat

# réponse 10.2

print("Exercice 10.2")
def my_diff(a: int, b: int):
    return b - a

a = 50
b = 25
resultat = my_diff(a, b)
print(resultat)



# exo 10.3
# Créer une fonction nommée `oui_non()` qui :
# - prend un paramètre booléen
# - renvoit `oui` si le booléen est égal à True
# - renvoit `non` si le booléen est égal à False
# Appelez la fonction avec la valeur True et affichez le résultat
# Appelez la fonction avec la valeur False et affichez le résultat

# réponse 10.3

print("Exercice 10.3")


def oui_non(a: bool):
    if a == True:
        return "oui"
    else:
        return "non"

a = True
print(oui_non(a))

a = False
print(oui_non(a))

# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit True si `a` est plus grand que `b`
# - renvoit False dans les autres cas
# Appelez la fonction et affichez le résultat

# réponse 10.4
print("Exercice 10.4")

def is_greater(a: float, b: float):
    if a > b:
        return True
    else:
        return False

a = 34.3
b = 33.2
print(is_greater(a, b))

# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit 1 si `a` est plus grand que `b`
# - renvoit -1 si `a` est plus petit que `b`
# - renvoit 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5
print("Exercice 10.5")

def compare(a: float, b: float):
    if a > b:
        return "1"
    elif a < b:
        return "-1"
    else: 
        return "0"

a = 4.31
b = 3.14
print(compare(a, b))

a = 5.30
b = 6.31
print(compare(a, b))

a = 30
b = 30
print(compare(a, b))

# exo 10.6
# La formule suivante permet de convertir des mètres en miles :
#
#       miles = meters / 1609.344
#
# La formule suivante permet de faire l'inverse :
#
#       meters = miles * 1609.344
#
# Créez une fonction nommée :
#
# - meters_to_miles() permettant de convertir des mètres en miles
# - miles_to_meters() permettant de convertir des miles en mètres
#
# Ensuite convertissez les valeurs :
#
# - 1 Km en miles
# - 10 miles en mètres
#
# Appelez les fonctions et affichez les résultats

# réponse 10.6
print("Exercice 10.6")

def meters_to_miles(a):
    return a * 1609.344

a = 1000
print(meters_to_miles(a))

def miles_to_meters(b):
    return b / 1609.344

b = 10
print(miles_to_meters(b))

# exo 10.7
# Créer une fonction nommée `compute_tax()` qui :
# - prend un paramètre nommé `price` de type `float`
# - prend un paramètre nommé `tax_type` de type `int`
# - ajoute une taxe de 2,1 % à `price` si `tax_type` est égal à `1`
# - ajoute une taxe de 5,5 % à `price` si `tax_type` est égal à `2`
# - ajoute une taxe de 10 % à `price` si `tax_type` est égal à `3`
# - ajoute une taxe de 20 % à `price` si `tax_type` est égal à `4`
# - renvoit le prix initial si `tax_type` n'est pas reconnu
# Appelez la fonction et affichez le résultat avec un montant de 100 € pour chaque type de taxe
#
# Référence : [Quels sont les taux de TVA en vigueur en France et dans l'Union européenne ? | economie.gouv.fr](https://www.economie.gouv.fr/cedef/taux-tva-france-et-union-europeenne)

# réponse 10.7
print("Exercice 10.7")

def compute_tax(price: float, tax_type: int):
    if tax_type == 1:
        return price + (price * (2.1 / 100))
    elif tax_type == 2:
        return price + (price * (5.5 / 100))
    elif tax_type == 3:
        return price + (price * (10 / 100))
    elif tax_type == 4:
        return price + (price * (20 / 100))
    else:
        print(price)


price = 100
tax_type = 1
print(compute_tax(price, tax_type))

price = 100
tax_type = 2
print(compute_tax(price, tax_type))

price = 100
tax_type = 3
print(compute_tax(price, tax_type))

price = 100
tax_type = 4
print(compute_tax(price, tax_type))
