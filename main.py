print("========== Electricity Bill Calculator ==========")

name = input("Enter Customer Name: ")
units = float(input("Enter Units Consumed: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
else:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 6)

tax = bill * 0.05
total = bill + tax

print("\n========== BILL DETAILS ==========")
print("Customer Name :", name)
print("Units Consumed:", units)
print("Electricity Bill: ₹", round(bill, 2))
print("Tax (5%): ₹", round(tax, 2))
print("Total Amount: ₹", round(total, 2))
print("==================================")
