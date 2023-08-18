import random

MIN_NUMBER = 1 
MAX_NUMBER = 10
QUESTION_COUNT = 4


def ask_question(min_num, max_num):
    a = random.randint(min_num, max_num)
    b = random.randint(min_num, max_num)
    o = random.randint(0, 1)
    operator_str = "+"
    if o == 1:
        operator_str = "*"
    response_str = input(f"Calculate: {a} {operator_str} {b} = ")
    response_int = int(response_str)
    calculation = a + b
    if o == 1:
        calculation = a * b
    if response_int == calculation:
        return True
    return False

score = 0

for i in range(0, QUESTION_COUNT):
    print(f"Question {i+1} out of {QUESTION_COUNT}")
    if ask_question(MIN_NUMBER, MAX_NUMBER):
        print("Correct answer")
        score += 1
    else:
        print("Incorrect answer")
    print()

print(f"Your score is {score}/{QUESTION_COUNT}")

average = int(QUESTION_COUNT / 2)

if score == QUESTION_COUNT:
    print("Excellent!")
elif score == 0:
    print("Review your math!")
elif score > average:
    print('Not bad!')
else:
    print("Can do better")
