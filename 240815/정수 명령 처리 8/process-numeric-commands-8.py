# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# DoublyLinkedList
class DLL:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0
    
    def push_front(self, num):
        new_node = Node(num)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.count += 1

    def push_back(self, num):
        new_tail = Node(num)
        if self.tail is None:
            self.tail = new_tail
            self.head = new_tail
        else:
            old_tail = self.tail
            new_tail.prev = old_tail
            old_tail.next = new_tail
            self.tail = new_tail

        self.count += 1
    
    def pop_front(self):
        if self.head is None:
            return None

        popped_data = self.head.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None 
        
        self.count -= 1
        return popped_data
    
    def pop_back(self):
        if self.tail is None:
            return None

        popped_data = self.tail.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.count -= 1
        return popped_data

    def size(self):
        return self.count
    
    def front(self):
        if self.head is None:
            return None
        return self.head.data

    def back(self):
        if self.tail is None:
            return None
        return self.tail.data
    
    def empty(self):
        return 1 if self.head is None else 0

# 입력 및 실행
cmd_lines = int(input())

dll = DLL()

for _ in range(cmd_lines):
    input_list = input().split()
    cmd = input_list[0]
    num = input_list[1] if len(input_list) > 1 else None

    if cmd == "push_front":
        dll.push_front(int(num))
    elif cmd == "push_back":
        dll.push_back(int(num))
    elif cmd == "pop_front":
        result = dll.pop_front()
        if result is not None:
            print(result)
    elif cmd == "pop_back":
        result = dll.pop_back()
        if result is not None:
            print(result)
    elif cmd == "front":
        result = dll.front()
        if result is not None:
            print(result)
    elif cmd == "back":
        result = dll.back()
        if result is not None:
            print(result)
    elif cmd == "size":
        print(dll.size())
    elif cmd == "empty":
        print(dll.empty())