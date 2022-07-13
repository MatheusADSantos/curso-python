"""
Printar na tela:
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
Usando for/while
"""

# Minha soluçã
print(f'\nMinha Solução (Usando RLM -> PA):')
cont = 10
for n in range(0, 9, 1):
    m = n + cont
    print(n, m)
    cont -= 2

# -----------------------------

print(f'\nSolução do professor:')
for progressão_de_cada_loop, decrescente_10 in enumerate(range(10, 2, -1)):
    print(progressão_de_cada_loop, decrescente_10)