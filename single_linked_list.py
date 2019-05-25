class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, n):
        self.next = n

    def get_next(self):
        return self.next


class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def get_length(self):
        return self.length

    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.set_data(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node()
        new_node.set_data(data)
        current_node = self.head
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(new_node)
        self.length += 1

    def insert_at(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            self.length += 1
            return

        if position >= self.length:
            self.insert_at_end(data)
            self.length += 1
            return

        current_position = 1
        current_node = self.head

        while current_position != position:
            current_node = current_node.get_next()
            current_position += 1

        new_node = Node()
        new_node.set_data(data)
        new_node.set_next(current_node.get_next())
        current_node.set_next(new_node)
        self.length += 1

    def display_list(self):
        if self.length == 0:
            print("\nEmpty list\n")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.get_data(), end=" ")
            current_node = current_node.get_next()
        print()

    def search(self, data):
        current_node = self.head
        current_position = 0
        while current_node is not None:
            if current_node.get_data() == data:
                print("\n{} is at {} position".format(data, current_position))
                return
            current_position += 1
            current_node = current_node.get_next()
        else:
            print("Data not found")

    def get_data_at(self, position):
        if position >= self.length:
            return "\nPosition out of range"

        current_node = self.head
        current_position = 0

        while current_position != position:
            current_node = current_node.get_next()
            current_position += 1

        return current_node.get_data()


sll = SingleLinkedList()
sll.insert_at_beginning("nani")
sll.insert_at_end(11)
sll.insert_at_beginning(20)
sll.insert_at_end(10)
sll.insert_at(15, 2)
sll.insert_at(16, 4)
sll.display_list()
sll.search(10)
sll.search(16)
sll.search("nani")
print(sll.get_data_at(1))

