class ll:
    class Node:
        def __init__(self, value, next):
            self.data = value
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        self.head = self.Node(data, self.head)
        self.size += 1

    def add_node(self, data):
        self.size += 1
        self.tail = self.Node(data, None)

    def del_node(self, to_del):
        temp = self.head
        prev = self.head
        if self.head.data == to_del:
            self.head = self.head.next
        while temp is not None:
            if temp.data == to_del:
                prev.next = temp.next
            else:
                prev = temp
                temp = temp.next

    def print__(self):
        print("Queue:")
        if (self.size == 0):
            print("EMPTY Queue")
            return
        else:
            temp = self.head
            while temp is not None:
                print("-{}-".format(temp.data))


if __name__ == '__main__':
    lnkdlst = ll()
    while 1:
        n = int(input("Enter\n1->To print Q\n2->To add a data to Q\n3->To push data to Q\n4 To delete data\n5 To exit\nEnter your input ::"))
        if n == 1:
            lnkdlst.print__()
        elif n == 2:
            data = int(input("Enter a value to add :"))
            lnkdlst.add_node(data)
        elif n == 3:
            data = int(input("Enter a value to add :"))
            lnkdlst.push(data)
        elif n == 4:
            data = int(input("Enter a value to add :"))
            lnkdlst.del_node(data)

        elif n == 5:
            print("Thanks!")
            quit()
        else:
            print("Enter a valid input(integer between (1,4) both inclusive)")
