def write_and_append_file():
    data = input("Enter text to write into the file: ")
    with open("output.txt", "w") as file:
        file.write(data + "\n")
    print("Data written to 'output.txt'.")

    more_data = input("Enter additional text to append: ")
    with open("output.txt", "a") as file:
        file.write(more_data + "\n")
    print("Data Successfully Append. ")

    print("\nFinal file content:")
    with open("output.txt", "r") as file:
        print(file.read())