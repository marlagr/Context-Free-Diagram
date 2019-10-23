numberOfVariable=int(input("Enter how many variables: "))
numberOfTerminals=int(input("Enter how many terminal: "))
numberOfRules=int(input("Enter how many rules: "))

rules = [[] for j in range(numberOfVariable)]

variable = []
terminals = []
rules = []

#ESCANEO DE LAS VARIABLES(NON-TERMINAL SYMBOLS)
for i in range(0, numberOfVariable):
    print("Set variables "+str(i+1)+" :")
    n=str(input())
    variable.append(n)
variable.append("empty")
print(variable)


#ESCANEO DE LAS TERMINALES
for i in range(0, numberOfTerminals):
    print("Set terminal "+str(i+1)+" :")
    n=str(input())
    terminals.append(n.upper())

print(terminals)

#ESCANEO DE LAS REGLAS  
for i in range(0, numberOfRules):
    aux = []
    print("Which terminal use this rule: ")
    print(terminals)
    t=str(input())
    aux.append(t)
    print("Rule sring: ")
    n=str(input())
    aux.append(n)
    rules.append(aux)

print(rules)