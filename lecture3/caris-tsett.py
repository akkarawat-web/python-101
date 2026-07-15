hours = int(input("Enter the number of hours worked: "))
pay_rate = int(input("Enter the hourly pay rate: "))

if hours > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours * pay_rate

print(f"The gross pay is ${gross_pay:,.2f}")