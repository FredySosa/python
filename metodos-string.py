curso = 'Curso'
string = 'Musica'

resultado = '{a} de {b}'.format(b=string,a=curso)
resultado = resultado.lower() #A minusculas
resultado = resultado.upper() #A mayúsculas
resultado = resultado.title() #Inician con mayúsculas

pos = resultado.find('Musica')
count = resultado.count('u')
resultado = resultado.replace('u','a')
resultado = resultado.split(' ')

print(count)
print(resultado)