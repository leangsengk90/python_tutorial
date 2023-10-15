# from modules import my_greeting
# from modules.my_greeting import greeting

import modules.my_greeting
mylib = modules.my_greeting
# from lib.my_greeting import greeting

# Here we call parameters
# def greeting(first_name, last_name):
#     print("Welcome!", f"{first_name} {last_name}")
#     return "Boom" # Default: return None



print("Hey!")
# Here we call arguement
mylib.greeting(last_name="John", first_name="Dara")
# greeting(first_name="Dara", "John") # Error: Keyword Arguement first
mylib.greeting("Dara", last_name="John")
mylib.greeting("Dara", "John")

getGreeting = mylib.greeting("Dara", "John")
print(getGreeting)