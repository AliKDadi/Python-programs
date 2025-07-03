#BSCIT-05-0836/2022
#Prime numbers
def prime(n):
    if n<2:
        return False
    if n%2==0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
        return True

#Prime numbers in a range
def prime_number():
#prompt user to enter the range
    start=int(input("Enter the starting number of the range: "))
    end=int(input("Enter the ending number of the range: "))

    if start>end:
        print("start should be less than end!")
        return []

#prime numbers in the range
    Prime=[n for n in range(start, end+1) if prime(n)]
    return Prime

#call function and print result
print("Prime numbers in the range:",prime_number())


