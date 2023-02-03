n=int(input("Enter Values : "))

# All Side Parttern
for i1 in range(n):
    for j1 in range(i1+1):
        print("#",end=" ")
    for k1 in range(n-i1-1):
        print("*",end=" ")
    for j2 in range(n-i1-1):
        print("*",end=" ")
    for k2 in range(i1+1):
        print("#",end=" ")
    print()
for i2 in range(n):
    for j3 in range(n-i2-1):
        print("#",end=" ")
    for k3 in range(i2+1):
        print("*",end=" ")
    for j4 in range(i2+1):
        print("*",end=" ")
    for k4 in range(n-i2-1):
        print("#",end=" ")
    print()



print(" ")

for i3 in range(n):
    for j5 in range(n-i3):
        print("#",end=" ")
    for k5 in range(i3):
        print("*",end=" ")
    for j6 in range(i3):
        print("*",end=" ")
    for k6 in range(n-i3):
        print("#",end=" ")
    print() 

for i4 in range(n):
    for j7 in range(i4+1):
        print("#",end=" ")
    for k7 in range(n-i4-1):
        print("*",end=" ")
    for j8 in range(n-i4-1):
        print("*",end=" ")
    for k8 in range(i4+1):
        print("#",end=" ")
    print()
