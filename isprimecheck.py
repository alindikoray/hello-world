max_value = eval(input ("display numbers to what maximum value?"))
for value in range(2, max_value +1):
	is_prime = True
	# Try all possible factors from 2 to value - 1
	for trial_factorin range (2, value):
		if value % trial_factor == 0:
			is_prime = False # Found a factor
			break           # No need to continue; it is NOT prime 
	if is_prime:
		print(value, end ' ')
print()
		

