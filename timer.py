# Create a Timer with the Time module
import time

# run = input("Start? > ")
run = "yes"

seconds = 0

if run == "yes":
    while seconds < 5:
        time.sleep(1)
        seconds += 1
        print(">", seconds)
