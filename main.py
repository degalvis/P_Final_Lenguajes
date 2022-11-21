from analizador import analizador
from tkinter import *
def main():
    sujetoInput = input("Ingrese una un sujeto: ")
    verboInput = input("Ingrese una un verbo: ")
    predicadoInput = input("Ingrese una un predicado: ")
    
    sujetoInput = sujetoInput.lower()
    verboInput = verboInput.lower()
    predicadoInput = predicadoInput.lower()
    
    l = analizador(sujetoInput, verboInput, predicadoInput)
    booleano = l.analizarSintaxis()
    
    if booleano:
        print("Oración correcta")
    else:
        print("Oración incorrecta")
    
main()