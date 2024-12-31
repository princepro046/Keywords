
input_string = input("Enter a string: ")


found = False


for char in input_string:

    if char.upper() == 'A':
        print("The alphabet 'A' is present in the string.")
        found = True
        break 


if not found:
    print("The alphabet 'A' is not present in the string.")
