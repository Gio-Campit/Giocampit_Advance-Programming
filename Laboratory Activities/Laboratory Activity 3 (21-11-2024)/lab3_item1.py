def roman_to_integer(roman):
    # Define the dictionary mapping Roman numerals to integer values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    
    roman = roman.upper()  # Ensure the input is uppercase for processing
    total = 0
    prev_value = 0

    # Process Roman numeral from right to left
    for char in reversed(roman):
        if char not in roman_values:
            return f"Invalid Roman numeral: {roman}"
        
        current_value = roman_values[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total


def main():
    roman = input("Enter a Roman numeral: ").strip()
    result = roman_to_integer(roman)
    
    if isinstance(result, str):  # Handle invalid input
        print(result)
    else:
        print(f"The integer value of '{roman.upper()}' is: {result}")


if __name__ == "__main__":
    main()
