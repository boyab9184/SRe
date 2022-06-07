import export_to_file as ef


print("\nWELCOME to Boyan Benev's codding assignment")

while True:  
    print("\nMAIN MENU:\n")  

    user_choice = input("Enter the file path you want to be analysed or press 9 to exit:\n")

    if user_choice == "9":
        break 
    else:
        #needs try catch block
        try:
            print("\nYou can find the output file in:", ef.export_to_file(user_choice))
            break
        except FileNotFoundError:
            print("Wrong file or file path. Please try again")
