total_bill = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid: "))
due_amount = total_bill - amount_paid
if due_amount > 0:
    print("The customer still owes:", due_amount)
elif due_amount < 0:
    print("The customer is owed change:", due_amount)
else:
    print("The bill is paid in full.")