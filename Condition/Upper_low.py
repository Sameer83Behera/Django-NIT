n=int(input())

# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(n,0,-1):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# for i in range(n,0,-1):
#     for j in range(i-1):
#         print("*",end=" ")
#     print()


# for i in range(n):
#     for j in range(n-i-1):
#         print("#",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()


# count=0
# while n >0:
#     print(count)
#     count+=1
#     n-=1

# for i in range(n):
#     for j in range(i):
#         print("#",end=" ")
#     for k in range(n-i):
#         print("*",end=" ")
#     print()


# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
    

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    