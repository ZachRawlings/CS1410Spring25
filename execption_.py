while True:
    try:
        a = int(input("Enter a number: "))
    except ValueError:
        print("An error occurred.")
    else:
        break