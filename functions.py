def plus_operation(number_1, number_2):
	return int(number_1) + int(number_2)


def minus_operation(number_1, number_2):
	return int(number_1) - int(number_2)


def multiply_operation(number_1, number_2):
	return int(number_1) * int(number_2)


def division_operation(number_1, number_2):
	return float(number_1) / float(number_2)


def process_calculation(number_1, number_2, operator):
	if operator == "+":
		operation_result = plus_operation(number_1, number_2)
	elif operator == "-":
		operation_result = minus_operation(number_1, number_2)
	elif operator == "*":
		operation_result = multiply_operation(number_1, number_2)
	elif operator == "/":
		operation_result = division_operation(number_1, number_2)
	else:
		exit("Wrong operator. Exiting...")
	return operation_result
