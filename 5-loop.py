import time

i = 1
# while True:
while i <= 3:
    print(i)
    i += 1
    time.sleep(1)
    if (i == 2):
        print("This is your lucky number")
        break
        # continue
else:
    print("The End") 

for item in ["apple", "banana", "jerry"]:
    print(item)

for item in range(10):
    print(item)