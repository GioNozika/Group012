num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

my_sum = 0

if num1 % 2 == 1:
    my_sum += num1
if num2 % 2 == 1:
    my_sum += num2
if num3 % 2 == 1:
    my_sum += num3
else:
    print("No answer")




my_info = "Here is sum of even numbers {}".format(my_sum)


print(my_info)
