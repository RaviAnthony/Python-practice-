"""
#Write a program to add two numbers

a = input("enter value of a:")
b= input("enter value of b:")

c = a + b
print c

"""

# didn't get the question. Write a program to generate a random number of "n" number of digits/letters. "n" should be function parameters. 

"""
#Write a program to check whether the given number is a prime number. This number is given as a function parameter.

def prime(n):
     
    if n > 1:
        for i in range(2,n):
            if (n % i == 0):
                return False
    return True
        
            
   
print prime(int(raw_input("enter a number:")))

"""
#Write a program to generate prime numbers from 1 to n.

first = int(input("Enter first number: "))
last = int(input("Enter last number: "))

for num in range(first,last + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)


