file='fecha_rango_M4D7y26_titulos'

fil = open(file+'.txt', 'r')
datos = fil.readlines()
fil.close()

filo = open(file+'.rst', 'w')

filo.write(file+'\n')
filo.write('==================='+'\n')
filo.write('\n')

for ss in datos:
  filo.write('* '+ss)

filo.close()





