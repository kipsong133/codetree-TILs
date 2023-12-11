def make_square(n: int):
    cnt = 0
    value = 1 # staring from 1
    # Iteration: number of lines
    for _ in range(n): # ex) 4 line
        for _ in range(n):
                    # condition: re-starting from 1
            if value >= 10:
                value = 1
            print(value, end = ' ')
            value += 1
        print('')



def solution():
    # input: 4
    n = int(input())
    make_square(n)


solution()