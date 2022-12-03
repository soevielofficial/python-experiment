# a simple CRUD (Create, Read, Update, Delete) program for processing student name data.

student = []

def menu():
    print("------- MENU -------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")

active = False
def main():
    active = True
    while active:
        menu()
        print("Select a menu by entering the menu number.")
        selected = int(input())
        if(selected == 1):
            show_data_student()
        elif(selected == 2):
            insert_data_student()
        elif(selected == 3):
            edit_data_student()
        elif(selected == 4):
            delete_data_student()
        elif(selected == 5):
            active = False
        else:
            print("Enter the correct data!!!")
        print()

def show_data_student():
    no = 1
    print("Student List: ")
    for item in student:
        print(f'{no}. {item}')
        no +=1

def insert_data_student():
    student_len = len(student)
    student_input = input("Enter student name: ")
    student.insert(student_len, student_input)
    show_data_student()

def edit_data_student():
    no = 1
    print("Student List: ")
    for item in student:
        print(f'[{no}]. {item}')
        no +=1

    edit_selected = int(input("Select the student serial number, to edit the student name."))
    student[edit_selected-1] = input(f"Edit name'{student[edit_selected-1]}' become: ")
    show_data_student()

def delete_data_student():
    print("Student List: ")
    no = 1
    for item in student:
        print(f'[{no}]. {item}')
        no +=1

    del_selected = int(input("Select the serial number of students, to delete student names: "))
    student.pop(del_selected-1)
    print()
    show_data_student

main()