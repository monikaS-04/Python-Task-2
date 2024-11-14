
import calendar
import time

# Display the calendar for August 2022
print(calendar.month(2022, 8))

# Display current time in seconds since the epoch
print("Current time in seconds:", time.time())

# Display the local time in a simple string format
print("Local time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# Convert a string to a time object
time_string = "2024-11-14 12:30:00"
print("Time object from string:", time.strptime(time_string, "%Y-%m-%d %H:%M:%S"))
