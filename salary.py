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