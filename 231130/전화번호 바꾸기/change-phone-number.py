# Input: 010-xxxx-yyyy
# Output: 010-yyyy-xxxx

def solution():
    phone_number = input().split("-")
    front = phone_number[1]
    back = phone_number[2]
    print(f"010-{back}-{front}")

solution()