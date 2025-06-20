num = float(input('Enter a number:'))
if(num <=100):
    res = num* 5
elif(num<=200 and num>=101):
    res = (100*5)+((num-100)*8)
elif(num>200):
    res = (100*5)+(100*8)+((num-200)*10)

print(res)