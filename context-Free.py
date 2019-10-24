numberOfVariable=int(input("Enter how many variables: "))
numberOfTerminals=int(input("Enter how many terminal: "))
numberOfRules=int(input("Enter how many rules: "))

rules = [[] for j in range(numberOfVariable)]

variable = []
terminals = []
rules = []

rightSideString = ""
leftSideString = ""

#ESCANEO DE LAS VARIABLES(NON-TERMINAL SYMBOLS)
print("-------SCANNING VARIABLES(NON-TERMINAL SYMBOLS)---------")
for i in range(0, numberOfVariable):
    print("Set variables "+str(i+1)+" :")
    n=str(input())
    variable.append(n.lower())
variable.append("3")
print(variable)


#ESCANEO DE LAS TERMINALES
print("-------SCANNING TERMINALS---------")
for i in range(0, numberOfTerminals):
    print("Start terminal 'S' is already in")
    print("Set terminal "+str(i+1)+" :")
    n=str(input())
    terminals.append(n.upper())
terminals.append("S")
print(terminals)

#ESCANEO DE LAS REGLAS  
print("-------SCANNING RULES---------")
for i in range(0, numberOfRules):
    aux = []
    print("Which terminal use this rule: ")
    print(terminals)
    t=str(input())
    aux.append(t.upper())
    print("---Rule string: ---")
    print("list of variables: (3 for empty)")
    print(variable)
    n=str(input())
    aux.append(n)
    rules.append(aux)
print(rules)

#     FUNCTION TO CHECK THE STRING

def insertingTheString(insertionString):
  print(insertionString)







print("-------START WRITING THE RULES---------")
bandera = False
initial = False
while (bandera == False): 
    aux = []
    if initial == False:
        print("-------AVAILABLE RULES:---------")
        aux1 = []
        for indice, i in enumerate(rules):
            if(i[0] == "S"):
                print(indice+1)
                print(i)
                aux1.append(indice)
                aux1.append(i)
        #print(aux1)
        n=int(input("Enter index for rule: "))
        aux.append(aux1[n])
        print(aux)
        #print(aux[0][1])
        insertingTheString(aux[0][1])
        initial = True
            
            
        bandera = True


