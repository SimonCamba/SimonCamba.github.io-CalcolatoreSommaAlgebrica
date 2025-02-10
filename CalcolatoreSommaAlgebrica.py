somma=0
while True:
    numero= input("Prego, inserire un numero (oppure 'x' per uscire): ")
    if numero == "x" or numero=="X":
        break
    somma+=float(numero)
print(f"La somma dei numeri inseriti è: {somma}")
