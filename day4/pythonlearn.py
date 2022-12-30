# my_name = "Giorgi"

# for char in my_name:
#     print(char)


# name1 = input("enter your  name: ")
# name2 = input("enter your  name: ")

# amount_of_vowels_in_name1 = 0 
# amount_of_vowels_in_name2 = 0 

# for char in name1:
#   if  char in "aeiou":
#     amount_of_vowels_in_name1 +=1

# for char in name2:
#   if  char in "aeiou":
#     amount_of_vowels_in_name2 +=1


# if amount_of_vowels_in_name1 > amount_of_vowels_in_name2:
#     print(name1)
#     print("amount of wovels in name 1 is more and it contains {} vowels".format(amount_of_vowels_in_name1))
# elif amount_of_vowels_in_name1 > amount_of_vowels_in_name2: 
#     print(name2)
#     print("amount of wovels in name 2 is more and it contains {} vowels".format(amount_of_vowels_in_name2))
# else:
#     print("amount of vowels in this two names are tied")


# my_text = input("enter your sentence: ")
# amounts_of_a = 0
# for char in my_text:
#     if char in "a":
#         amounts_of_a += 1

# print('There is {} amount of "a" in text'.format(amounts_of_a))

# num = 12
# if num>5:
#     print("Bigger than 5")
#     if num <= 47:
#         print("between 5 and 47")

name1 = input("enter name number1: ")
name2 = input("enter name number2: ")

amount_of_tanxmovani_in_name1 = 0
amount_of_tanxmovani_in_name2 = 0

for char in name1:
  if char in "bcdfghjklmnpqrstvwxyz":
     amount_of_tanxmovani_in_name1 += 1


for char in name2:
  if  char in "bcdfghjklmnpqrstvwxyz":
    amount_of_tanxmovani_in_name2 += 1

if amount_of_tanxmovani_in_name1 > amount_of_tanxmovani_in_name2:
    print("amount of tanxmovani in {1} is more than amount of tanxmovani in {2} and it contains {0} tanxmovani".format(amount_of_tanxmovani_in_name1,name1,name2))
elif amount_of_tanxmovani_in_name2 > amount_of_tanxmovani_in_name1:
    print("amount of tanxmovani in {2} is more than amount of tanxmovani in {1} and it contains {0} tanxmovani".format(amount_of_tanxmovani_in_name2,name1,name2)) 
else:
    print("amount of tanxmovani in these two names are tied")
