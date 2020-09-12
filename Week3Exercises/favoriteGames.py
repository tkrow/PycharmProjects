# Game storage
def titleBar():
    gamesStored = len(games)

    print("************************")
    print("   Game Storage   ")
    print("You have %d games stored" % gamesStored)
    print("************************\n")

def options():
    option = ''
    print("[1] See stored games")
    print("[2] Store new game")
    print("[q] Quit")
    option = input("What would you like to do ^_^  ")
    if option == '1':
        listGames()
    elif option == '2':
        addGames()
    elif option == 'q':
        quit()
    else:
        print("I don't know what that is.")
        options()

def listGames():
    if len(games) > 0:
        print("I know the following games")
    else:
        print("You don't have any games saved right now OwO")
    for game in games:
        print(game)
    options()

def addGames():
    newGame = ''
    while newGame != 'q':
        print("Enter 'q' to quit entry")
        newGame = input("What game would you like to save UwU  ")
        if newGame != 'q' and len(games) > 0:
            for game in games:
                if newGame != game:
                    games.append(newGame)
                    print("I will remember this game, owo.")
                else:
                    print("I already know this game UwU. Nice choice ^_^.")
        elif newGame != 'q':
            print("I will remember this game, owo.")
            games.append(newGame)
    options()

def quit():
    try:
        file = open('savedGames.pydata', 'wb')
        pickle.dump(games, file)
        file.close()
        print("\nI will remember the following games: ")
        for game in games:
            print(game)
    except Exception as e:
        print(e)
        print("\nI can't figure out how to store the games")

import pickle

try:
    file = open("savedGames.pydata", 'rb')
    games = pickle.load(file)
    file.close()
except:
    file = open("savedGames.pydata", 'wb')
    file.close()
    games = []

titleBar()
options()

