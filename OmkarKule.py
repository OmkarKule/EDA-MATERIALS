#reverse number

n=(int(input(" Please enter a Number ")))
rev=0
while (n!=0):
    rem=n%10
    rev=(n*10)+rem
    n=n//10
print (rem)
