# Here we call parameters
def greeting(first_name, last_name):
    print("Welcome!", f"{first_name} {last_name}")
    return "Boom" # Default: return None

print("Hey!")
# Here we call arguement
greeting(last_name="John", first_name="Dara")
# greeting(first_name="Dara", "John") # Error: Keyword Arguement first
greeting("Dara", last_name="John")
greeting("Dara", "John")

getGreeting = greeting("Dara", "John")
print(getGreeting)