# print("Ster")


# try:
#     print("The"+1)
# except ZeroDivisionError:
#     print("This is invalid expression")
# except TypeError:
#     print("Value Error has occured")


try:
    num1=int(input("Enter the Number1: "))
    num2=int(input("Enter the Number2: "))
    print(num1/num2)
except ValueError:
    print("Please provide valid number!")
except ZeroDivisionError:
    print("invalid Expression!")
finally:
    print("Final Step!")


