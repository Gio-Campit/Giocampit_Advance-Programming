def check_palindrome(number):
    str_number = str(number)
    if str_number == str_number[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

user_input = int(input("Enter an integer: "))
check_palindrome(user_input)
