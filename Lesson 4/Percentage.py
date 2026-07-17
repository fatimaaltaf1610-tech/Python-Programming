print("Enter your marks obtained in 4 subjects: ")
math = int(input("maths: "))
physics = int(input("physics: "))
bio = int(input("bio: "))
chem = int(input("chem: "))
sum = math+physics+bio+chem
print("The sum of math, physics, bio, and chem is = ", sum)
percentage = (sum/400)*100
percentage2 = int(percentage)
print(percentage2, end = "%")