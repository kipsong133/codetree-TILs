def print_square(n: int, m: int):
    # Iteration: number of lines
    for _ in range(n):
        print('1' * m)
    

def solution():
    input_arr = list(map(int, input().split()))
    n = input_arr[0]
    m = input_arr[1]

    print_square(n, m)
    
solution()