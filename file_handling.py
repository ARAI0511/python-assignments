def read_file():
    try:
        with open("sample.txt","r") as file:
            print("file content:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file ;'sample.txt' does not exist.")

read_file()