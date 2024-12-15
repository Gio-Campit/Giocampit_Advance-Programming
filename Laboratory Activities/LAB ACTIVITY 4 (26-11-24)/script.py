from Capybara import Capybara

capybara1 = Capybara("Gio", "M", 5)
capybara2 = Capybara("April", "F", 3)
capybara3 = Capybara("Tope", "M", 7)

capybaras = [capybara1, capybara2, capybara3]

print("Enter the test case number: ")
test_case = int(input())

if 1 <= test_case <= 3:
    selected_capybara = capybaras[test_case - 1]
    print(f"Test case 1: {test_case}  Name: {selected_capybara.name}, Gender: {selected_capybara.gender}, Age: {selected_capybara.age}")
else:
    print("Invalid selection! Please select a number between 1 and 3.")
