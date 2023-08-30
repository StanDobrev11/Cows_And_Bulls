import time
from random import choice

user_number = "1234"
user_number = list(user_number)


def bulls_cows_check(number_to_check):
    print(user_number)
    print(number_to_check)
    bulls = 0
    cows = 0
    for index, digit in enumerate(number_to_check):
        if digit in user_number:
            if number_to_check[index] == user_number[index]:
                bulls += 1
            else:
                cows += 1
    checked_numbers = number_to_check.copy()
    print("Bulls: ", bulls)
    print("Cows: ", cows)
    return checked_numbers, (bulls, cows)


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
    # actual_nums = []
    # nums_not_in_play = []
    all_num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(answers_list) == 2:
        if sum(answers_list[0]) + sum(answers_list[1]) == 4:
            # print("IT IS 4")
            nums_to_play = [num for sublist in guesses_list for num in sublist]
            # print(nums_to_play)
            for num in all_num_list:
                if num not in nums_to_play:
                    nums_not_in_play.append(num)
        elif sum(answers_list[0]) + sum(answers_list[1]) == 3:
            # print("It is 3")
            nums_to_play = [num for sublist in guesses_list for num in sublist]
            # print(nums_to_play)
            for el in nums_to_play:
                all_num_list.remove(el)
            actual_nums = all_num_list.copy()
            # print(actual_nums)

    return actual_nums, nums_not_in_play


def generated_number_list_function(guesses_list, answers_list, work_list):
    # generates all possible numbers as per cows and bulls and returns list of generated numbers
    generated_number_list = []
    for index, number_to_check in enumerate(guesses_list):
        number_to_check = list(number_to_check)
        bulls = answers_list[index][0]
        cows = answers_list[index][1]
        # print(number_to_check)
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
        checked = bulls_cows_check(random_num)
        is_valid = True
        guesses_list.append("".join(checked[0]))
        answers_list.append(checked[1])
        if answers_list[0][0] == 4:
            print("Your number has been guessed!!!", "".join(random_num))

        cows = input()
        # bulls = answers_list[2][0]
        # cows = answers_list[2][1]
        bulls = answers_list[0][0]
        cows = answers_list[0][1]

        # print(random_num)
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
    random_count = 0
    is_guessed = False  # indicates if the number is guessed in order to break the loop
    checked = [""]  # a list with number to be checked for cows and bulls
    guesses_list = []
    answers_list = []
    nums_not_in_play = []
    actual_nums = []
    while not is_guessed:
        while play_count < 2:  # first 2 attempts to pass through all the numbers w/out repetition
            play_count += 1
            print(f"Count: {play_count}")
            num = comp_guess(checked[0])  # returns number generated fm the computer
            print("Cows & bulls in: ", ''.join(num))
            checked = bulls_cows_check(num)  # returns bulls & cows in the generated number
            guesses_list.append("".join(checked[0]))
            answers_list.append(checked[1])
            cows = input()
            # bulls = input()
            if sum(checked[1]) == 0:
                for each in num:
                    nums_not_in_play.append(each)
            elif sum(checked[1]) == 4:
                # actual_nums = []
                for each in num:
                    actual_nums.append(each)
        # if len(actual_nums) == 4:
        #     pass
        # elif len(actual_nums) == 1:
        #     pass

        work_list = total_answer_count(answers_list, guesses_list, actual_nums,
                                       nums_not_in_play)  # returns actual_nums, nums_not_in_play
        generated_list = generated_number_list_function(guesses_list, answers_list, work_list)
        # step 3: random num from the generated_list
        # requirements: - to have all nums in actual_num_list
        # - to lack nums from nums_not_in_play list
        # step 4: comparing bulls & cows
        while not is_guessed:
            num_list = []
            guesses_list.clear()
            answers_list.clear()
            play_count += 1
            print(f"Count: {play_count}")
            random_list = random_generated_list(generated_list, guesses_list, answers_list, work_list)

            #
            # if ['5', '3', '2', '8'] in generated_list:
            #     print("YES", generated_list.count(['5', '3', '2', '8']))
            # generated_list.sort()

            for el in random_list:  # appending num list
                if el in generated_list:
                    num_list.append(el)
            for el in generated_list:
                if el in random_list:
                    num_list.append(el)
                    if el in num_list:
                        num_list.pop()
            generated_list.clear()
            generated_list = num_list.copy()

            # print()
            # print()
            # print(len(generated_list))
            # for i in generated_list:
            #     # print(i, end="")
            #     print("".join(i), end=" ")
            # print()
            # for i in random_list:
            #     # print(i, end="")
            #     print("".join(i), end=" ")
            # print()
            # print(len(random_list))
            # print()
            # num_list.sort()
            # for i in num_list:
            #     print("".join(i), end=" ")
            # print()
            # print(len(num_list))
            # time.sleep(5)

            #
            # for index, answer in enumerate(answers_list):
            #     if sum(answer) == 4:
            #         print("4")
            #         print(index)
            #     elif sum(answer) == 3:
            #         print("3")
            #         print(index)
            #     elif sum(answer) == 2:
            #         print("2")
            #         print(index)
            #     elif sum(answer) == 1:
            #         print("1")
            #         print(index)
            #     else:
            #         print("0")
            #         print(index)

        break


play()
