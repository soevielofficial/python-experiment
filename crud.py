mahasiswa = []

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
    menu()
    while active:
        print("Select a menu by entering the menu number.")
        selected = int(input())
        if(selected == 1):
            show_data_mahasiswa()
        elif(selected == 2):
            insert_data_mahasiswa()
        elif(selected == 3):
            edit_data_mahasiswa()
        elif(selected == 4):
            delete_data_mahasiswa()
        elif(selected == 5):
            active = False
        else:
            print("Enter the correct data!!!")
        print()

def show_data_mahasiswa():
    no = 1
    print("Student List: ")
    for item in mahasiswa:
        print(f'{no}. {item}')
        no +=1

def insert_data_mahasiswa():
    mahasiswa_len = len(mahasiswa)
    mahasiswa_input = input("Enter student name: ")
    mahasiswa.insert(mahasiswa_len, mahasiswa_input)
    show_data_mahasiswa()

def edit_data_mahasiswa():
    no = 1
    print("Student List: ")
    for item in mahasiswa:
        print(f'[{no}]. {item}')
        no +=1

    edit_selected = int(input("Select the student serial number, to edit the student name."))
    mahasiswa[edit_selected-1] = input(f"Edit name'{mahasiswa[edit_selected-1]}' become: ")
    show_data_mahasiswa()

def delete_data_mahasiswa():
    print("Student List: ")
    no = 1
    for item in mahasiswa:
        print(f'[{no}]. {item}')
        no +=1

    del_selected = int(input("Select the serial number of students, to delete student names: "))
    mahasiswa.pop(del_selected-1)
    print()
    show_data_mahasiswa

main()