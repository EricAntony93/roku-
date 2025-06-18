a = int(input("enter your mark: "))

if a<=100 and a>=0:
    if a>=90:
        print("A grade")
    elif a>=80:
        print("B grade")
    elif a>=70:
        print("C grade")
    elif a>=60:
        print("D grade")
    elif a<=59:
        print("E grade")
else:
    print("invalid number")