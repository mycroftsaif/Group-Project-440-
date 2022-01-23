import numpy as np

data = open("scores.txt")
nd = data.read()
print(nd)

ndl = nd.split("\n")
print(ndl)

counter = int(0)
print("Scoreboard")
print("Name"+'\t'+"     Total Win")
for i in ndl:
  if i != "":
    print(i + "\n")
    counter+=int(1)
    if counter == 10:
      break

"""
k, v = np.array(list(ndl.items())).T
print(k)
print(v)

names = []
score = []

for i in ndl:
  list = i.split(";")
  names.append(list[0])
  score.append(list[1])

score = int(str(score))
print(names)
print(score)
"""
