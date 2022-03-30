rate = 50
hours = {"REG HOURS": 1.00, "125%": 1.25, "150%": 1.50, "175%": 1.75, "200%": 2.00, "130%": 1.30, "30%": 0.30,
         "SIC PAYY": 1, "WORKING DAYS (commute payment) ": 31.8 / rate}
calculated = {}
sum = 0

for hour_name, hour_value in hours.items():
    while True:
        try:
            calculated[hour_name] = float(input(f"Insert {hour_name} amount")) * hour_value * rate
            sum += calculated[hour_name]
            break
        except ValueError:
            print("Incorrect input, try again.")

print(f"Summary {sum}, detailed payment:\n{calculated}")
