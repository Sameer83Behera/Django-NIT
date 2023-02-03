n=int(input())

# if n%2 == 0:
#     print("n is even")
# else:
#     print("n is odd")


if n%3 == 0 and n%5==0:
    print(f"{n} is divisble by 3 & 5")
elif n%5 == 0:
    print(f"{n} is divisble by 5")
elif n%3 == 0:
    print(f"{n} is divisble by 3")
else:
    print(f"{n} is divisble by 365")