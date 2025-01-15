import sys

len1 = len(sys.argv)
print(len1)

if len1 < 2:
  print(' --- falta el nombre de archivo para procesar --')
else: 
  file = sys.argv[1]
  print(file) 
  fil = open(file+'.txt', 'r')
  datos = fil.readlines()
  fil.close()

  fil = open(file+'.rst', 'w') 

  for dd in datos:
    print(dd)
    fil.write(dd)
    fil.write('\n')
  fil.close()





