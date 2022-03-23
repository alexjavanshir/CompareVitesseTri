import random
import timeit

def gener_liste(taille):
  
  liste = [random.randrange(1, 100, 1) for i in range(taille)]
  return liste
  
def tri_selec(t):
  
  debut= timeit.default_timer()

  n = len(t)
  for i in range(0, n-1):
    m = i
    for j in range(i+1, len(t)):
      if t[j] < t[m]:
        m = j
    if m != i:
      t[i], t[m] = t[m], t[i]

  fin= timeit.default_timer()
  duree=(fin-debut)*1000
  return t,duree

def tri_inser(t):
  debut= timeit.default_timer()
  n = len(t)
  for i in range(1, n):
    x = t[i]
    j=i
    while j >0 and t[j-1]>x:
      t[j]=t[j-1]
      j=j-1
    t[j]=x
  
  fin= timeit.default_timer()
  duree=(fin-debut)*1000

  return t,duree  

t = gener_liste(1000)
moyenne_temps_selec = 0
moyenne_temps_inser = 0
nombre_de_repetition = 5

for i in range(0,nombre_de_repetition):
  triSelect,dureeSelect= tri_selec(t.copy())
  moyenne_temps_selec += dureeSelect

  triInsert,dureeInsert= tri_inser(t.copy())
  moyenne_temps_inser += dureeInsert

print("Tri selection : ", moyenne_temps_selec/nombre_de_repetition)
print("Tri insertion : ",moyenne_temps_inser/nombre_de_repetition)