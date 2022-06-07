"""
While / Else
Cont and Acumalations
"""

cont = 1
acum = 1

while cont <= 100:
    print(cont, acum)

    if acum > 100:
        break

    acum = acum + cont
    cont += 1
else:
    print(f"\nArrive in ELSE...")

print(f'\n\nFINISH \nAcum > 100 in cont: {cont}')