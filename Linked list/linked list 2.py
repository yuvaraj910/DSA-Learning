class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = None

while True: 
    task = input("Enter new task :")
    new_node = Node(task)

    if head is None:
        head = new_node
    else:
        current = head

        while current.next is not None:
            current = current.next

        current.next = new_node