# def greet(name):
#     print(f"Hello {name}!")
#     print("Good Afternoon!")

# greet('Livin')

# def calcVal(a,b,c):
#     print(a-b/c)

# calcVal(2,9,3)
# calcVal(b=90,c=30,a=20)

# def calcVal(a,b=10):
#     print(a*b)

# calcVal(a=2)

# def findsum(*values):
#     total = 0
#     for num in values:
#         total += num
#     print(total)
    
# findsum(2,3,4,5,6,7,8)

# def pritSteps():
#     print("Step1")
#     print("Step2")
#     return "Gift"
#     print("Step3")
#     print("Step4")
#     print("Step5")
    

# print(pritSteps())

# def findProduct(a,b):
#     return a*b

# print(findProduct(2,findProduct(3,findProduct(6,1/6))))

a=15

def greet():
    a=10
    print(f"The a's value from inside of function1: {a}")

# def greet1():
#     print(f"The a's value from inside of function2: {a}")
    
    

greet()
print(f"The a's value from outside of function1: {a}")
# greet1()