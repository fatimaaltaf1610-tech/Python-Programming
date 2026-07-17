Amount =int(input("Please enter amount for withdrawl: "))
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
note_4 = (((Amount%100)%50)%10)//5
print("notes of 100 rupee: ", note_1)
print("notes of 50 rupee: ", note_2)
print("notes of 10 rupee: ", note_3)
print("notes of 5 rupee ", note_4)