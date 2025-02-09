from datetime import datetime

current_time = datetime.now()

clean_time = current_time.replace(microsecond=0)

print("Original Datetime:", current_time)
print("Without Microseconds:", clean_time)