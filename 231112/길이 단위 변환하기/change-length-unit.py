ft_unit = 30.48 # 1 ft = 30.48cm
mi_unit = 160934 # 1 mi = 160934cm

a, b = 9.2, 1.3
answer_01 = ft_unit * a
answer_02 = mi_unit * b

print(f"{a}ft = {answer_01:.1f}cm")
print(f"{b}mi = {answer_02:.1f}cm")