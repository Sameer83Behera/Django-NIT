_range=int(input("Enter : "))
_sum=0
length=0


# while n>0:
#     rem =n%10
#     _sum += rem
#     n= int(n/10)
# print(_sum) 

#Reverse number 
#---------------

# while n>0:
#     rem=n%10
#     _sum=_sum*10+rem
#     n=int(n/10)
# print(_sum)
 

# #Plindrome 
# #----------

# while n>0:
#     rem=n%10
#     _sum=_sum*10 + rem
#     n=int(n/10)

# if temp == _sum:
#     print(f"{_sum} is palindrome")
# else:
#     print(f"{_sum} is not plindrome")


#Antrome Number

for i in range(_range):
    n=i
    _sum=0
    temp=n
    length=0
    temp_size=n




while temp_size > 0:
    temp_size = int(temp_size/10)
    length+=1

while n>0:
    rem=n%10
    _sum +=(rem**length)
    n=int(n/10)

if temp == _sum:
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")




