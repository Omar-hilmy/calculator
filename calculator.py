# Calculator by Omar Hilmy

print("=== Calculator ===")
print("1. +  2. -  3. *  4. /")

choice = input("Choose 1/2/3/4: ")
a = float(input("First number: "))
b = float(input("Second number: "))

if choice == "1":
    print("Result:", a + b)
elif choice == "2":
    print("Result:", a - b)
elif choice == "3":
    print("Result:", a * b)
elif choice == "4":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Can't divide by zero!")
else:
    print("Wrong choice!")
