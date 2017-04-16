import os

students = ["hamza", "osama"]

message = print("Press 1 to add a new Student, Press 2 to get Students List, Press 3 to search a Student or Press 4 to exit.\n")

while ("true"):
    num = int(input("Enter Number between 1 to 3:\t"))

    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    if num == 1:
        print("Type quit to exit.")
        while ("true"):
            add_stud = input("Enter Student Name:\t")
            if add_stud.lower() == "quit":
                break
            students.append(add_stud.lower())
    if num == 2:

        print("\n")
        for stud in students:
            print(stud)
        print("\n")

    if num == 3:
        stud_search = input("Enter Student Name to Search:\t")
        if stud_search.lower() in students:
            print("Found", stud_search.lower(), " in the list.")
        else:
            print("No Student name", stud_search.lower(), " in the list. Add it now.")

    if num == 4:
        break
