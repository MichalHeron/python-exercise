# isSkyBlue = True
# isPythonDifficult = False

# isIt = isSkyBlue and isPythonDifficult
# print(isIt)

# b = "dsafsd a"

# a = f"ad dafda \\\d dsdsd {b}" #interpolacja stringa 
# print(b.replace("a","c"))

# def add(a, b):
#     print(a+b)

# c= 3.5
# d = "4.5"

# add(c,float(d))


# try:
#     age = int(input("Enter your age: "))
#     print("You entered an integer.")
# except ValueError:
#     try:
#         age = float(input("Enter your age: "))
#         print("You entered a floating-point number.")
#     except ValueError:
#         print("You did not enter a number.")

# age = input("enter your age: ")
# if age.isdigit():
#     age = int(age)
#     print(age)
# else:
#     print("give a number")

# age = ""
# while not age.isdigit():
#     age = input("enter your age: ")
# print("Twoj wiek: " + age + "!")


# light = input("what is the color?")
# match light:
#     case "red":
#         print("stop")
#     case "yellow":
#         print("wait")
#     case "green":
#         print("go")
#     case _:
#         print("wrong light")  

# for number in range(1, 11):
#     if number == 6: 
#         continue 
#         break
#     print(number)

#######################
# number = ""
# while not number.isdigit():
#     number = input("enter your number: ")

# def is_odd_even(n):
#     if n % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# print("Your number is", is_odd_even(float(number)))

########################

# for n in range(0,101):
#     print(n)

##################### isprime check

# is_prime = True
# for n in range (2,101):
#     for m in range (2, n + 1):
#         is_prime = True
#         if n == m:
#             continue
#         if n % m != 0:
#              continue
#         is_prime = False
#         break
#     if is_prime:
#          print(n)

         ###### sum of even numbers
# sum = 0;
# for n in range (1, 100):
#     if n % 2 == 0:
#         sum += n
# print(sum)

#########

