n=int(input("enter n:"))
value=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("input number",value)
print("reverse number",rev)
if(value==rev):
    print("polindrome")
else:
    print("not a polindrome")
    
