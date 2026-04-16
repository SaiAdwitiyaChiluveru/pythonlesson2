try:
    num1, num2, = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Dividing by zero is error !!")
except SyntaxError:
    print("Comma is missing. Enter the numbers separated by a comma like this 1, 2 ")
except:
    print("Wrong Input!!")
else:
    print("No Exceptions")
finally:
    print("This will run no matter what!")