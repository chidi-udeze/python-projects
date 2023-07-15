# 1. Get input from the user 
# 1.1. money_owed (Principal)
money_owed = float(input("principal  "))
# 1.2. Annual rate of interest
annual_interest = int(input("interest rate  "))
# 1.3. Payment per month
monthly_payment = float(input("monthly payment  "))
# 1.4. How many months to see the results for
months = int(input("number of months to pay loan  "))


# 2. Calculate monthly interest rate
monthly_interest_rate = annual_interest/100/12

# 3. Loop until the months the user has specified to see the results
for i in range (months):
    # 3.1 calculate the monthly interest
    monthly_interest = money_owed * monthly_interest_rate
    # 3.2 Add that interest to the money owed
    money_owed = money_owed + monthly_interest
    # 3.3 If the money_owed < monthly payment then break the loop
    if money_owed < monthly_payment:
        print(f" your loan payment will terminate on month {i+1} and the money owed will be ${round(money_owed, 2)}")
        break
    # 3.4 calculate the money_owed
    money_owed = money_owed - monthly_payment

    # 3.5 print the payment per month, Interest per month and amount due
    print(f"Month {i+1}: The monthly payment is ${round(monthly_payment, 2)}, the monthly interest is ${round(monthly_interest, 2)} and the money owed is ${round(money_owed, 2)}")
