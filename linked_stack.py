class Stack:
    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, data):
        self.items.append(data)
        self.length += 1

    def pop(self):
        if self.length == 0:
            print("No elements in stack")
            return
        self.items.pop()
        self.length -= 1

    def get_length(self):
        return self.length

    def get_stack(self):
        return self.items


def main():
    stack = Stack()
    while True:
        try:
            ch = int(input("\n1.Push"
                           "\n2.Pop"
                           "\n3.Display"
                           "\n4.Exit"
                           "\nChoose a option: "))
        except ValueError:
            print("Invalid option selected")
            continue
        if ch == 1:
            data = input("Enter data: ")
            stack.push(data)
        elif ch == 2:
            stack.pop()
        elif ch == 3:
            print(stack.get_stack())
        elif ch == 4:
            break
        else:
            print("Invalid option selected")


if __name__ == '__main__':
    main()
