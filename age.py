# ask the user for input
#n=int(input("what's your age?"))
#print(n)

# save the input to a variable
n=int(input("what's your age?"))

# calculate the decades and years
decade =n//10 
dob =2023-n

# Convert these numbers to text
decade =str(decade)
dob =str(dob)

# print the results - "It has been X decades (birth year Y)"
print(f"It has been {decade} decades (birth year {dob})")
