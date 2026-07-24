total_homework = 4
original_count = total_homework
print(f"You have {original_count} homework tasks to complete today!\n")

completed_count = 0
task_num = 1

while task_num <= total_homework:
    if task_num == 1:
        next_task = "math worksheet"
    elif task_num == 1:
        next_task = "science worksheet"
    elif task_num == 3:
        next_task = "english worksheet"
    else:
        next_task = "coding practice"

    answer = input(f"Have you finised {next_task} ? (yes/no): ")

    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("Great job!")
    else:
        print("its okay, complete it now")

    print("Homework tasts remaining: ", total_homework - completed_count)
    print()

print("=========ALL HOMEWORK COMPLETE!=========")
print("Great job finishing your work today!")

print("Now lets safely peek at an infinite loop.")
test_value = 0
safety_counter = 0

while test_value <= 0:
    print("This cndition never changes so this would run forever")
    safety_counter += 1

    if safety_counter == 3:
        print("(stopping here on purpose!)")
        break 

print("============HOMEWORK COMPLETION SUMMARY====================\n")
print("Homework assigned today: ", original_count)
print("Homework completed: ", completed_count)
print("Homework remianing: ", total_homework - completed_count)
print("============================================================")