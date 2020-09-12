# 3 major groups of errors:
# SyntaxError
# RuntimeError
# LogicalError

# SyntaxError - mistakes in the use of the python languages, similar to grammar or spelling mistakes in a language
# common:
# leaving out a keyword
# putting a keyword in the wrong place
# incorrect indentation
# empty block

# RuntimeError - mistakes that were not found when the code was being compiled, the command was syntactically correct but could not be performed
# common:
# division by 0
# performing an operation on incompatible types
# using and identifier which has not been defined
# attribute doesn't exist
# access a file that doesn't exist

# LogicalError - mistakes that do not result in the program crashing but are caused because of a logical error, resulting in an incorrect result
# common:
# using the wrong variable name
# indenting a block to the wrong level
# using integer division, not floating point division
# getting operator precedence wrong
# making a mistake in a boolean
# off-by-one, numerical errors

# Handling Exceptions
# try:
#     age = int(input("give me your age: "))
#     print("I see you are %d years old" % age)
# except ValueError:
#     print("that wasn't a number")
#
# try:
#     dividend = int(input("enter a dividend: "))
#     divisor = int(input("Please enter a divisor: "))
#     print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
# except ValueError:
#     print("something went wrong")
# except ZeroDivisionError:
#     print("Can't divide by zero")
#
# try:
#     dividend = int(input("enter a dividend: "))
# except ValueError:
#     print("the dividend has to be a number")
# try:
#     divisor = int(input("Please enter a divisor: "))
# except ValueError:
#     print("the divisor has to be a number")
# try:
#     print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
# except ZeroDivisionError:
#     print("cannot divide by zero")

# with error checks
# n = None
# while n is None:
#     s = input("enter a number: ")
#     if s.lstrip('-').isdigit():
#         n = int(s)
#     else:
#         print("%s is nto a number" % s)

# with exception handling
# n = None
# while n is None:
#     try:
#         s = input("enter a number: ")
#         n = int(s)
#     except ValueError:
#         print("%s is not a number" % s)

# abs()
# intNum = -25
# floatNum = -10.50
# print("The absolute value of int is:", abs(intNum))
# print("The absolute value of float is:", abs(floatNum))

# Debug Tools
# Pyflakes - parses code instead of importing it
# Pylint - more extensive error checking enforces coding standards
# Pychecker - more extensive error checking enforces coding standards
# Pep8 - style aka now pycodestyle
# pdb
# logging - critical, error, warning, info, debug
