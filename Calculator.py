a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print(
    "1.Addition\n"
    "2.Subtraction\n"
    "3.Multiplic\n"
    "4.Division"
)
choice = int(input("Enter your choice:"))

if  choice == 1:
    print("result =",a+b)

elif choice == 2:
    print("result =",a-b)

elif choice == 3:
    print("result =",a*b)
    
elif choice == 4:
    if b != 0:
        print("result =",a/b)
    else:
        print("Division by Zero is not allowed")
else:
    print("Invalid Choice")

