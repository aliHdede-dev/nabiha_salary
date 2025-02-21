salary = float(input("Please enter your salary: "))
month = input("Please enter the month: ")
savings_percentage = float(input("Please enter the percentage of salary to save: "))
rent_percentage = float(input("Please enter the percentage of salary to spend on rent: "))
electricity_percentage = float(input("Please enter the percentage of salary to spend on electricity: "))

savings_amount = salary * savings_percentage / 100
rent_amount = salary * rent_percentage / 100
electricity_amount = salary * electricity_percentage / 100

total_amount = savings_amount + rent_amount + electricity_amount

salary_remainder = salary - total_amount

yearly_rent = rent_amount * 12
yearly_electricity = electricity_amount * 12

double_salary = salary * 2

additional_savings = 50
savings_left = additional_savings / savings_amount

print(f"your salary is: {salary}")
print(f"your savings amount is: {savings_amount}")
print(f"your rent amount is: {rent_amount}")
print(f"your electricity amount is: {electricity_amount}")
print(f"your total amount is: {total_amount}")
print(f"your salary remainder is: {salary_remainder}")
print(f"your yearly rent is: {yearly_rent}")
print(f"your yearly electricity is: {yearly_electricity}")
print(f"your double salary is: {double_salary}")
print(f"your savings left is: {savings_left}")

# i did not know how to show results for several months so i just showed the results for one month