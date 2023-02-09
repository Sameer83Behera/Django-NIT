number=int(input("Enter number : "))

def lenghtOf(number):
    sum=0
    while number >0:
        rem=number%10
        sum +=1
        number=int(number/10)
    return sum

def Calculate(number,length):
    _sum=0
    while number >0:
        rem=number%10
        _sum +=rem**length
        number=int(number/10)
    return _sum

def ArmStrongNum(number):
    length=lenghtOf(number)
    Cal=Calculate(number,length)
    if number == Cal:
        print("True")
    else:
        print("False")

ArmStrongNum(number)
