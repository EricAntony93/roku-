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
# n=5
# for i in range(0,5):
#     for j in range(0,n-1):
#         if(i==0 or i==2 or i==4 or j==0 or j==4 or j==4):
#              print(" ",end="*")
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