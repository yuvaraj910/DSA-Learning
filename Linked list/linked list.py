class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


task1 = Node("Study")
task2 = Node("Gym")
task3 = Node("gaming")


head = task1
task1.next = task2
task2.next = task3


current = head
while current is not None:
    print(current.data)
    current = current.next