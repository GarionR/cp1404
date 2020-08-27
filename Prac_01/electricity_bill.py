TITLE = "Electricity bill estimator"
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print(TITLE)

price = float(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
number_of_days = float(input("Enter number of billing days: "))

estimated_bill = (price * daily_use * number_of_days) / 100
print("Estimated bill: ${:.2f}".format(estimated_bill))

print(TITLE, "2.0")
tariff = 0
while not tariff:
    tariff_choice = int(input("Which tariff? 11 or 31: "))
    if tariff_choice == 11:
        tariff = TARIFF_11
    elif tariff_choice == 31:
        tariff = TARIFF_31

daily_use = float(input("Enter daily use in kWh: "))
number_of_days = float(input("Enter number of billing days: "))
estimated_bill = tariff * daily_use * number_of_days
print("Estimated bill: ${:.2f}".format(estimated_bill))
