## Input we need from the user
## Total rent
## Total food ordered for snacking 
## Electricity units speed
## Charge per unit 
# Persons living in room/flat
## output 
## Total amount you've to pay is 

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food order = "))
electricity_units = int(input("Enter the total electricity units = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

total_electricity_bill = electricity_units * charge_per_unit
total_amount = rent + food + total_electricity_bill

each_person_pay = total_amount / persons

print("Each person has to pay = ", each_person_pay)
print("Total amount you've to pay is =", total_amount)