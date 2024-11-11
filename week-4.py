def read_and_modify_file():
    #  Prompting the user for a filename
    global filename
    while True:
        try:
            # Asking the user for the filename
            filename = input("Enter the filename to read: ")

            # Attempting to open the file for reading
            with open(filename, 'r') as file:
                content = file.read()
            break  # Exiting the loop if the file is read successfully

        except FileNotFoundError:
            print("Error: The specified file does not exist. Please try again.")
            continue  # Prompting again if the file is not found

    # Asking if the user wants to continue with modification
    while True:
        choice = input("All the file contents will be capitalized, do you wish to continue? (Y/N): ").strip()

        # Validating the choice input
        if choice.upper() == 'Y':
            try:
                # Modifying the content
                modified_content = content.upper()

                # Writing the modified content to a new file
                new_filename = f"modified_{filename}"
                with open(new_filename, 'w') as new_file:
                    new_file.write(modified_content)

                print(f"Modified content has been written to '{new_filename}'.")
            except IOError:
                print("Error: The file could not be read or written.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            break

        elif choice.upper() == 'N':
            print("Session cancelled.")
            break

        else:
            print("Please enter a single character 'Y' or 'N'.")


read_and_modify_file()
