# C=5(f-32)/9
# F° = (C° x 9/5) +32

print("Welcome to the temperature converter!")
user_response = input("Do you want to convert F to C or C to F? (Y/N):")
while user_response == "Y":
    # Enter a temperature value: 25
    temp_value = int(input("Enter temperature value:"))

    # Enter the temperature scale (C/F): C
    T = input("Enter the temperature scale (C/F):")
    if T == "C":
        # convert C to F
        F = (temp_value * 9/5) + 32
        # 25 Celsius is equal to 77 Fahrenheit
        print(f"{temp_value} Celsius is equal to {round(F, 3)} Fahrenheit")
    else:
        # 77 Fahrenheit is equal to 25 Celsius
        C = 5*(temp_value-32)/9
        print(f"{temp_value} Fahrenheit is equal to {round(C, 3)} Celsius")

    # Would you like to convert to another temperature? (Y/N): Y
    user_response = input(
        "Would you like to convert to another temperature? (Y/N):")
    print('-' * 50)
print("Thank You!")
