# need to import math modules for mathematical function
# import math

# print("hello world")
# print("*" * 10)
# print("hello world")
# x = 1
# y = 3

# # we need to install python extention to usevscode as ide in python
# # you can run current file by clicking play button on top right
# # to format python
# # go to view -> commant palette search format document you need to install autopep8
# # run run format document and it will format your document
# # to format document on save goto file -> preferencs -> setting search and select  Format On Save now your code will get format automatically on save
# # to associate shortcut to run python by shortcut key
# # open command palette -> search for run python file -> clink om keybinding -> provide shortcut key and press enter
# unit_price = 3

# # funcdamental  to python
# student_count = 1000
# rating = 4.99
# is_published = False
# course_name = "python programming"
# print(student_count)
# # titple code to format long string
# message = """
# hi all
# this is long strong
# with multi line
# """
# print(message)
# # length of sring
# lenght = len(message)
# print(f"Total length : {lenght}")
# # to get character
# print(message[1])
# print(message[-1])
# # slice a string print(message[0:3]) return first 3 character
# print(message[0:4])
# # hot to add double quoe in string -- we can use \
# course = " python \"programming"
# print(course)
# # escape sequences in python
# # \"
# # \'
# # \\
# # \n  for new line

# # to print full name

# first = "firdous"
# last = "alam"
# # full = first+" "+last
# # or we can use we can use f and {}
# full = f"{first} {last}"
# print(full)

# # string function in python
# print(course.capitalize())
# print(course.upper())
# print(course.title())
# print(course.strip())
# print(course)
# print(course.find("pro"))
# print(course.find("Pro"))
# print(course.replace("p", "j"))
# print("pro" in course)
# print("swift" not in course)


# # number method there are 3 type of number integer,float and complex number (a+bj)

# print(10+3)
# print(10-3)
# print(10*3)
# print(10/3)
# print(10//3)  # return only integer
# print(10 % 3)  # modulus
# print(10 ** 3)  # power

# print(round(2.9))

# print(abs(-2.9))
# # for mathematical function we need to import math modules

# print(math.ceil(2.2))

# # x = input("x: ")
# # Traceback (most recent call last):
# #  File "C:\Users\techn\TechnophileFirdous\pythonBeginning\app.py", line 90, in <module>
# #    y = x + 1
# #       ~~^~~
# # TypeError: can only concatenate str (not "int") to str
# # y = x + 1
# # print(type(x))
# # need to type convert
# # int(x)
# # float(x)
# # bool(x)
# # str(x)

# #

# # falsy
# # ""
# # 0
# # None
# # anyhting else is true

# # bool(0)
# # # False
# # bool(1)
# # # True
# # bool(-1)
# # # True
# # bool("")
# # # False

# # Comparision operator

# # >>> 10>3
# # True
# # >>> 10>=3
# # True
# # >>> 10<20
# # True
# # >>> 10<=20
# # True
# # >>> 10=10
# #   File "<python-input-12>", line 1
# #     10=10
# #     ^^
# # SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
# # >>> 10 == 10
# # True
# # >>> 10 == "10"
# # False
# # >>> "bag" > "apple"
# # True
# # >>> "bag" == "BAG"
# # False
# # >>> ord("b")
# # 98
# # >>> ord("B")
# # 66

# conditional operator
# if statement
# temperature = 35
# if temperature > 300:
#     print("it's warm")
#     print("Drink water")
# print("Done")

# for multiple condition we can use elif
temperature = 15
if temperature > 30:
    print("it's warm")
    print("Drink water")
elif temperature > 20:
    print("it's nice")
else:
    print("it's cold")
print("Done")

# small program to check eligibility

age = 22
if age >= 18:
    print("eligible")
else:
    print("not eligible")

 # or we can rewrite using variable or trinary operator

message = "Eligible" if age >= 19 else "Not eligible"
print(message)
# 3 logical operator
#  and or not

high_income = True
good_credit = False
student = True
if high_income and good_credit:
    print("eligible for credit")
else:
    print("Not eligible")

if not student:
    print("student eligible for credit")
else:
    print("student Not eligible")


# chaining comparision operator

age = 22
# if age>=18 and age < 65 we can write this to
if 18 <= age < 65:  # just like make comparision
    print("age is eligible")
else:
    print("age not eligible")

# loop in python for

# for number in range(3):
#     print(f"Attempt {number+1}")

# # if we want to jump out of loop and use for-else statement
# successful = False
# for number in range(3):
#     print(f"Attempt {number}")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attemted 3 time and failed")
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(f"even {number}")
        count += 1

print(f"number of time even number occur = {count}")


###################
# writing a function
############
