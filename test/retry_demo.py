def unreliable_operation():
	print("Trying Operation..")

	raise ConnectionError ("Temporary Network failure")

def run_with_retry(max_attempts=3):
	for attempt in range(1, max_attempts + 1):

		try:
			result= unreliable_operation()
			return result

		except ConnectionError as error:
			print(f"Attempt {attempt} failed: {error}")
	return "Operation failed after all retries"

result = run_with_retry()
print(result)

