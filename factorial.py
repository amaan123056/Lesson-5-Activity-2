def recursive_factorial(n) :
    if n==1 :
        return n 
    else:
        return n*recursive_factorial(n-1)
number = int(input("enter your number"))
if number<0 :
    print("sorry ,factorialdoes not come exist for negative number")
elif number==0 :
    print("factorial of 0 is 1")
else:
        print("factorial of", number , "is" , recursive_factorial(number))



