import numpy as np
import json
names = open("winners.txt")
board = open("scores.txt",'w')

nd = names.read()

ndl = nd.replace('\n',"").split(";")
print(ndl)
print(type(ndl))
dndl = []
dndl2 = []

names.close()
names2 = open("winners.txt",'w')
print('Enter your name:')
x = input()
new_ndl = np.append(ndl,x)

for r in new_ndl:
  if r != "":
    dndl.append(r)
    dndl2.append(r)

for m in new_ndl:
  if m != "":
    names2.write(m + ';')

i = int(0)
wintot = []
winname = []

def my_function(x):
  return list(dict.fromkeys(x))

dndl2 = my_function(dndl2)
print(dndl2)

for x in range(len(dndl2)):
  for y in range(len(dndl)):
    if dndl2[x] == dndl[y]:
      i+=int(1)
  wintot.append(i)
  print(wintot)
  winname.append(dndl2[x])
  print(winname)
  i = 0


list = []
dict2 = {}

for n in winname:
  for v in wintot:
    dict2[n] = v
    wintot.remove(v)
    break


print(dict2)

list = sorted(dict2.items(), key=lambda x:x[1], reverse=True)
print(list)
print(type(list))

for t in list:
  board.write('\t\t'.join(str(s) for s in t) + '\n')

names2.close()
board.close()
