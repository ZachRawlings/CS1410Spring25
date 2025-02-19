import test_age

def cat_by_age(age):
    if 0<= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    elif 65 < age <= 150:
        return "Golden age"
    else:
        return f"Invalid age:{age}"
    
    if __name__ == "__main__":
        unitest.main()
        print(cat_by_age(0))
        print(cat_by_age(9))