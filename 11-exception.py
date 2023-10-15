try:
    int(input("Give me you age: "))
    print("Damn! Cool!", 100/0)
except ValueError:
    print("Watch your input!")
except Exception as ex:
    print("Catch all exception!", ex)