import os
os.system('cls')

SBruto = int(input("Ingrese su sueldo mensual: "))
SBruto = SBruto*12

if (SBruto > 867123.1):
    SNeto = SBruto-867123.1
    SNeto = SNeto*0.25
    SNeto = SNeto+79776
    SNeto = SBruto-SNeto
    print("Le quedan", SNeto/12, "de su sueldo inicial al pagar este impuesto")
    
elif (SBruto > 624329.01):
    SNeto = SBruto-624329.01
    SNeto = SNeto*0.2
    SNeto = SNeto+31216
    SNeto = SBruto-SNeto
    print("Le quedan", SNeto/12, "de su sueldo inicial al pagar este impuesto ")
    
elif (SBruto > 416220.01):
    SNeto = SBruto-416220.01
    SNeto = SNeto*0.15
    SNeto = SBruto-SNeto
    print("Le quedan", SNeto/12, "de su sueldo inicial al pagar este impuesto")
    
else:
    print("Su sueldo sigue siendo ", SBruto/12, " aplica a este impuesto")