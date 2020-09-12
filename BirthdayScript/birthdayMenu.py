import time
import playsound
import pyinputplus as pyip


def menu():
    print("**********************")
    print("1. Wishes \n2. Song \n3. Exit")
    print("**********************")

    answer = pyip.inputNum("Please select menu item's number.")

    if answer == 1:
        print('The message will take a bit to display in full.')
        wishes()
    elif answer == 2:
        print("You will get a song.")
        song()
    elif answer == 3:
        exit()
    else:
        print("What?")
        menu()


def wishes():
    print("HAPPY BIRTHDAY")
    time.sleep(2)
    print("You are now one year older.")
    time.sleep(2)
    print("I hope you have a good day.")
    time.sleep(2)
    print("Love you Mom")
    time.sleep(2)
    print("---Tim")
    time.sleep(2)
    print("\n\n\n\n\n")
    menu()


def song():
    playsound.playsound("happyBday.mp3")
    print("\n\n\n\n\n")
    menu()

print("HAPPY BIRTHDAY")

menu()
