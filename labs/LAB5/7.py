import re
def snake_to_camel(s):
    return ''.join(word.capitalize() for word in s.split('_'))
print(snake_to_camel('hello_world_test'))