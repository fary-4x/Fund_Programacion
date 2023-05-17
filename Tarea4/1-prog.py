import os
os.system('cls')

def main():
   l1 = float(input("Ingrese el valor del primer lado:"))
   l2 = float(input("Ingrese el valor del segundo lado:"))
   l3 = float(input("Ingrese el valor del tercer lado:"))
   
   if(l1==l2 and l2==l3):
       print ("\nEl Triangulo es Equilatero")
   elif(l1==l2 or l1==l3 or l2==l3):
       print ("\nEl Triangulo es Isoceles")
   elif (l1!=l2 or l1!=l3 or l2!=l3):
       print ("\nEl Triangulo es Escaleno")

if __name__ == '__main__':
   main()

    
   