# Función para crear un nombre aleatorio
# Francesco Esposito - Diciembre 2021
def random_name(elem=1, sex='r', pop=0, rep=True):
    '''
    Una función que genera nombres españoles de manera aleatoria, utilizando
    los nombres y apellidos más frecuentes en España, segun los datos
    proporcionados por el Instituto Nacional de Estadística

    Args:
    elem (int) = el número de nombres que querremos generar (por defecto 1)
    sex (str) = puede ser 'm' por hombre, 'f' por mujer u omitirlo para que sea aleatorio (por defecto aleatorio)
    pop (int) = el nivel de popularid de los nombres entre 0 y 9 (donde 0 es muy común y 9 muy poco)
    rep (bool) = si los nombres a generar se pueden repetir (por defecto True).
                Si se elije False el número máximo de nombres generable es de 100

    Results:
    str or list = si el numero de elementos es 1 devuelve una cadena de texto, sino una lista de cadenas

    '''
    import csv, os, random
    actualFolder = os.path.dirname(__file__)
    apellidosCsvFile = os.path.join(actualFolder, 'apellidos.csv')
    nombresHombreCsvFile = os.path.join(actualFolder, 'nombresHombre.csv')
    nombresMujerCsvFile = os.path.join(actualFolder, 'nombresMujer.csv')
    enc = 6 # El número de elementos que hay que excludir al principio de los ficheros CSV (encabezado)
    enc += pop * 500
    numElementos = 200 # Número de elementos de los CSV que hay que usar
    numE = enc + numElementos
    if numE > 5000: return f'El nivel de popularidad debe ser un valor entre 0 y 9. {pop} no es valido'

    # Abro el file CSV y añado a una lista el número de elementos especificados
    apellidos = []
    with open(apellidosCsvFile, newline='') as f:
        data = list(csv.reader(f))
        for e in data[enc:numE]: apellidos.append(e[1])

    # Abro el file CSV y añado a una lista el número de elementos especificados
    nombresHombre = []
    with open(nombresHombreCsvFile, newline='') as f:
        data = list(csv.reader(f))
        for e in data[enc:numE]: nombresHombre.append(e[1])

    # Abro el file CSV y añado a una lista el número de elementos especificados
    nombresMujer = []
    with open(nombresMujerCsvFile, newline='') as f:
        data = list(csv.reader(f))
        for e in data[enc:numE]: nombresMujer.append(e[1])
    
    # Genero los nombres aleatoriamente y los añado a una lista
    result = []
    for e in range(elem):
        # Elijo el nombre dependiendo del sexo pasado como parametro
        # Si el parametro del sexo no ha sido pasado, lo elige aleatoriamente
        if sex == 'm':
            nombre = random.choice(nombresHombre)
            if rep == False: nombresHombre.remove(nombre)
        elif sex == 'f':
            nombre = random.choice(nombresMujer)
            if rep == False: nombresMujer.remove(nombre)
        else:
            if random.choice([True, False]):
                nombre = random.choice(nombresHombre)
                if rep == False: nombresHombre.remove(nombre)
                pass
            else:
                nombre = random.choice(nombresMujer)
                if rep == False: nombresMujer.remove(nombre)

        # Elijo aleatoriamente los apellidos
        try:
            apellido1 = random.choice(apellidos)
            if rep == False: apellidos.remove(apellido1)
            apellido2 = random.choice(apellidos)
            if rep == False: apellidos.remove(apellido2)
        except IndexError:
            return ('Se ha superado el limite máximo de nombres generables')

        # Añado el nombre a la lista
        result.append(f'{nombre} {apellido1} {apellido2}'.title())
    
    # Si el resultado es único, devuelve una cadena y sino la lista
    return result[0] if elem == 1 else result

if __name__ == '__main__':
    print(random_name(sex='f'))
