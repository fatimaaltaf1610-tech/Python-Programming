pet_task = ["feeding the pet", "refilling the water bowl", "cleaning the pet area", "taking the pet for a walk"]

original_count = len(pet_task)

completed_count = 0

while len(pet_task) > 0:
    next_task = pet_task[0]
    answer = input("Have you finished " + next_task + "? (yes/no): ")

    if answer == "yes":
        pet_task.pop(0)
        completed_count += 1
        print("Great job! Pet care task completed!")
    else:
        print("No problem! Try doing it now.")
        
        print("Pet care tasks remaining: ", len(pet_task))
        print("")

        