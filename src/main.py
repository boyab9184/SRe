from export_to_file import export_to_file


def menu():
    print("\nWELCOME to Boyan Benev's codding assignment")

    while True:
        print("\nMAIN MENU:\n")

        user_choice = input(
            "Enter path to one or more plain text files, or a directory. If you enter more than one item separate them with space. Press "
            "0 to exit:\n")
        if user_choice == "0":
            break
        else:
            try:
                print("\nYou can find the output file in:", export_to_file(user_choice))
                break
            except FileNotFoundError:
                print("Wrong file path. Please try again")


if __name__ == "__main__":
    menu()
