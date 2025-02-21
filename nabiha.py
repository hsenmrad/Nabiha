#Nabiha Salary
salary=float(input("Enter your Salary :"))
Month=input("Enter the name of Month:")

saving=float(input("Enter Your Saving percentage:"))
rent=float(input("Enter Your Rent percentage:"))
electricity=float(input("Enter Your elec percentage:"))
# Second Commit

allocating_savings=(saving/100)*salary
allocating_rent=(rent/100)*rent
allocating_electricity=(electricity/100)*electricity

total_allocating = allocating_rent +allocating_electricity + allocating_savings
Remaining_Saving=salary-total_allocating
#Remaining Saves

monthly_rent=rent*12
monthly_electricity=electricity*12
yearly_rent=monthly_rent
yearly_elec=monthly_electricity

#Yearly Costs
salary_doubled=salary**2

#For Fun
add_savings= 50
 
saving_division= add_savings/allocating_savings if allocating_savings!=0 else 0
#Additional Svaing



print("\n==== Financial Summary for", Month, "====")
print(f"Salary for the month: ${salary:.2f}")
print(f"Savings allocated: ${allocating_savings:.2f}")
print(f"Rent allocated: ${yearly_rent:.2f}")
print(f"Electricity allocated: ${yearly_elec:.2f}")
print(f"Total expenses: ${total_allocating:.2f}")
print(f"Remaining salary: ${Remaining_Saving:.2f}")
print(f"Yearly rent estimate: ${yearly_rent:.2f}")
print(f"Yearly electricity estimate: ${yearly_elec:.2f}")
print(f"Salary squared (just for fun!): {salary_doubled:.2f}")
print(f"$50 extra savings divided by allocated savings: {saving_division:.2f}")
print("====================================")
