from random import choice

"""
Bulls and Cows is a logic game to guess numbers. The numbers have to be with four digits and the 
digits must be all different. 
The game is played by two players and they take turns to try to guess their opponent's number. 
The answering player responds with the number of matching digits. 
If they are in their right positions, they are "bulls"; if in different positions, they are "cows".

Example:
If the player's number is 7359
And the opponent asks how many matches are there in 7893
The answer is 1 "bull" and 2 "cows".
"""


# user_number = "1234"
# user_number = list(user_number)

def comp_guess(checked_nums):  # to be used only on first and second attempts
    all_num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for element in checked_nums:
        if element in all_num_list:
            all_num_list.remove(element)
    guess = []
    for _ in range(4):
        num = choice(all_num_list)
        guess.append(num)
        all_num_list.remove(num)
    return guess


def total_answer_count(answers_list, guesses_list, actual_nums, nums_not_in_play):
    all_num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(answers_list) == 2:
        if sum(answers_list[0]) + sum(answers_list[1]) == 4:
            nums_to_play = [num for sublist in guesses_list for num in sublist]
            for num in all_num_list:
                if num not in nums_to_play:
                    nums_not_in_play.append(num)
        elif sum(answers_list[0]) + sum(answers_list[1]) == 3:
            nums_to_play = [num for sublist in guesses_list for num in sublist]
            for el in nums_to_play:
                all_num_list.remove(el)
            actual_nums = all_num_list.copy()

    return actual_nums, nums_not_in_play


def generated_number_list_function(guesses_list, answers_list, work_list):
    # generates all possible numbers as per cows and bulls and returns list of generated numbers
    generated_number_list = []
    for index, number_to_check in enumerate(guesses_list):
        number_to_check = list(number_to_check)
        bulls = answers_list[index][0]
        cows = answers_list[index][1]
        for a in range(1, 10):
            for b in range(1, 10):
                for c in range(1, 10):
                    for d in range(1, 10):
                        if a != b and a != c and a != d and b != c and b != d and c != d:
                            bulls_found = 0
                            cows_found = 0
                            number_generated = f"{a}{b}{c}{d}"
                            number_generated = list(number_generated)
                            if work_list == "":
                                pass
                            else:
                                if len(work_list[0]) == 0:
                                    if work_list[1][0] in number_generated:
                                        continue
                                else:
                                    if work_list[0][0] not in number_generated:
                                        continue
                            work_number = number_generated.copy()

                            # checking bulls & cows
                            for ind in range(4):
                                if work_number[ind] == number_to_check[ind]:
                                    bulls_found += 1
                                    work_number[ind] = "*"
                                elif work_number[ind] in number_to_check:
                                    cows_found += 1

                            if bulls_found == bulls and cows_found == cows:
                                if number_generated in generated_number_list:
                                    continue
                                else:
                                    generated_number_list.append(number_generated)
    return generated_number_list


def random_generated_list(generated_list, guesses_list, answers_list, work_list):  # PART 2
    is_valid = False
    while not is_valid:
        random_num = choice(generated_list)
        print("Cows & bulls in: ", ''.join(random_num))
        bulls = int(input("Bulls: "))
        cows = int(input("Cows: "))

        checked = (bulls, cows)  # returns bulls & cows in the generated number
        is_valid = True
        guesses_list.append("".join(random_num))
        answers_list.append(checked)
        if checked[0] == 4:
            print("Your number has been guessed!!!", "".join(random_num))
            break
        random_list = []
        for a in range(1, 10):
            for b in range(1, 10):
                for c in range(1, 10):
                    for d in range(1, 10):
                        if a != b and a != c and a != d and b != c and b != d and c != d:
                            bulls_found = 0
                            cows_found = 0
                            number_generated = f"{a}{b}{c}{d}"
                            number_generated = list(number_generated)
                            if work_list == "":
                                pass
                            else:
                                if len(work_list[0]) == 0:
                                    if work_list[1][0] in number_generated:
                                        continue
                                else:
                                    if work_list[0][0] not in number_generated:
                                        continue
                            work_number = number_generated.copy()

                            # checking bulls & cows
                            for ind in range(4):
                                if work_number[ind] == random_num[ind]:
                                    bulls_found += 1
                                    work_number[ind] = "*"
                                elif work_number[ind] in random_num:
                                    cows_found += 1

                            if bulls_found == bulls and cows_found == cows:
                                if number_generated in random_list:
                                    continue
                                else:
                                    random_list.append(number_generated)
        return random_list


def play():  # main game line
    play_count = 0  # how many attempts are made to guess the number
    is_guessed = False  # indicates if the number is guessed in order to break the loop
    checked_nums = [""]  # a list with number to be checked for cows and bulls
    guesses_list = []
    answers_list = []
    nums_not_in_play = []
    actual_nums = []
    have_all_nums = False
    while not is_guessed:
        while play_count < 2:  # first 2 attempts to pass through all the numbers w/out repetition
            play_count += 1
            print(f"Count: {play_count}")
            num = comp_guess(checked_nums)  # returns number generated fm the computer
            print("Cows & bulls in: ", ''.join(num))
            bulls = int(input("Bulls: "))
            if bulls == 4:
                print("I won!")
                is_guessed = True
                break
            cows = int(input("Cows: "))
            if bulls + cows == 4:
                have_all_nums = True
                for each in num:
                    actual_nums.append(each)
                # break
            elif bulls + cows == 0:
                for each in num:
                    nums_not_in_play.append(each)
            checked = (bulls, cows)  # returns bulls & cows in the generated number
            checked_nums.clear()
            checked_nums = num.copy()
            guesses_list.append("".join(checked_nums))
            answers_list.append(checked)

        work_list = total_answer_count(answers_list, guesses_list, actual_nums,
                                       nums_not_in_play)  # returns actual_nums, nums_not_in_play
        generated_list = generated_number_list_function(guesses_list, answers_list, work_list)
        while not is_guessed:
            if len(actual_nums) == 4:
                pass

            num_list = []
            guesses_list.clear()
            answers_list.clear()
            play_count += 1
            print(f"Count: {play_count}")
            random_list = random_generated_list(generated_list, guesses_list, answers_list, work_list)
            if answers_list[-1][0] == 4:
                break
            for el in random_list:  # appending num list
                if el in generated_list:
                    num_list.append(el)
            for el in generated_list:
                if el in random_list:
                    num_list.append(el)
                    if el in num_list:
                        num_list.pop()
            generated_list.clear()
            generated_list = num_list

        break


play()
# 2456

# TODO fix to break when 4 bulls are guessed
# TODO add comments to explain functions
