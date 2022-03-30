tax_elevations = [(10, 75720), (14, 108600),
                 (20, 174360), (31, 242400),
                 (35, 504360), (47, 649560),
                 (50, 999999999)]

tax_point_rate = 2616

while True:
    try:
        full_income = float(input(f"Insert annual income income "))
        break
    except ValueError:
        print("Incorrect input, try again.")

current_income = full_income
tax_sum = 0
previous_tax_value = 0

for rate, tax_value in tax_elevations:
    tax_length = tax_value - previous_tax_value
    if current_income - tax_length > 0:
        elevation_tax = tax_length * rate / 100
        tax_sum += elevation_tax
    else:
        elevation_tax = current_income * rate / 100
        tax_sum += elevation_tax
        break

    print(f"for rate {rate}% - the tax amount is {elevation_tax}")
    current_income -= tax_length
    previous_tax_value = tax_length

print(f"for rate {rate}% - the tax amount is {elevation_tax}")

print(f"Summary {tax_sum}")

while True:
    try:
        tax_points = float(input(f"Please insert tax points "))
        break

    except ValueError:
        print("Incorrect input, try again.")

tax_sum_points = tax_sum - tax_points * tax_point_rate
print(f"Summary {tax_sum_points} without points, for each month {tax_sum_points / 12}")
