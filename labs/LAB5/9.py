import re

print(re.sub(r'(?<!^)(?=[A-Z])', ' ', 'HelloWorldTest'))