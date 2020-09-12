# Hello World
#
# message = "Hello Python World!"
# print(message)
#
# message = "Mic is too sensitive"
# print(message)
#
# message = "Hi, how are ya?"
# print(message)


# Strings
#
# myString = "this is a string."
# myString = 'This is also a string.'
#
# quote = "Linus Torvalds once said, 'Any program is only as good as it is useful.'"
# print(quote)
#
# firstName = 'tim'
# print(firstName)
# print(firstName.title())
# print(firstName.upper())
#
# firstName = "Tim"
# lastName = "Krow"
#
# fullName = firstName + " " + lastName
# print(fullName.title())
#
# print("Hello Everybody")
# print("\tHello Everybody")
# print("Hello \tEverybody")
#
# name = ' tim '
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())
#
# quoteName = "Constantine the Great"
# quote = " once said, 'How pleasing to the wise and intelligent portion of mankind is the concord which exists among you!'"
# print(quoteName + quote)
# print(quoteName.title() + quote)
# print(quoteName.upper() + quote)
# print(quoteName.lower() + quote)


# Numbers
#
# print(3+2)
# print(3-2)
# print(3*2)
# print(3/2)
# print(3**2)
#
# standard_order = 2+3*4
# print(standard_order)
#
# print(0.1+0.1)
# print(0.1+0.2)


# This program says hello and asks for a name
#
# print("Hello")
# print("What is your name?")
# myName = input()
# print('It is good to meet you, ' + myName)
# print('The length of your name is:')
# print(len(myName))


# List
#
# students = ['patrick', 'Alan', 'Ethan']
# for student in students:
#     print("Hello, " + student.title() + "!")
#
# dogs = ['border collie', 'German Shepherd', 'labrador']
# dog = dogs[0]
# print(dog.title())
#
# cats = ['patches', 'peanut', 'angel', 'gizmo', 'Pumpkin', 'spot']
# i = 0
# for cat in cats:
#     print("One of my cats is named " + cat.title() + ".")
#
# dogs = ['border collie', 'German Shepherd', 'labrador']
# for dog in dogs:
#     print("I like " + dog + "s.")
#
# dogs = ['border collie', 'German Shepherd', 'labrador']
# print("Results for the dog show are as follows:")
# for index, dog in enumerate(dogs):
#     place = str(index)
#     print("Place: " + place + " Dog: " + dog.title())
#
# dogs = ['border collie', 'German Shepherd', 'labrador']
# dogs[0] = "Poodle"
# print(dogs)
#
# dogs = ['border collie', 'German Shepherd', 'labrador']
# print(dogs.index("labrador"))
#
# dogs = ['border collie', 'German Shepherd', 'labrador']
# print('labrador' in dogs)
# print('poodle' in dogs)
#
# dogs = ['border collie', 'German Shepherd', 'labrador']
# dogs.append('poodle')
# for dog in dogs:
#     print(dog.title() + "s are neato")
#
# # Create an empty list to hold users
# userNames = []
#
# # add some users
# usernames.append('Alan')
# usernames.append('Tim')
# usernames.append('Garrett')
#
# # Greeting
# for username in usernames:
#     print("Welcome, " + username.title() + "!")
#
# # recognize first user
# print("\nThank you for being my first user, " + usernames[0].title() + ".")
# print("And welcome to our newest user, " + usernames[-1].title + ".")
#
# students = ['bob', 'jim', 'pat', 'alan']
# students.sort()
# print("Our students are in alphabetical order.")
# for student in students:
#     print(student.title())
#
# students.sort(reverse=True)
# for student in students:
#     print(student.title())
#
# students = ['bob', 'jim', 'pat', 'alan']
# print("Alphabetical order:")
# for student in sorted(students):
#     print(student)
#
# print("Reverse Alphabetical Order:")
# for student in sorted(students, reverse=True):
#     print(student)
#
# print("Original order")
# for student in students:
#     print(student)
#
# usernames = ['pat', 'bob', 'aaron']
# userCount = len(usernames)
# print(userCount)
#
# usernames = []
# usernames.append('bob')
# userCount = len(usernames)
# print("We have " + str(userCount) + " user(s).")
# usernames.append('pat')
# usernames.append('aaron')
# userCount = len(usernames)
# print("We have " + str(userCount) + " user(s).")
#
# dogs = ['poodle', 'german shepherd', 'pug']
# # delete the first item in the list
# del dogs[0]
# print(dogs)
#
# dogs = ['poodle', 'german shepherd', 'pug']
# lastDog = dogs.pop()
# print(lastDog)
# print(dogs)
#
# usernames = ['pat', 'bob', 'aaron', 'jeff', 'tim']
# # Grab the fist three users in the list
# firstBatch = usernames[0:3]
# for user in firstBatch:
# print(user.title())
#
# usernames = ['bob', 'pat', 'aaron', ' tim']
# # Grab from the middle of the list
# middleBatch = usernames[1:3]
# for user in middleBatch:
#     print(user.title())
#
# usernames = ['bob', 'pat', 'aaron', 'tim']
# endBatch = usernames[2:]
# for user in endBatch:
#     print(user.title())
#
# usernames = ['bob', 'pat', 'aaron', 'tim', 'jim']
# # make a copy of the list
# copiedUsernames = usernames[:]
# print("the full copied list: \n\t", copiedUsernames)
#
# del copiedUsernames[0]
# del copiedUsernames[0]
# print("Two users removed from copied list: \n\t", copiedUsernames)
#
# print("The original list: \n\t ", usernames)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(number)


