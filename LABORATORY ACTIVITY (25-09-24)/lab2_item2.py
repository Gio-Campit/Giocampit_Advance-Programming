def calculate_discount(amount):
    if amount > 5000:
        discount = 0.10  
    else:
        discount = 0.05  
    return discount
def main():
    while True:
        purchase_amount = float(input("Enter the total purchase amount: "))
        
        discount_percentage = calculate_discount(purchase_amount)
        discount_amount = purchase_amount * discount_percentage
        final_amount = purchase_amount - discount_amount
        
        print(f"Initial Purchase Amount: {purchase_amount:.2f}")
        print(f"Discount: {discount_amount:.2f}")
        print(f"Final Price: {final_amount:.2f}")
        
        try_again = input("Do you want to try again? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Thank you!")
            break
main()
