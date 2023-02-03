n =int(input())
count=0

for i in range(n):
    if n%i==0:
        print(i,end=";")
        count +=1
print()
if count==1:
    print(f"{n}Is prime number")
else:
    print(f"{n}is not prime number")    