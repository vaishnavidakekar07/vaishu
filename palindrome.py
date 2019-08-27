n=int(input("enter the number"))
temp=n
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=int(n/10)
if(temp==rev):
        print("the given number is palindrome")
else:
         print("the given number is not palindrome")    
