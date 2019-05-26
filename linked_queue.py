class Queue:
    def __init__(self):
        self.elements = []
        self.length = 0

    def enqueue(self, data):
        self.elements.insert(0, data)
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            print("No elements in list")
            return

        self.elements.pop()
        self.length -= 1

    def get_length(self):
        return self.length

    def get_queue(self):
        return self.elements


def main():
    queue = Queue()
    while True:
        try:
            ch = int(input("\n1.Enqueue"
                           "\n2.Dequeue"
                           "\n3.Display"
                           "\n4.Exit"
                           "\nChoose a option: "))
        except ValueError:
            print("Invalid option selected")
            continue
        if ch == 1:
            data = input("Enter data: ")
            queue.enqueue(data)
        elif ch == 2:
            queue.dequeue()
        elif ch == 3:
            print(queue.get_queue())
        elif ch == 4:
            break
        else:
            print("Invalid option selected")


if __name__ == '__main__':
    main()