# Functions
#
# # define a function
# def functionName(arg1, arg2):
#     # do stuff
#     # do stuff with args
# # use functionName to call thse function
# functionName(val1, val2)
#
# print("you are awesome, bob!")
# print("COVID-19 is terrible!")
#
# def thankYou(name):
#     print("\nYou are awesome, %s!" % name)
#     print("Covid-19 is terrible!")
#
# thankYou(input("What is your name?"))
#
# students = ['pat', 'bob', 'aaron', 'blake']
# def sort(li, rev):
#     if rev:
#         li.sort()
#         print("The list is in alphabetical order")
#         for item in li:
#             print(item.title())
#     else:
#         li.sort(reverse=True)
#         print("The list is in reverse order.")
#         for item in li:
#             print(item.title())
#
# sort(students, True)
# sort(students, False)
#
# def getNumberWord(number):
#     if number == 1:
#         return 'one'
#     elif number == 2:
#         return 'two'
#     elif number == 3:
#         return 'three'
#     else:
#         return "I'm sorry, I don't know that number"
#
# for currentNumber in range(0, 4):
#     numberWord = getNumberWord(currentNumber)
#     print(currentNumber, numberWord)
#
# students = ['pat', 'tim', 'joe', 'bob']
# favoriteStudent = 'bob'
# for student in students:
#     if student == favoriteStudent:
#         print("%s is my favorite student" % student.title())
#     else:
#         print("I like %s." % student)
#
# # player power level starts at 5
# power = 5
# while power > 0:
#     print("You are still playing because your power is %d." % power)
#     power -= 1
# print("Oh no! Your power dropped to 0, game over!")
#
# # make a variable called strength, and set its value to 5
# # print a message reporting the players strength
# # set up a while loop that runs until player strength increases to 10
# # print message on current strength
# # statement to increase strength
# # print message that the player has gotten too strong, and moved up level
# strength = 5
# while strength < 10:
#     print("Your current strength is %d." % strength)
#     strength += 1
# print("Your strength has increased to 10 and you have moved to the next level")
#
# names = ['pat', 'bob', 'aaron']
# newName = input("Please tell me your name")
# names.append(newName)
# print(names)
#
# names = []
# newName = ''
# while newName != 'quit':
#     newName = input("Please tell me someone's name or enter 'quit': ")
#     if newName != 'quit':
#         names.append(newName)
# print(names)
#
# def masterBlaster():
#     print("Taking on the master blaster")
#
# def pig():
#     print("Grab a pig")
#
# def tinaTurner():
#     print("We don't need another hero")
#
# print("Welcome to the Thunderdome. What would you like to do? ")
# choice = ''
# while choice != 'q':
#     print("[1] Enter 1 to fight")
#     print("[2] Enter 2 to make methane")
#     print("[3] Enter 3 to sing with Tina Turner")
#     print("[q] Enter q to quit")
#
#     choice = input("What would you like to do?")
#
#     if choice == '1':
#         masterBlaster()
#     elif choice == '2':
#         pig()
#     elif choice == '3':
#         tinaTurner()
#     elif choice ==  'q':
#         print("Be gone from the Thunderdome")
#     else:
#         print("You need to choose, please try again")
# print("Goodbye")
#
# currentNumber = 1
# while currentNumber <= 5:
#     print(currentNumber)
#     currentNumber += 1#


# Console Apps
#
# import os
#
# print("Make computers do stuff")
#
# os.system('cls')
#
# print("\t****************************************")
# print("\t**** Welcome to Computers doing stuff! ****")
# print("\t****************************************")
#
# for x in range (0, 51):
#     print("\n%d Lines of things happening" % x)
#
# from time import sleep
#
# print("I'm going to sleep now")
# sleep(3)
# print("I woke up!")
#
# from time import sleep
# import os
#
# def displayTitleBar():
#     os.system('cls')
#
# print("\t****************************************")
# print("\t**** Welcome to Computers doing stuff! ****")
# print("\t****************************************")
#
# names = ['pat', 'tim', 'jim', 'aaron', 'bob']
# for name in names:
#     displayTitleBar()
#
#     print("\n")
#     for x in range(0, 5):
#         print(name.title())
#     sleep(1)
#
# from time import sleep
# import os
#
# def displayTitleBar():
#     os.system('cls')
#
# print("\t****************************************")
# print("\t**** Welcome to Computers doing stuff! ****")
# print("\t****************************************")
#
# def getUserChoice():
#     print("\n[1] List of friends")
#     print("[2] Tell me a new person")
#     print("[q] Quit")
#
#     return input("What would you like to do?")
#
# def showNames():
#     print("\nHere are the people I know \n")
#     for name in names:
#         print(name.title())
#
# def getNewName():
#     newName = input("\nTell me a new name")
#     if newName in names:
#         print("\n%s is an  old friend!" % newName.title())
#     else:
#         names.append(newName)
#     print("\nI'm happy to know %s\n" % newName.title())
# ### Main Program ###
#
# names = []
# choice = ''
# displayTitleBar()
# while choice != 'q':
#     choice = getUserChoice()
#
#     #respond to choice
#     displayTitleBar()
#     if choice == '1':
#         showNames()
#     elif choice == '2':
#         getNewName()
#     elif choice == 'q':
#         print("\nThanks for stopping by")
#     else:
#         print("\nI don't understand that choice.\n")
#
# from random_words import RandomWords
# rw = RandomWords()
# word = rw.random_word()
# print(word)
#
# word = rw.random_word('y')
# print(word)
#
# words = rw.random_words(count=10)
# print(words)
#
# words = rw.random_words(letter='r', count=5)
# print(words)
#
# words = rw.random_words(letter=None, count=2)
# print(words)


