import time
import sys


# Checks for the right input.
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Invalid input. Enter a positive number.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


h = get_positive_int("Enter hours: ")
m = get_positive_int("Enter minutes: ")
s = get_positive_int("Enter seconds: ")

# (1) and (2) rearrange the timer.
while s > 60:  # (1)
    s -= 60
    m += 1
    if s < 60:
        break

while m > 60:  # (2)
    m -= 60
    h += 1
    if m < 60:
        break

while True:
    for i in range(s, -1, -1):
        time.sleep(1)
        t = f"{h} : {m} : {i}"
        sys.stdout.write(f"\r{t.ljust(20)}")
        sys.stdout.flush()
        if h == 0 and m == 0 and i == 0:
            sys.stdout.write(f"\r{'0 : 0 : 0'.ljust(20)}\n")
            break
    if h == 0 and m == 0:
        break
    s = 59
    m -= 1
    if m < 0:
        h -= 1
        m = 59

