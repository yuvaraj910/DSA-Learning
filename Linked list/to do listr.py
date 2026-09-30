class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


task1 = Node("Running")
task2 = Node("Gym")
task3 = Node("study")
task4 = Node("gaming")

head = task1

task1.next = task2
task2.next = task3
task3.next = task4

current = head
count = 1
while current is not None:
    print(f"{count}.{current.data} ")
    count += 1
    current = current.next