class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

head = None

def add_task(task):
    global head

    new_node = Node(task)
    if head is None:

        head = new_node

    else:
        current = head

        while current.next is not None:
            current = current.next

        current.next = new_node

def display():
    if head is None:
        print("No tasks available")
        return
    else:

        current = head 
        count = 1

        while current is not None:
            print(f"{count}.{current.data}")
            count += 1
            current = current.next


def delete(task):
    global head

    if head is None:
        print("Tasks not available")
        return

    if head.data == task:
        head = head.next
        print("task deleted")
        return
    previous = None
    current = head

    while current is not None:

        if current.data == task:
            previous.next = current.next
            print("Task deleted")
            return

        previous = current
        current = current.next

    print("task not found")


print("----To Do list----")
print("1.add task")
print("2.delete task")
print("3.display task")
print("4.exit")
while True:

    choice = int(input("Enter your choice :"))
    if choice == 1:
        task = input("Enter the task to be added :")
        add_task(task)
        print("task added")
    elif choice == 2:
        task = input("Enter the task to be deleted :")
        delete(task)
        print("task deleted")
    elif choice == 3:
        display()
    elif choice == 4:
        print("exiting...")
        break

    else:
        print("invalid input")