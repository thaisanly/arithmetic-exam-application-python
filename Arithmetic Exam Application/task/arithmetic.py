# write your code here
import math
import random

result = 0

total_exam = 5
current_exam = total_exam
correct_answer = 0
levels = {
    "1": "simple operations with numbers 2-9",
    "2": "integral squares of 11-29",
}


def is_integer(s):
    return s.isdigit() or (s.startswith('-') and s[1:].isdigit())


def select_level():
    print("Which level do you want? Enter a number:")
    for _level, des in levels.items():
        print("{level} - {des}".format(level=_level, des=des))
    return input()


selected_level = select_level()

while True:
    if selected_level not in levels.keys():
        selected_level = select_level()
    else:
        break

while current_exam > 0:

    num1 = random.choice(list(range(2, 10)))
    num2 = random.choice(list(range(2, 10)))
    num3 = random.choice(list(range(11, 30)))
    opt = random.choice(["+", "-", "*"])

    if selected_level == '1':
        if opt == '+':
            result = num1 + num2
        elif opt == '-':
            result = num1 - num2
        elif opt == '*':
            result = num1 * num2
        elif opt == '/':
            result = num1 // num2

        print("{num1} {opt} {num2}".format(num1=num1, opt=opt, num2=num2))
    else:
        result = math.pow(num3, 2)
        print("{num3}".format(num3=num3))

    answer = input()

    while True:
        if not is_integer(answer):
            print("Incorrect format.")
            answer = input()
        else:
            break

    answer = int(answer)

    if answer == result:
        print("Right!")
        correct_answer += 1
    else:
        print("Wrong!")

    current_exam -= 1

is_save = input("Your mark is {correct_answer}/{total_exam}. Would you like to save the result? Enter yes or no.".format(
        correct_answer=correct_answer, total_exam=total_exam))

if is_save.lower() in ['y', 'yes']:
    name = input("What is your name?")
    with open("results.txt", "a") as file:
        file.write("{name}: {correct_answer}/{total_exam} in level {level} ({des}).\n".format(
            name=name,
            correct_answer=correct_answer,
            total_exam=total_exam,
            level=selected_level,
            des=levels[selected_level]
        ))
    print('The results are saved in "results.txt"')
