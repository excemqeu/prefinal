import os

def display():
    print("1 - Create File")
    print("2 - Read File")
    print("3 - Add Note")
    print("4 - Delete File")
    print("5 - Exit")

def create_file():
    userwrite = input("Write a note...: ")
    try:
        with open("notes.txt", "x") as file:
            file.write(userwrite + "\n")
            print("File created successfully.")
    except FileExistsError:
        print("File already exists!")

def read_file():
    try:
         with open ("notes.txt", "r") as f:
            print("======================File contents======================")
            print(f.read())
            print("=========================================================")
    except FileNotFoundError:
            print("File is not found!")

def add_note():
    if os.path.exists("notes.txt"):
        note = input("Add note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
            print("Note added successfully.")
    else:
        print("File does not exist.")

def remove_file():
    try:
        os.remove("notes.txt")
        print("File has been deleted successfully.")
    except FileNotFoundError:
        print("File is not found.")

def main():
    while True:
        display()
        try:
            choice = int(input("Enter your choice (1-5): "))
        except:
            print("Please enter a valid number!")
            return(main())

        if choice == 1:
            create_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            add_note()
        elif choice == 4:
            remove_file()
        elif choice == 5:
            exit()

if __name__ == "__main__":
    main()
    
