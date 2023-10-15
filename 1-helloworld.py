str = "hello, world!"
print('''This's a "BOOK"''')
print("""
      This's a "BOOK".
      The book is on the table.
""")
print(str[:])
print(str[0])
print(str[:3])
print(str[3:])
print(str[5:-1])
print(str[5:-2])
print(len(str))

print(f"{str}".upper())

print(str.find("o"))
print(str.replace('o', '#'))
print("o" in str)
print(str.title()) # Convert each word to Capital Case

name = input("What is your name? ")
print("=" * 20)
print("Hi, " + name)
print("=" * 20)
