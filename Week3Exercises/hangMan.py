from random_words import RandomWords
game = ""
while game != "quit":
    turns = 7
    hang_word_arr = []
    blank_spaces_arr = []
    rw = RandomWords()
    word = rw.random_word()
    # print(word)

    for char in word:
        hang_word_arr.append(char)

    for char in hang_word_arr:
        blank_spaces_arr.append("_")

    word_final = ' '.join(map(str, blank_spaces_arr))
    hang_word = ' '.join(map(str, hang_word_arr))

    print("Welcome to Hangman! Enter a letter to fill out the word...\n")

    while turns > 0 and hang_word != word_final:
        if turns == 7:
            print("_________________")
            print("|                ")
            print("|                ")
            print("|                ")
            print("|                ")
            print("|________________")
        elif turns == 6:
            print("_________________")
            print("|         |      ")
            print("|                ")
            print("|                ")
            print("|                ")
            print("|________________")
        elif turns == 5:
            print("_________________")
            print("|         |      ")
            print("|         O      ")
            print("|                ")
            print("|                ")
            print("|________________")
        elif turns == 4:
            print("_________________")
            print("|         |      ")
            print("|         O      ")
            print("|         |      ")
            print("|                ")
            print("|________________")
        elif turns == 3:
            print("_________________")
            print("|         |      ")
            print("|       __O      ")
            print("|         |      ")
            print("|                ")
            print("|________________")
        elif turns == 2:
            print("_________________")
            print("|         |      ")
            print("|       __O__    ")
            print("|         |      ")
            print("|                ")
            print("|________________")
        elif turns == 1:
            print("_________________")
            print("|         |      ")
            print("|       __O__    ")
            print("|         |      ")
            print("|        /       ")
            print("|________________")

        print("\nGuess a letter...")
        print(word_final)
        guess = input()
        if guess in hang_word_arr:
            for i, value in enumerate(hang_word_arr):
                if guess == hang_word_arr[i]:
                    blank_spaces_arr[i] = hang_word_arr[i]
        else:
            turns -= 1
            print(guess + " is not in the word! You have %d more guesses..." % turns)
        word_final = ' '.join(map(str, blank_spaces_arr))

        if hang_word == word_final:
            print("Win!")
        if turns == 0:
            print("_________________")
            print("|         |      ")
            print("|       __O__    ")
            print("|         |      ")
            print("|        / \     ")
            print("|________________")
            print("LOSE!")

    print("Enter anything to start a new game, or 'quit' to exit")
    game = input()


