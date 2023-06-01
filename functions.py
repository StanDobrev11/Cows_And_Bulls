from random import choice
import variables


# from game import chosen_numbers_list, chosen_number_dict


def random_initial_choice():
    initial_numbers = []
    remaining_numbers = []
    chosen_number = ""
    for i in range(1, 10):
        initial_numbers.append(str(i))

    remaining_numbers = initial_numbers
    for i in range(4):
        number = choice(initial_numbers)
        remaining_numbers.remove(number)
        chosen_number += number

    return chosen_number, remaining_numbers


def play(answer):
    is_valid = False
    is_correct = False
    final_number_list = ["*", "*", "*", "*"]
    returned_fm_random = random_initial_choice()
    chosen_number = returned_fm_random[0]
    variables.chosen_numbers_list.append(chosen_number)
    count = 2
    print(f"Attempt: {count}")
    print(f"Give me bulls & cows in: {chosen_number}")
    while not is_valid:
        bulls_in_chosen_number = int(input("How many bulls: "))

        try:
            if 0 > bulls_in_chosen_number > 4:
                raise ValueError
        except ValueError:
            print("Incorrect input.\n"
                  "Bulls in range(1 - 4)")
        cows_in_chosen_number = int(input("How many cows: "))
        try:
            if 0 > cows_in_chosen_number > 4:
                raise ValueError
        except ValueError:
            print("Incorrect input.\n"
                  "Cows in range (1 - 4)")
        elements = bulls_in_chosen_number + cows_in_chosen_number
        try:
            if 0 > elements > 4:
                raise ValueError
        except ValueError:
            print("Incorrect input.\n"
                  "and Bulls + Cows should be less than 5")
            is_valid = True
            answer = (bulls_in_chosen_number, cows_in_chosen_number)
            chosen_number_dict[chosen_number] = bulls_in_chosen_number, cows_in_chosen_number

    # return answer, chosen_numbers_list, chosen_number_dict
