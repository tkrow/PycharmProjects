import tkinter
import random

class NewGui:
    def __init__(self, master):
        self.master = master
        master.title("A small GUI")

        self.secret_number = random.randint(1, 100)
        self.guessCount = 0

        print(self.secret_number)
        self.guessLabel = tkinter.Label(master, text="0")
        self.guessLabel.pack()

        self.addButton = tkinter.Button(master, text="Add 1", command=self.add)
        self.addButton.pack()

        self.subtractButton = tkinter.Button(master, text="Remove 1", command=self.subtract)
        self.subtractButton.pack()

        self.submitButton = tkinter.Button(master, text="Guess", command=self.guess)
        self.submitButton.pack()

        self.guessedLabel = tkinter.Label(master, text="Please guess")
        self.guessedLabel.pack()

    def add(self):
        guess = self.guessLabel['text']
        guess = int(guess) + 1
        self.guessLabel['text'] = guess

    def subtract(self):
        guess = self.guessLabel['text']
        guess = int(guess) - 1
        self.guessLabel['text'] = guess

    def guess(self):
        self.guessCount += 1
        guess = self.guessLabel['text']
        if int(guess) > self.secret_number:
            self.guessedLabel['text'] = "Too High"
        if int(guess) < self.secret_number:
            self.guessedLabel['text'] = "Too Low"
        if int(guess) == self.secret_number:
            self.guessedLabel['text'] = "You got the right answer after %d guess(es)" % self.guessCount


root = tkinter.Tk()
my_gui = NewGui(root)
root.mainloop()
