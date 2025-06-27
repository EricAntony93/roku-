# text = input("enter a string:")
# reverse = ""
# for i in text:
#     reverse = i + reverse
#     print("reversed string is ",reverse)

#  or
 
# a = text[::-1]
# print(a)


#floyds triangle
# n = 4
# count=0
# for i in range (0,n):
#     for j in range(0,i+1):
#         count+=1
#         print(count,end="")
#     print()


#full pyramid
# n = 5
# for i in range (0,n):
#     for j in range(0,n-i):
#         print(" ",end="")

#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()


#rhombus pattern
# n = 5
# for i in range (0,n):
#     for j in range(0,i+1):
#         print(" ",end="  ")

#     for k in range(0,n+1):
#         print("*",end=" ")
#     print()


#inverted right half pyramid
# n = 5
# for i in range (0,n):
#     for j in range(0,n-i):
#         print(" ",end="*")

#     for k in range(0,i+1):
#         print("    ",end="   ")
#     print()


#inverted full pyramid
# n = 5
# for i in range (0,n):
#     for j in range(0,i):
#         print(" ",end="")

#     for k in range(0,n-i):
#         print("",end=" *")
#     print()


#inverted left half pyramid
# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end=" ")

#     for k in range(0,n-i):
#         print("*",end=" ")
#     print()


#diamond pattern
# n = 5
# for i in range (0,n):
#     for j in range(0,n-i):
#         print(" ",end="")

#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()
# n = 5
# for i in range (1,n):
#     for j in range(0,i+1):
#         print(" ",end="")

#     for k in range(0,n-i):
#         print("*",end=" ")
#     print()

#hourglass pattern
# n = 5
# for i in range (0,n):
#     for j in range(0,i+1):
#         print(" ",end="")

#     for k in range(0,n-i):
#         print("*",end=" ")
#     print()
# n = 5
# for i in range (1,n):
#     for j in range(0,n-i):
#         print(" ",end="")

#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()

#hollow square
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             print("* ",end="")
#         else:
#             print(" ",end=" ")
#     print()

#E
# n=5
# for i in range(0,5):
#     for j in range(0,n-1):
#         if(i==0 or i==2 or i==4 or j==4 or j==0 or j==n):
#              print(" ",end="*")
#         else:
#             print("",end="")
#     print()

#e
# n=6
# for i in range(0,5):
#     for j in range(0,n-1):
#         if(i==0 or i==2 or i==4  or j==0  or j==5):
#              print(" *",end="")
#         else:
#             print("",end="")
#     print()


#hollow diamond
# n = 5
# for i in range(0, n):
#     for j in range(0, n - i):
#         print(" ", end="")

#     for k in range(0, i + 1):
#         if k == 0 or k == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(1, n):
#     for j in range(0, i + 1):
#         print(" ", end="")

#     for k in range(0, n - i):
#         if k == 0 or k == n - i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

 #Hollow full pyramid
# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(end=" ")
#     for k in range(0,i+1):
#         if(i==0  or k==0 or k==n-1 or i==n-1 or k==i ):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#inverted hollow pyramid
# n = 5
# for i in range (0,n):
#     for j in range(0,i+1):
#         print(" ",end="")

#     for k in range(0,n-i):
#         if(i==0 or k==0 or k== n - i - 1 ):
#             print("",end=" *")
#         else:
#             print(" ",end=" ")
#     print()

#while loop
# choice=0
# res=0
# while True:
#     print("1.ADDITION")
#     print("2.SUBSTRACTION")
#     print("3.MULTIPLICATION")
#     print("4.DIVISION")
#     print("5.EXIT")
#     choice = int(input("enter your choice:"))
    
#     if choice==1:
#         a=int(input("enter your number:"))
#         b=int(input("enter  your number:"))
#         res=a+b 
#     elif choice==2:
#         a=int(input("enter your number:"))
#         b=int(input("enter  your number:"))
#         res=a-b
#     elif choice==3:
#         a=int(input("enter your number:"))
#         b=int(input("enter  your number:"))
#         res=a*b
#     elif choice==4:
#         a=int(input("enter your number:"))
#         b=int(input("enter  your number:"))
#         if b==0:
#             print("invalid")
#         else:
#             res=a/b
#     elif choice==5:
#         break
#     else:
#         print("invalid choice")
#     break
#     print(res)
    
#registration
# choice=0
# name=0
# age=0
# address=0
# username=0
# password=0
# usrname=0
# pass2=0
# phone=0
# while True:
#     print("1.REGISTRATION")
#     print("2.LOGIN")
#     choice=int(input("enter your choice: "))
#     if choice==1:
#         name=(input("Enter your name:"))
#         age=(input("Enter your age:"))
#         address=(input("Enter your address:"))
#         username=(input("Enter your username:"))
#         password=(input("Enter your password:"))
#         phone=str(input("enter your phone number:"))
#         if len(phone)==10:
#             break
#         else:
#             print("Invalid")
#     elif choice==2:
#         usrname=(input("Enter the username:"))
#         pass2=(input("Enter the password:"))
#     if usrname==username and pass2==password and int(age)>=18 and len(phone)==10:
#             print("Name: ",name)
#             print("Address:",address)
#             print("Age:",age)
#             print("Phone:",phone)
#     else:
#          print("Invalid") 

