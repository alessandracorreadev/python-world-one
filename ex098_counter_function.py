from time import sleep

def counter(start, end, step):
    print(f"Counting from {start} to {end} with a step of {step}.")
    # testing if this is a countdown
    if start > end:
        # checking if the user entered a positive step for the countdown
        if step > 0:
            # converting the step to negative for the countdown
            step *= -1
        # subtracting one from the end value to include the user's input
        end -= 1
    else:
        # adding one to the end value to include the user's input
        end += 1
    for count in range(start, end, step):
        print(count, end=' ')
        sleep(0.5)
    print("End!")
    print('-=' * 30)

print('-='*30)
counter(1, 10, 1)
counter(10, 0, 2)

print("Now it's your turn to customize the counting: ")
user_start = int(input("Start: "))
user_end = int(input("End: "))
user_step = int(input("Step: "))

counter(user_start, user_end, user_step)
