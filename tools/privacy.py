# Script para editar la base de datos del Anviz CrossChex
from unicodedata import name
import pyodbc as db
import os, randomName
from genderize import Genderize

def normalize(s):
    s = s.lower()
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b)
    return s

# Para ver los driver disponibles
# print(db.dataSources())
# print(db.drivers())

# Configuro variables
fileName = 'TimeAndAttendance.mdb'
actualFolder = os.path.dirname(__file__)
database = os.path.join(actualFolder, fileName)
driver = 'Microsoft Access Driver (*.mdb, *.accdb)' # Trabajo
password = ''
connectString = (f'DRIVER={driver};DBQ={database};PWD={password}')

# Me conecto al database
con = db.connect(connectString)
cur = con.cursor()

# Saco toda la tabla UserInfo y la pongo en una lista de listas
SQL = 'SELECT * FROM UserInfo;' # your query goes here
rows = cur.execute(SQL).fetchall()

# Saco solo los nombres y los pongo en una lista
names = []
for row in rows:
    names.append(row[2])

# Applico i cambi al database
count = noCount = 0
for originalName in names:
    name = normalize(originalName.split()[0])
    response = Genderize().get([name])
    gender = response[0]['gender']
    if gender == 'male':
        newName = randomName.random_name(sex='m')
        print(name, gender, newName)
        count += 1
    elif gender == 'female':
        newName = randomName.random_name(sex='f')
        print(name, gender, newName)
        count += 1
    else:
        newName = f'NO SEX: {name}'
        print('*** Sexo no detectado:', name)
        noCount += 1
    cur.execute("UPDATE UserInfo SET name = ? WHERE name = ?", newName, originalName)
print(f'{count} nombres cambiados con éxito')
print(f'{noCount} nombres no han sido identificados')

# Applico i cambi al cursore
con.commit()
# Chiudo cursore e connessione
cur.close()
con.close()