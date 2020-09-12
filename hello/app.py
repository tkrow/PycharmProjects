mainFile = 'add.txt'

file = open(mainFile, 'r')
for text in file:
    print(text)
file = open(mainFile, 'w')
file.write("Here is words! Come at me bruh!\n")

# mainFile = 'saw.txt'
# file = open(mainFile, 'x')

mainFile = 'saw.txt'
file = open(mainFile, 'w+')
file.write('More chainsaw \n')
file.close

# File handling methods
# detach() - separate and underlying binary buffer from the text
# fileno() - return the integer nuumber of the file
# flush() - flush a write buffer of the file stream
# isatty() - return a true if a file stream is inactive
# read(n) - read almost n chars from the file
# readable() - returns true if a file stream can be read from
# readline(n=1) - returns 1 line from file
# readlines(n=-1) - reads multiple lines from file
# seek(offset, from=SEEK_SET) - changing the file position
# seekable() - returns true if the file supports random access
# tell() - returns the location of the current file
# truncate(size=NONE) - change file size
# writable() - can be written to the file stream
# write(s) - write strings to file and return number of characters written
# writelines(lines) - write a liest of lines to a file
