
#Nabiha Salary
salary=float(input("Enter your Salary :"))
Month=input("En(ter the name of Month:")

saving=float(input("Enter Your Saving percentage:"))
rent=float(input("Enter Your Rent percentage:"))
electricity=float(input("Enter Your Rent percentage:"))
# Second Commit

allocating_savings=(saving/100)*salary
allocating_rent=(rent/100)*rent
allocating_electricity=(electricity/100)*electricity

total_allocating = allocating_rent +allocating_electricity + allocating_savings
Remaining_Saving=salary-total_allocating
#Remaining Saves