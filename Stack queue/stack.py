stack = []

def push():
    value = input("Enter value:")
    stack.append(value)
    print("Element pushed")

def pop():
    if not stack:
        print("Stack underflow")
    else:
        print("Element poped")
        stack.pop()

def peek():
    if not stack:
        print("Stack underflow")
    else:
        print(f"top : {stack[-1]}")

def dislay():
    if not stack:
        print("stack is empty")
    else:
        print(f"Stack : {stack}")

        