
nombre1 = input("Entrez un nombre entier: ")
nombre2 = input("Entrez un nombre entier: ")

if not nombre1.isnumeric() or not nombre2.isnumeric()
print ("ce ne sont pas des nombres entiers")
raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

operation =input("Choisissez une opération  ['+', '-', '*' ou '/']: ")
if operation not in ['+', '-', '*' , '/']
print ("ce n’est pas une opération possible")
raise SystemExit("Fin du programme")


 if  operation == '/' 
       match nombre2:
       case nombre2 ==0
       print ("il n’est pas possible de diviser par zéro")
      case nombre2 = !"0"
      resultat=(nombre1/nombre2)
      
elif operation == '+'
resultat=nombre1+nombre2

elif operation == '-'
resultat=nombre1-nombre2

else operation == '*'
resultat= nombre1*nombre2
  
resultat=round(resultat)
print(resultat)
