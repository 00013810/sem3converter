# Task for seminar 3

decimal = int(input('Print number: '))  # we convert our variable into integer as input() always show strings
octal_number = oct(decimal).replace("0o", "")  # we use method replace() to delete 0o from output in 5 line code
print(f"The answer is {octal_number}")
