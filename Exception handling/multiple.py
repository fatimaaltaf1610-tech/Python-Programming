try:
    num1, num2 = eval(input("Enter two numbers seperated by a comma: "))
    result = num1 / num2
    print("Result is: ", result)

except ZeroDivisionError:
    print("Division by Zero is an error!!")

except SyntaxError:
    print("The comma is missing. Add a comma, for example x , y.")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")