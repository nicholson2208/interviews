import numpy as np
import time


def make_question():
    q_type = np.random.randint(0, 4, 1)[0]
    two_nums = np.random.randint(1, 100, 2)

    if q_type == 0:  # addition
        reply = str(two_nums[0]) + " + " + str(two_nums[1])
        answer = two_nums[0] + two_nums[1]

    elif q_type == 1:  # subtraction
        reply = str(two_nums[0]) + " - " + str(two_nums[1])
        answer = two_nums[0] - two_nums[1]
    elif q_type == 2:  # multiplication
        reply = str(two_nums[0]) + " * " + str(two_nums[1])
        answer = two_nums[0] * two_nums[1]
    else:  # division
        product = two_nums[0] * two_nums[1]
        reply = str(product) + " / " + str(two_nums[0])
        answer = two_nums[1]

    return reply+"\t", str(answer)


def main():
    # type: () -> object
    duration = "-1"
    score = 0
    while int(duration) < 0:
        duration = input("How long do you want to play for? (seconds): \t")

    count_down = 5
    while count_down > 0:
        print "game will start in ", count_down
        time.sleep(1)
        count_down -= 1
    print "Begin!"

    start_time = time.time()

    user_guess = None
    reply, correct_answer = make_question()

    while time.time() < start_time + duration and str(user_guess) != str(correct_answer):
        user_guess = input(reply)

        if str(user_guess) == str(correct_answer):
            print "Correct!"
            score += 1
            reply, correct_answer = make_question()

    print "Time's up! Your score is ", score

if __name__ == "__main__":
    main()