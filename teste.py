import sys
entrada_lista = sys.stdin.readlines()

#type 0.in | python teste.py

e = entrada_lista[2].split("=")
n = int(e[1])

L_arestas = [] * (len(entrada_lista) - 4)
L_vertices = [] * n

for i in range(n):
  L_vertices.append(i+1)

for j in range(len(entrada_lista) -4):
  L_arestas.append(entrada_lista[j+4])

L_arestas.pop(1)
print(L_arestas)