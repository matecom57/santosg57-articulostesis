
from deep_translator import GoogleTranslator
import sys

print(sys.argv)

file = sys.argv[1]

#file = 'fmri_2022_3000_titulos.txt'

fil = open(file, 'r')

datos = fil.readlines()

k = 1
for ss in datos:
  ss = ss.replace('\n', '')
  ss2 = ss[13:]
  print(ss2)
  if len(ss2) > 12:
    traduccion = GoogleTranslator(source='en', target='es').translate(ss2)
    print(str(k) + ' - ' + traduccion) # Salida: Hola, ¿cómo estás?
    print('  ')
  k = k+1
  
