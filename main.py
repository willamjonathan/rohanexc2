rows = eval(input("How many rows do you want:"))
for i in range(rows):
    print(" "*(rows-i),end="")
    for j in range(1,i+2):
        print("*",end="")
    print()
