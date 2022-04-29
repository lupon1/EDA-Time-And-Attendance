# Un pequeño script para corregir unos fallos en un fichero CSV del INE
from os import path
import time
start = time.time()
workingPath = path.dirname(__file__)
inputFile = path.join(workingPath, 'nombresMujer.csv')
outputFile = path.join(workingPath, 'output.csv')
output = open(outputFile, 'w')
with open(inputFile, 'r', encoding='cp1252') as input:
    while True:
        line = input.readline()
        line = line.replace('.', '')
        line = line[::-1].replace(',', '.', 1)[::-1]
        output.write(line)
        print(line[:-1])
        if line == '':
            output.close()
            break
print(time.time() - start)