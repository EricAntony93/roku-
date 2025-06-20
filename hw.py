#Sum of digits
sum=0
n=0
i=int(input("enter a number"))
while i>0:
    n=i%10
    sum+=n
    i=i//10
print(sum)

#count the number of digits#Sum of digits
n=0
count=0
i=int(input("enter a number"))
while i>0:
    n=i%10
    count +=1
    i=i//10
print(count)

#armstrong number or not
n=0
sum=0
i=int(input("enter a number"))
temp=i
while temp>0:
    n=temp%10
    sum+=n**3
    temp=temp//10
if sum==i:
    print("it is an armstrong number")
else:
        print("it is not an armstrong number")

#palindrome or not
temp=0
rev=0
i=int(input("enter a number"))
temp=i
while temp>0:
    n=temp%10
    rev=rev*10+n
    temp=temp//10
if rev==i:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")