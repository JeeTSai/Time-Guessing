import time
import random


def game():
    print("Let's Play Waiting Game...!!")
    target = random.randint(2, 5)
    print(f"Guess the correct time... Your time is {target}")

    input("___Enter to start the timer___\n")
    start = time.perf_counter()

    input(f"Press Enter after {target} seconds :)")
    elapse = time.perf_counter() - start

    print(f"Elapsed Time {elapse}")

    if elapse == target:
        print("What really...!! Perfect Timing wowww :)")
    elif elapse < target:
        print(f"Your guess: {target-elapse} seconds...\nToo fast :(")
    else:
        print(f"Your guess: {elapse - target} seconds...\nToo slow :(")


if __name__ == "__main__":
    game()
