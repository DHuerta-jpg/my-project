#Diccionario
persona={
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Chihuahua',
    'trabajo': 'programador'
}
print(persona['nombre'],persona['edad'],persona['ciudad'],persona['trabajo'])

#Ver. 2
diccionario= dict([
    ('Nombre', 'Fer'),
    ('Edad', 18),
    ('Matrícula', 'L00016437'),
])
diccionario['Dirección'] = "Calle 123"
print(diccionario)

#diccionario['Nombre'] = "Clara"
#print(diccionario)

#print(diccionario['Nombre']) 
#print(diccionario.get('Nombre'))