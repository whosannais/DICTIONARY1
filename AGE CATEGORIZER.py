def classify_age(age):
	if age < 0:
		print("Invalid age.")
	elif age <= 12:
		print("You are a Child.")
	elif age <= 19:
		print("You are a Teen.")
	elif age <= 64:
		print("You are an Adult.")
	else:
		print("You are a Senior.")
		
		
#Let's try
classify_age(12)
classify_age(19)
classify_age(64)
classify_age(70)
classify_age(-10)