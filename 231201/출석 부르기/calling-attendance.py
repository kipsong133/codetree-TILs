def solution():
    input_num = int(input())
    student_name = get_student_name(input_num)
    print(student_name)


def get_student_name(student_num: int):
    student_dic = {1: "John", 2: "Tom", 3: "Paul"}
    return student_dic.get(student_num, "no element error") # String




solution()