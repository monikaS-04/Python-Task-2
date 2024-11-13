from datetime import datetime

# Get the current date and time
current_time = datetime.now()

# Display the components of the current date and time
print(f"Year: {current_time.year}")
print(f"Month: {current_time.month}")
print(f"Day: {current_time.day}")
print(f"Hour: {current_time.hour}")
print(f"Minute: {current_time.minute}")
print(f"Second: {current_time.second}")
print(f"Microsecond: {current_time.microsecond}")
print(f"Full Date and Time: {current_time}")
