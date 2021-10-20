# coding: utf-8
from os import system; import sys

stack = [] # Alla tal du skriver in.

system("clear || cls") # Rensar terminalen 
while True: 
    for i in range(len(stack)-1,-1,-1): 
        print("%s. %s" % (i+1, stack[i])) # Ordningen på talen man skriver in 
    stackx = input("╔═══════════════╦══════════╦══════════╦═════════════╦══════════════════════╗\n║ Nollställ [c] ║ Drop [d] ║ Swap [s] ║ Avsluta [q] ║ [+][-][*][/][^][r]ot ║\n╚═══════════════╩══════════╩══════════╩═════════════╩══════════════════════╝\nWrite a number or an operator: ") # Utseendet
    try: 
        exec({
            stackx: "stack.insert(0,float(stackx))", # RPN
            "+": "stack[0] = stack[1] + stack[0]; stack.pop(1)", # Addition
            "-": "stack[0] = stack[1] - stack[0]; stack.pop(1)", # Subtraktion
            "*": "stack[0] = stack[1] * stack[0]; stack.pop(1)", # Multiplikation
            "/": "stack[0] = stack[1] / stack[0]; stack.pop(1)", # Division
            "^": "stack[0] = pow(stack[1],stack[0]); stack.pop(1)", # Upphöjd till
            "r": "stack[0] = pow(stack[0],0.5)", # Roten ur
            "d": "stack.pop(0)", # Tar bort talet som är först
            "c": "stack.clear()", # Nollställer eller tar bort alla tal
            "s": "stack[0], stack[1] = stack[1], stack[0]", # Byter plats på första och andra talen
            "q": "sys.exit()"}[stackx]) # Avslutar koden
        system("clear || cls")   
    except Exception: print("Error: Either %s is not a valid operator or the stack does not contain enough values" % stackx) # Uppkommer om man skriver ett ogiltigt tal eller bokstav