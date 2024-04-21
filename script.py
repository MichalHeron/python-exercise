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
# a = input("podaj dlugosc pierwszego z boków w mm: ")
# while not a.isdigit():
#     a = input("nie podałes liczby. podaj dlugosc pierwszego z boków w mm: ")

# b = input("podaj dlugosc drugiego z boków w mm: ")
# while not b.isdigit():
#     b = input("nie podałes liczby. podaj dlugosc drugiego z boków w mm: ")

# print("pole prostokąta wynosi: ",  float(a) * float(b))

########### checking female or male name (latter a in the end)
# your_name = input("podaj swoje imie: ")

# if your_name[-1] == "a":
#     print("to imie jest żeńskie")
# else:
#     print("to imie jest męskie")

#####
# number_one = int(input("podaj pierwszą liczbę: "))
# number_two = int(input("podaj drugą liczbę: "))
# number_three = int(input("podaj trzecią liczbę: "))

# if number_one > number_two and number_one > number_three:
#     print(number_one)
#     if number_two > number_three:
#         print(number_two)
#         print(number_three)
#     else:
#         print(number_three)
#         print(number_two)
# elif number_two > number_one and number_two > number_three:
#     print(number_two)
#     if number_one > number_three:
#         print(number_one)
#         print(number_three)
#     else:
#         print(number_three)
#         print(number_one)
# else:
#     print(number_three)
#     if number_one > number_two:
#         print(number_one)
#         print(number_two)
#     else:
#         print(number_two)
#         print(number_one)

# numbers = [number_one, number_two, number_three]
# numbers.sort(reverse=True)
# print(numbers)
########

# import random

# random_number = random.randint(1, 100)
# win = False
# while not win:
#     your_number = int(input("podaj liczbę z przedziału 1-100: "))
#     if your_number == random_number:
#         print("wygrałeś")
#         win = True
#     elif your_number > random_number:
#         print("za dużo")
#     else:
#         print("za mało")
# print("GG")

################### lists

# names = ['Kamil', 'Mariusz']
# names.append('Kasia') #pojedynczy lement
# names.extend(['Paulina', 'Mariusz']) #kilka elementow
# print(names[0])

# print(names)

# for n in names:
#     print(n)

# del names[1]
# names.remove('Kasia')
# print(names.count('Mariusz'))
# print(names)

##### set  (zbiór)
# names3 = set()
# names = {'Kamil', 'Mariusz'} # nie moze miec duplikatow nie sa uporzadkowane
# names2 = {'Kamil', 'Paulina', 'Asia', 'Rafał'}

# print(names.intersection(names2))
# print(names.union(names2))

# print(names.difference(names2))

# print(names.symmetric_difference(names2))

# names.add('Kasia')
# names.update({'Adam', 'Rafał'})
# print(names)

# names.remove('Kasia')

# print(names)

##### dictionary
# phone_book = {
#     'Kamil': 100200300,
#     'Mariusz': 123456789,
#     'Paulina': 987654321
# }

# phone_book['Dominik'] = 349502432

# print(phone_book.get('Kamil'))
# print(phone_book['Paulina'])

# phone_book.pop('Kamil') #usuwanie

# print(phone_book)

# for element in phone_book.items():
#     print(element[0] + ":" + str(element[1]))

# for name, phone_number in phone_book.items():
#     print(name + ":" + str(phone_number))

# for element in phone_book.values():
#     print(element)

####### tuple (krotka)(podobna do listy) ale nie modyfikujemy go 

names = ('Kamil', 'Mariusz', 'Paulina')

print(names[0])

######

