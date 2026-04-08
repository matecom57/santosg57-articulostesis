file = 'abstract-20260401.rst'

fil = open(file, 'r')

datos = fil.readlines()
fil.close()

print(len(datos))

k = 1

ban = 0
i=0
while i < len(datos):
  ss = datos[i]
  ss = ss.replace('\n','')
#  print(ss)
  if k < 10:
    if str(k)+'.' == ss[:2]:
      print(ss)
      k = k+1
      i = i+1
      ban = 1
  elif k < 100:
    if str(k)+'.' == ss[:3]:
      print(ss)
      k = k+1
      i = i+1
      ban = 1
  elif k < 1000:
    if str(k)+'.' == ss[:4]:
      print(ss)
      k = k+1
      i = i+1
      ban = 1
  elif k < 10000:
    if str(k)+'.' == ss[:5]:
      print(ss)
      k = k+1 
      i = i+1
       ban = 1
  if ban == 1:
      ss = datos[i]
      ss = ss.replace('\n','')
      if len(ss > 0):
      
  i = i+1
