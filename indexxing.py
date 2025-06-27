# a="Hello World"
# print(a[0:5])

# a="Hello World"
# print(a[0:9:2])

# a="Hello World"
# print(a[::-1])

# a="Hello World"
# print(a[::-1])
# a[1]="y"
# print(a)

#string functions and methods
#lowercase
# message="PYTHON IS FUN"
# print(message.lower())

#uppercase
# message="python is fun"
# print(message.upper())

#count
# txt="i love apples,apples are my favourite fruit"
# x=txt.count("p")
# print(x)

#find
# message="python is a fun programming language"
# print(message.find("fun"))

#replace
# text="Bat Ball"
# replaced_text=text.replace("Ba","Ro")
# print(replaced_text)

#append
# numbers=[21,34,54,12]
# print("before append:",numbers)
# numbers.append(32)
# print("after append:",numbers)

#insert
# vowel=['a','e','i','u']
# vowel.insert(3,'o')
# print('List:',vowel)

#extend
# prime_numbers=[2,3,5]
# print("List1:",prime_numbers)
# even_numbers=[4,6,8]
# print("List2:",even_numbers)
# prime_numbers.extend(even_numbers)
# print("List after append:",prime_numbers)

#change
# languages=['Python','Swift','C++']
# languages[2]="C"
# print(languages)

a=[]
x=int(input("enter your numbers:"))
for i in range(0,x):
    value=int(input("enter your values:"))
    a.append(value)
print(a)