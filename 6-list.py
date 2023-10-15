fruits = ["apple", "banana", "jerry"]

for fruit in fruits:
    print(fruit)
print("================")
fruits[1] = "BANANA"
print(fruits[0:2]) # Slice from 0 index to 1 index 
print(fruits[-1]) # last index

fruits.append(2)
fruits.pop()
fruits.remove("BANANA")
fruits.insert(1, 100)
fruits.append("apple")

print(fruits)
print(fruits.index(100))
print(fruits.count("apple"))

# fruits.sort()
# fruits.reverse()
print(fruits)
temp = []
for i in fruits:
    print("Found: ", i)
    if i not in temp:
        temp.append(i)
        print("Add ", i, "in temp")

print(temp)