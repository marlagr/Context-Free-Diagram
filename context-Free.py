numberOfVariable=int(input("Enter how many variables: "))
numberOfTerminals=int(input("Enter how many terminal: "))
numberOfRules=int(input("Enter how many rules: "))

rules = [[] for j in range(numberOfVariable)]

variable = []
terminals = []

print("number of terminal", numberOfTerminals)
for i in range(numberOfTerminals):
    print("Set terminal "+str(i)+" :")

print(terminals)