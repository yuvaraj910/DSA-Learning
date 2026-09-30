student = []
student_id = []
student_class = []
#ask
ask = input("Choose an option on CRUD").lower().strip()


if ask == "create" or ask == "c":
    # Create 
    name = input("Enter the name to be added on the list : ").lower().strip()
    student.append(name)
    idd = int(input("ID no. :").lower().strip())
    student_id.append(idd)
    class1 = input("Student Class :").lower().strip()
    student_class.append(class1)
elif ask == "remove" :
    #remove
    name = input("Enter the student to be removed")
    index = student.index(name)

    student.pop(index)
    student_id.pop(index)
    student_class.pop(index)
    
elif ask == "update" or ask == "u":
    #update
    ask1 = input("What to update name,id no. or class :").lower().strip()
    if ask1 in ("name","n"):
        old_name = input("Enter the old name :").lower().strip()
        index = student.index(old_name)
        new_name = input("Enter the new name :").lower().strip()
        student[index] = new_name
    elif ask1 in ("id"):
        old_id = int(input("Enter the old id :").lower().strip())
        index = student_id.index(old_id)
        new_id = int(input("Enter the new id :").lower().strip())
        student_id[index] = new_id
    elif ask1 in ("class"):
        old_class = input("Enter the old class :").lower().strip()
        index = student_class.index(old_class)
        new_class = input("Enter the new class :").lower().strip()
        student_class[index] = new_class
elif ask in ("read","r"):
    name = input("which student details you want :").lower().strip()

    if name == "all":
        for i in range(len(student)):
            print(
                f"{student[i]} | {student_id[i]} | {student_class[i]}"
            )
    else:
        index = student.index(name)

        print(f"{student[index]} | {student_id[index]} | {student_class[index]}")