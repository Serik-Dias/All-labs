import time
import math

num = 25100
delay = 2123 / 1000  # 2123 миллисекунды -> 2.123 секунды

time.sleep(delay)  # Ждём 2.123 секунды
sqrt_value = math.sqrt(num) 
print(f"Square root of {num} after {delay * 1000} milliseconds is {sqrt_value}")