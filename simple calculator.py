print("")
print("           CALCULATOR          ")
print("")
a=int(input("Enter a number: "))
b=int(input("Enter second number: "))
print("")
print("What operation would you like to perform?")
op=input("Choose a operator(+,-,*,/): ")
if op== '+':
    print("Sum =",a+b)
elif op=='-':
    print("Difference =",a-b)
elif op=='*':
    print("Product =",a*b)
elif op=='/':
    try:
        print("Division =",a/b)
    except ZeroDivisionError:
        print("Cannot divde by zero!")
else:
    print("INVALID OPERATOR")

