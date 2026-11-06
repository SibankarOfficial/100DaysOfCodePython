print("Welcome, to Tip Calculator!")
total_bill = float(input("what was the total bill? $"))
tip_percentage = int(input("how much tip want t give, 10 , 12 , 15?"))
no_of_person = int(input("How many people to split the bill?"))
tip = (total_bill * tip_percentage/100)/ no_of_person
print(f"total tip ${round(tip, 2)}")