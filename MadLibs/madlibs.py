import pyinputplus as pyip

# opens and closes a selected file after making contents a string
lib = pyip.inputInt("Please select an option from the list\n1.Bar\n2.Cookie\n3.Nuts\n", min=1, max=3)
if lib == 1:
    lib = open('bar.txt')
elif lib == 2:
    lib = open('cookie.txt')
elif lib == 3:
    lib = open('nuts.txt')

libText = lib.read()
lib.close()
# splits string into a list and counts list length
libList = libText.split()
libLen = len(libList)

i = 0
# checks for any NOUN, ADJECTIVE, ADVERB, VERB, and periods(.)
while i < libLen:
    word = libList[i]
    if libList[i] == "NOUN":
        word = pyip.inputStr("Please input a(n) %s:" % libList[i])
    if libList[i] == "ADJECTIVE":
        word = pyip.inputStr("Please input a(n) %s:" % libList[i])
    if libList[i] == "ADVERB":
        word = pyip.inputStr("Please input a(n) %s:" % libList[i])
    if libList[i] == "VERB":
        word = pyip.inputStr("Please input a(n) %s:" % libList[i])
    if libList[i] == ".":
        libList[i-1] = libList[i-1] + libList[i]
    libList[i] = word
    i += 1

# checks for and removes any lone  periods(.)
libList.remove('.')

# outputs string after combining list
libText = " ".join(libList)
print(libText)

# prints to a text file
lib = open("finishedLib.txt", "w")
lib.write(libText)
lib.close()

