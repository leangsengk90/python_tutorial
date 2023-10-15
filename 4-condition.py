is_adult = 0

if is_adult != 18:
    print("You are teenager")
elif is_adult < 18 and is_adult > 0 or not is_adult == 0:
    print("You are not old enough")
elif is_adult >= 45 and is_adult <= 65:
    print("You are mature")
else:
    print("You are old")