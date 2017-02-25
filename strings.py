mi_cadena = """Funciona con varios tipos de comillas comillas?"""

print(mi_cadena)

nombre = "Fredy"
curso = "python 3"

concat1 = "Nuevo curso de "+curso+" que lo toma "+nombre
concat2 = "Nuevo curso de %s que lo toma %s" %(curso,nombre)
concat3 = "Nuevo curso de {} que lo toma {}".format(curso,nombre)

print(concat1)
print(concat2)
print(concat3)