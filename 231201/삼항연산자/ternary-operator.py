def solution():
    # input: 100 / 98 / 50
    input_score = int(input()) 

    is_pass = "pass" if input_score >= 100 else "failure"
    print(is_pass)


solution()