# Pickling
#
# import pickle
#
# try:
#     fileObject = open("cars.pydata", 'rb')
#     cars = pickle.load(fileObject)
#     fileObject.close()
# except:
#     cars = []
#
# if len(cars) > 0:
#     print("I know the following cars")
#     for car in cars:
#         print(car)
#
# newCar = ''
# while newCar != 'quit':
#     print("\nPlease tell me a new car to remember.")
#     newCar = input("Enter 'quit' to quit: ")
#     if newCar != 'quit':
#         cars.append(newCar)
#
# try:
#     fileObject = open('cars.pydata', 'wb')
#     pickle.dump(cars, fileObject)
#     fileObject.close()
#     print("\nI will remember the following cars: ")
#     for car in cars:
#         print(car)
# except Exception as e:
#     print(e)
#     print("\nI can't figure out how to store the car")


# Classes
#
from math import sqrt
from random import randint

class Rocket():
    # simulates a rocket ship for a game
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # def moveUp(self):
    #     # increment the y-position of the rocket
    #     self.y += 1

    def moveRocket(self, xIncrement=0, yIncrement=0):
        self.x += xIncrement
        self.y += yIncrement

    def getDistance(self, otherRocket):
        distance = sqrt((self.x-otherRocket.x)**2+(self.y-otherRocket.y)**2)
        return distance

class Shuttle(Rocket):
    def __init__(self, x = 0, y = 0, flightsCompleted = 0, capacity = 0, supplies = 0):
        super().__init__(x,y)
        self.flightsCompleted = flightsCompleted
        self.troopCount = capacity
        self.supplies = supplies

    def dropSupplies(self):
        print("A shuttle drops off %d reinforcements and %d units of supplies." % (self.troopCount, self.supplies))

transport = Shuttle(0, 0, 1, 58, 50)
transport.dropSupplies()
#
# shuttles = []
# for x in range(0, 3):
#     x = randint(0, 100)
#     y = randint(1, 100)
#     flightsCompleted = randint(1, 10)
#
#     shuttles.append(Shuttle(x, y, flightsCompleted))
#
# rockets = []
# for x in range(0, 3):
#     x = randint(0, 100)
#     y = randint(1, 100)
#     rockets.append(Rocket(x, y))
#
# for index, shuttle in enumerate(shuttles):
#     print("Shuttle %d has completed %d flights" % (index, flightsCompleted))
#
# print("\n")
# firstShuttle = shuttles[0]
# for index, shuttle in enumerate(shuttles):
#     distance = firstShuttle.getDistance(shuttle)
#     print("The first shuttle is %f units away from shuttle %d." % (distance, index))
#
# print("\n")
# for index, rocket in enumerate(rockets):
#     distance = firstShuttle.getDistance(rocket)
#     print("The first shuttle is %f units away from rocket %d" % (distance, index))
#
# Shuttle = Shuttle(10, 0, 3)
# print(Shuttle)

# rocket0 = Rocket()
# rocket1 = Rocket(10, 5)
#
# distance = rocket0.getDistance(rocket1)
# print("The rockets are %f units apart." % distance)
#
# rockets = [Rocket() for x in range(0,3)]
#
# rockets[0].moveRocket()
# rockets[1].moveRocket(10, 10)
# rockets[2].moveRocket(-10, 0)
#
# for index, rocket in enumerate(rockets):
#     print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
#
# # rockets = []
# rockets.append(Rocket())
# rockets.append(Rocket(0, 10))
# rockets.append(Rocket(100, 0))
#
# for index, rocket in enumerate(rockets):
#     print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))
#
# Create a rocket object
# my_rocket = Rocket()
#
# print("Rocket altitude:", my_rocket.y)
# my_rocket.move_up()
# print("Rocket altitude:", my_rocket.y)
# my_rocket.move_up()
# print("Rocket altitude:", my_rocket.y)
#
# my_rockets = []
# for x in range(0, 5):
#     new_rocket = Rocket()
#     my_rockets.append(new_rocket)
#
# for rocket in my_rockets:
#     print(rocket)
