from functions import process_calculation

print("Hello! This is a simple calculator.")
continue_calculation = "y"

while continue_calculation == "y":
	first_number: str = input("Enter first number: ")
	operator: str = input("+ - * / ")
	print(f"My chosen operator: {operator}")
	operator = operator[0]
	second_number = input("Enter second number: ")

	operation_result = process_calculation(first_number, second_number, operator)

	operation_result = round(int(operation_result), 2)

	result: str = f"{first_number} {operator} {second_number} = {operation_result}"
	with open("greeting.txt", "a") as greeting_file:
		greeting = greeting_file.write(f"{result}\n")
	print(result)
	print("Do you want to calculate something else?")
	continue_calculation = input("y/n ")

print("Bye!")
