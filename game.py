import functions
import variables

is_valid = False
is_correct = False
returned_fm_random = functions.random_initial_choice()
variables.chosen_number = returned_fm_random[0]
variables.chosen_numbers_list.append(variables.chosen_number)
print("Start")
print(f"Attempt: {variables.count}")
print(f"Give me bulls & cows in: {variables.chosen_number}")
while not is_valid:
    bulls_in_chosen_number = int(input("How many bulls: "))
    try:
        if bulls_in_chosen_number not in range(5):
            raise ValueError
        else:

            cows_in_chosen_number = int(input("How many cows: "))
            if cows_in_chosen_number not in range(5):
                raise ValueError
            else:
                elements = bulls_in_chosen_number + cows_in_chosen_number
                if elements not in range(5):
                    raise ValueError
                else:
                    is_valid = True
                    variables.answer = (bulls_in_chosen_number, cows_in_chosen_number)
                    variables.chosen_number_dict[variables.chosen_number] = bulls_in_chosen_number, cows_in_chosen_number
                    variables.chosen_numbers_list.append(variables.chosen_number)
    except ValueError:
        print("Incorrect input.\n"
              "Bulls in range (1 - 4) and "
              "Cows in range (1 - 4) and the sum of bulls & cows should be less or equal to 4")

while not is_correct:
    print(functions.play())
#2574