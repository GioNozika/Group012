name1 = input("enter name number1: ")
name2 = input("enter name number2: ")


ammount_of_vowels_in_name1 = 0
ammount_of_vowels_in_name2 = 0



for char in name1:
    if char in "aeiou":
        ammount_of_vowels_in_name1 += 1
 
for char in name2:
    if char in "aeiou":
        ammount_of_vowels_in_name2 += 1



if ammount_of_vowels_in_name1 > ammount_of_vowels_in_name2:
    print( "{} has most Wovels.It has {} wovels".format(name1,ammount_of_vowels_in_name1))
if ammount_of_vowels_in_name2 > ammount_of_vowels_in_name1:
    print( "{} has most Wovels.It has {} wovels".format(name2,ammount_of_vowels_in_name2))




