numberOfVariable=int(input("Enter how many variables: "))
numberOfTerminals=int(input("Enter how many terminal: (INITIAL TERMINAL S is ALREADY IN)"))
numberOfRules=int(input("Enter how many rules: "))

rules = [[] for j in range(numberOfVariable)]

variable = []
terminals = []
rules = []

rightSideString = []
leftSideString = []
queue = ["S"]

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



#     FUNCTION TO MAP index with rule

def mappingRules(lista, indice):
  for indx, i in enumerate(lista):
    if(i == indice):
        return lista[indx+1]

#     FUNCTION TO get the rule string from terminal
def showingAvailableRules(term):
    aux = []
    print("-------AVAILABLE RULES:---------")
    aux1 = []
    for indice, i in enumerate(rules):
        if(i[0] == term):
            #print(indice+1)
            #print(i)
            aux1.append(indice)
            aux1.append(i)
    if aux1:
        print(aux1)
        n=int(input("Enter index for rule: "))
        aux.append(mappingRules(aux1, n))
        #print(aux)
        #print(aux[0][1])
        return aux[0][1]
    else :
        print("There are no more rules available")


#     FUNCTION TO CHECK THE STRING

def insertingTheString(insertionString):
    foundUpperLetter = False
    for i in insertionString:
        if not foundUpperLetter:
            if i == "3" :
                rightSideString.append(i)
                return
            elif i.islower():
                rightSideString.append(i)
                print(rightSideString+leftSideString)
            elif i.isupper():
                queue.append(i)
                foundUpperLetter = True
        else:
            if i == "3" :
                leftSideString.append(i)
                return
            elif i.islower():
                leftSideString.append(i)
            elif i.isupper():
                queue.append(i)
    






print("-------START WRITING THE RULES---------")


while (queue): 
    ruleString = showingAvailableRules(queue[0])
    insertingTheString(ruleString)
    queue.remove(queue[0])
print(rightSideString+leftSideString)
