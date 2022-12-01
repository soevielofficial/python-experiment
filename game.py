import random

options = ["Rock", "Paper", "Scissor"]

def get_computer_choice(data_options):
    len_options = len(data_options)
    random_data = random.randint(0, len_options-1)
    random_data = data_options[random_data]
    return random_data

def get_user_choice(data_options):
    is_valid_choice = False
    user_choice = " "
    len_options = len(data_options)

    while not is_valid_choice:
        print("Masukan Pilihan: ")
        for i in range(len_options):
            print(f"#.{data_options[i]}")

        user_input = input("Masukan disini: ")
        if user_input is not None and user_input in data_options:
            is_valid_choice = True
            user_choice = user_input

        if not is_valid_choice:
            print("Anda harus memasukan pilihan yang valid!!!")

    return user_choice

def print_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        result = "Imbang!!!"

    elif user_choice == "Rock" and computer_choice == "Scissor" and computer_choice == "Paper" and computer_choice == "Rock" or user_choice == "Scissor" and computer_choice == "Paper":
        result = "You Win!!!"

    else:
        result = "You Lose!!!"

    print(f"Your choice is {user_choice}.  I choose {computer_choice}. {result}")

def main():
    computer = get_computer_choice(options)
    user = get_user_choice(options)
    print_result(user, computer)

if __name__ == '__main__':
    main()