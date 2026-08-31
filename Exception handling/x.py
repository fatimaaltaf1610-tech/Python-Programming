try:
    print(x)
except NameError:
    print("Variable is not defined")
else:
    print("Something else went wrong")