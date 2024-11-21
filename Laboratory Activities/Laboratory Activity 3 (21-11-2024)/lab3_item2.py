def is_perfect_number(num):
    # Check if the number is equal to the sum of its proper divisors
    return num > 1 and sum(i for i in range(1, num // 2 + 1) if num % i == 0) == num


def main():
    try:
        num = int(input("Enter a number: "))
        print(f"{num} is a perfect number." if is_perfect_number(num) else f"{num} is not a perfect number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
