def convert_ft_to_cm(ft_input):
    result = float(ft_input * 30.48)
    return result

a = float(input())
result = convert_ft_to_cm(a)
print(f"{result:.01f}")