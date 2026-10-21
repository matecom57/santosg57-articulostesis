file = 'abstract-20261020-21.txt'

fil = open(file, 'r')

datos = fil.readlines()

k = 1

ln = len(datos)
i = 0

while i < ln:
  ss = datos[i]
  ss = ss.replace('\n', '')
  kk = str(k)+'. '
  if k < 10:
    ss2 = ss[:3]
  elif k < 100:
    ss2 = ss[:4]
  elif k < 1000:
    ss2 = ss[:5]
  else:
    ss2 = ss[:6]
  if ss2 == kk:
      print(ss)
      j = i+1
      while j < ln:
        ss = datos[j]
        ss = ss.replace('\n', '')
        if len(ss) == 0:
          i = j
          break
        else:
          print(ss)
        j = j+1
      k = k+1
  i = i+1

