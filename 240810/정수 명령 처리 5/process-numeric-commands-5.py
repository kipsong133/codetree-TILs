# Key List
PUSH_BACK = "push_back"
GET = "get"
SIZE = "size"
POP_BACK = "pop_back"

# Method list
def push_back(arr, num):
    arr.append(int(num))
    return arr

def get(arr, num):
    print(arr[int(num) - 1])
    return arr
    

def size(arr):
    print(len(arr))
    return arr

def pop_back(arr):
    arr.pop()
    return arr


# Implement
def solution():
    command_list = []

    # input & interator
    command_count = int(input())
    
    while command_count > 0:
        # (push_back 10)
        command_input = tuple(input().split())
        command = command_input[0] 
        
        # if push_back / get, must have two element
        if command in [PUSH_BACK, GET]:
            num = command_input[1]
            # validation
            if len(command_input) < 1: return -1 # Error...

            # command actions
            command_list = push_back(command_list, num) if command_input[0] == PUSH_BACK else get(command_list, num)

        else:    
            # others, need only one element: 'size' or 'pop_back'
            # validation
            if len(command_input) > 1: return -1
            command_list =  pop_back(command_list) if command == POP_BACK else size(command_list)

        # Iterating
        command_count -= 1

# Caller        
solution()