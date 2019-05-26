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
        if self.length == 0:
            self.head = new_node
            self.length += 1
            return

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

    def get_list(self):
        if self.length == 0:
            return "Empty list"

        elements = []
        current_node = self.head
        while current_node is not None:
            elements.append(current_node.get_data())
            current_node = current_node.get_next()
        return elements

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

    def delete_at_beginning(self):
        if self.get_length() == 0:
            print("\nNo elements in list")
            return
        self.head = self.head.get_next()
        self.length -= 1

    def delete_at_end(self):
        if self.length == 0:
            print("\nNo elements in list")
            return

        if self.length == 1:
            self.head = None
            self.length -= 1
            return

        current_node = self.head
        previous_node = current_node
        current_node = current_node.get_next()

        while current_node.get_next() is not None:
            previous_node = previous_node.get_next()
            current_node = current_node.get_next()

        previous_node.set_next(None)
        self.length -= 1

    def delete_at(self, position):
        if position == 0:
            self.delete_at_beginning()
            return

        if position >= self.length:
            self.delete_at_end()
            return

        current_position = 1
        current_node = self.head
        previous_node = current_node
        current_node = current_node.get_next()

        while current_position != position:
            previous_node = previous_node.get_next()
            current_node = current_node.get_next()
            current_position += 1

        previous_node.set_next(current_node.get_next())
        self.length -= 1

    def get_reversed_list(self):
        if self.length == 0:
            return "Empty list"

        rev = self.get_list()
        list.reverse(rev)
        return rev

    def get_sorted_list(self):
        if self.length == 0:
            return "Empty list"

        sort = self.get_list()
        list.sort(sort)
        return sort


def main():
    sll = SingleLinkedList()
    while True:
        try:
            ch = int(input("\n1.Insert at beginning"
                           "\n2.Insert at end"
                           "\n3.Insert at given position"
                           "\n4.Delete at beginning"
                           "\n5.Delete at end"
                           "\n6.Delete at given position"
                           "\n7.Display list"
                           "\n8.Search list"
                           "\n9.Length of list"
                           "\n10.Display sorted list"
                           "\n11.display reversed list"
                           "\n12.Exit"
                           "\n\nChoose a option: "))
        except ValueError:
            print("Invalid option selected")
            continue

        if ch == 1:
            data = input("Enter data to insert at beginning of list: ")
            sll.insert_at_beginning(data)
        elif ch == 2:
            data = input("Enter data to insert at ending of list: ")
            sll.insert_at_end(data)
        elif ch == 3:
            try:
                position = int(input("Enter position to insert data: "))
            except ValueError:
                print("Position must be a integer")
                continue

            data = input("Enter data to insert at position {}: ".format(position))
            sll.insert_at(data, position)
        elif ch == 4:
            sll.delete_at_beginning()
        elif ch == 5:
            sll.delete_at_end()
        elif ch == 6:
            try:
                position = int(input("Enter position to insert data: "))
            except ValueError:
                print("Position must be a integer")
                continue
            sll.delete_at(position)
        elif ch == 7:
            print(sll.get_list())
        elif ch == 8:
            data = input("Enter data to search: ")
            sll.search(data)
        elif ch == 9:
            print(sll.get_length())
        elif ch == 10:
            print(sll.get_sorted_list())
        elif ch == 11:
            print(sll.get_reversed_list())
        elif ch == 12:
            break
        else:
            print("Invalid option selected")


if __name__ == '__main__':
    main()
