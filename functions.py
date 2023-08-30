from random import choice
import variables


def random_initial_choice():
    # initial_numbers = []
    # remaining_numbers = []
    # chosen_number = ""
    # for i in range(1, 10):
    #     initial_numbers.append(str(i))

    variables.remaining_numbers = list(variables.available_numbers)
    variables.chosen_number = ""
    for i in range(4):
        number = choice(variables.remaining_numbers)
        variables.remaining_numbers.remove(number)
        variables.chosen_number += number

    return variables.chosen_number, variables.remaining_numbers


def play():
    print("Play")
    is_correct = False
    final_number_list = ["*", "*", "*", "*"]
    returned_fm_random = random_initial_choice()
    variables.chosen_number = returned_fm_random[0]
    variables.chosen_numbers_list.append(variables.chosen_number)
    variables.count += 1
    answer = print_input(variables.count)

    return functions_dict[answer]()


def print_input(count):
    is_valid = False
    print(f"Attempt: {count}")
    print(f"Give me bulls & cows in: {variables.chosen_number}")
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
        variables.answer = (bulls_in_chosen_number, cows_in_chosen_number)
        variables.chosen_number_dict[variables.chosen_number] = bulls_in_chosen_number, cows_in_chosen_number
    return variables.answer


def func_1():
    print("Function 1 - (0, 0)")


def func_2():
    print("Function 2 - (0, 1)")


def func_3():
    print("Function 3 - (0, 2)")


def func_4():
    print("Function 4 - (0, 3)")


def func_5():
    print("Function 5 - (0, 4)")
    for el in variables.chosen_number:
        variables.element_list.append(el)
    variables.element_list.reverse()
    variables.chosen_number = "".join(variables.element_list)
    variables.count += 1
    print_input(variables.count)

    return variables.chosen_number, variables.answer


def func_6():
    pass


def func_7():
    pass


def func_8():
    pass


def func_9():
    pass


def func_10():
    pass


def func_11():
    pass


def func_12():
    pass


def func_13():
    pass


def func_14():
    pass


functions_dict = {(0, 0): func_1,
                  (0, 1): func_2,
                  (0, 2): func_3,
                  (0, 3): func_4,
                  (0, 4): func_5,
                  (1, 0): func_6,
                  (1, 1): func_7,
                  (1, 2): func_8,
                  (1, 3): func_9,
                  (2, 0): func_10,
                  (2, 1): func_11,
                  (2, 2): func_12,
                  (3, 0): func_13,
                  (3, 1): func_14,
                  (4, 0): func_14}
