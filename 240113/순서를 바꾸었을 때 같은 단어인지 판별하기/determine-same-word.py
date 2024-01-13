str_a = list(input())
str_b = list(input())
str_a.sort()
str_b.sort()

def can_make():
    for i in range(len(str_a)):
        if str_a[i] != str_b[i]:
            print("No")
            return
    print("Yes")

can_make()