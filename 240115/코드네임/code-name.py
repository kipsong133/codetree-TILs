class Spy:
    def __init__(self, code_name="", score=101):
        self.code_name = code_name
        self.score = score

# input
spy_list = []
while True:
    if len(spy_list) >= 5:
        break
    code_name, score = tuple(input().split())
    spy_list.append(Spy(code_name, int(score)))

min_spy = Spy()
for spy in spy_list:
    if min_spy.score > spy.score:
        min_spy = spy

print(f"{min_spy.code_name} {min_spy.score}")