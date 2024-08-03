n=int(input("enter the number of rows for pyramid: "))
for x in range(1,n+1):
    space="  "*(n-x)
    star="* "*((2*x)-1)
    print(space+star)
for x in range(n-1,0,-1):
    space="  "*(n-x)
    star="* "*((2*x)-1)
    print(space+star)



lines = []
for x in range(1, n + 1):
    space = "  " * (n - x)
    star = "* " * ((2 * x) - 1)
    lines.append(space + star)
    print(space+star)

for line in reversed(lines):
    print(line)
