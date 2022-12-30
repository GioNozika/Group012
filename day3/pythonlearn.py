#my_name = "Giorgi"

# if "G" in my_name:
#     print("sheicavs G-s")
    
# else:
#     print("ar sheicavs G-s")    

# my_sentence = "aa {2} bb {1} cc {0}".format("xx",  "yy" , "zz")

# print(my_sentence)

# my_name = "Giorgi"
# my_surname = "Nozadze"
# my_age = 15
# my_hobby = "football/programming"

# my_info = "me mqvia {} {}. me var {} wlis. chemi hobbia {}.".format(my_name,my_surname,my_age,my_hobby)

# print(my_info)


# if "G" in my_name:
#     print("sheicavs G-s")
# else:
#     print("ar sheicavs")


# my_name = input("enter your name: ")
# my_surname = input("enter your surname: ")
# my_gmail = input("enter your gmail: ")


# print("chemi saxelia " + my_name)
# print("chemi gvaria " + my_surname)
# print("chemi gmail " + my_gmail)


# my_name = input("enter your name: ")
 
# my_surname = input("enter your surname: ")
# my_gmail = input("enter your gmail: ")
# my_age = int(input("enter your age: "))
# years = int(input("enter years: "))
# my_info = ("chemi saxelia {}.chemi gvaria {}.me var {} wlis.chemi gmail {}. " ).format(my_name,my_surname,my_age,my_gmail)


# print(my_info)

# new_age = int(my_age) + int(years)


# print("gavida {} weli da gavxdi  {}   wlis".format(years,new_age))

# num1 = int(input("enter number 1: "))
# num2 = int(input("enter number 2: "))

# answer = num1 * num2
# you_Won = "Very good you won"
# if answer > 100:
#     print(answer)
#     print("Very good you won 🙂")
# else:
#     print("Sorry 🙁 You lose")    


# საშინაო დავალება N33

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))



answer = num1 + num2 + num3

if  num1 % 2 == 0 and  num2 and num3 % 2 > 0:
    print(num2+num3)
elif num2 % 2 == 0 and num1 and num3 % 2 > 0:
    print(num1 + num3)
elif num3 % 2 == 0 and num1 and num2 % 2 > 0:
    print(num1 + num2)
elif num1 and num2 and num3 % 2 == 0:
    print("No answer") 
else:
    print(answer)

