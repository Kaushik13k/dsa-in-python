class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def traversal(self):
        current = self.head
        if current == None:
            print(f"There is nothing in the LL")
            return "There is nothing in the LL"
        while current is not None:
            print(f"{current.value} ->")
            current = current.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, value, position):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(position - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1

    def get_value(self, index):
        current = self.head
        if index == -1:
            return self.tail
        elif index < -1 and index > self.length:
            return None
        else:
            for _ in range(index-1):
                current = current.next
            return current.value

    def search_value(self, value):
        temp = self.head
        if self.head == None:
            return "There is nothing to return"
        while temp.next is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def search_index(self, value):
        temp = self.head
        count = 0
        if self.head == None:
            return "There is nothing to return"
        while temp.next is not None:
            if temp.value == value:
                return count
            temp = temp.next
            count +=1
        return False

# new_instance = LinkedList()
# new_instance.traversal()

# new_instance.append(1)
# new_instance.append(2)
# new_instance.append(3)
# new_instance.append(4)
# new_instance.append(5)

# print("------The LL after append is------")
# new_instance.traversal()

# new_instance.prepend(0)
# new_instance.prepend(-1)

# print("------The LL after prepend is------")
# new_instance.traversal()

# new_instance.insert(10, 2)

# print("------The LL after index insert is------")
# new_instance.traversal()

# print("------The LL after search value is------")
# print(new_instance.search_value(11))

# print("------The LL after search index is------")
# print(new_instance.search_index(11))




