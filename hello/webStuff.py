# request library
# allows to download pages from the internet
#
# import requests
# page = requests.get("https://www.python.org")
# # print(page.text)
#
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
#
# soup = BeautifulSoup(page.content, 'html.parser')
# soup.find_all('p') # <p> tags

# urllib.request -  urlopen function http:// or https:// or ftp:// or ssh:

# import urllib.request
# import shutil
# import tempfile
#
# with urllib.urlopen('http://www.python.org/') as response:
#     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#         shutil.copyfileobj(response, tmp_file)
# with open(tmp_file.name) as html:
#     pass

# import urllib.request
# req = urllib.request.Request('https://huntsd.com')
# with urllib.request.urlopen(req) as response:
#     the_page = response.read()

# import urllib.parse
# # import urllib.request
# #
# # url = 'http://huntsd.org'
# # values = {'name' : 'aaron smith',
# #           'location' : 'Huntington',
# #           'language' : 'Python'}
# # data = urllib.parse.urlencode(values)
# # data = data.encode('ascii') # this data should be in bytes
# # req = urllib.request.urlopen(req) as response:
# #     the_page = response.read()

from tkinter import Tk, Label, Button

class FirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A small GUI")

        self.label = Label(master, text="This is our first GUI")
        self.label.pack()

        self.greet_button = Button(master, text="Hello", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=self.quit)
        self.close_button.pack()

    def greet(self):
        print("welcome!")

    def quit(self):
        quit()

root = Tk()
my_gui = FirstGUI(root)
root.mainloop()
