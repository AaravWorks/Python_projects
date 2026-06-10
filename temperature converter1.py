print("===im temperature converter===")
print("1. for celsius to fahrenheit")
print("2. for fahrenheit to celsius")

choice = input("enter your choice (1 or 2): ")

if choice == "1":
    temp = float(input("give temperature in celsius: "))
    result = (temp * 9/5) + 32
    print("your tempreture in fahrenheit is" , result )
elif choice == "2":
    temp = float(input("give your temperature in fahrenheit"))
    result = (temp - 32) * 5/9
    print("your tempreture in celsius is", result )
