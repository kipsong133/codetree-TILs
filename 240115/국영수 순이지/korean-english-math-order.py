class Score:
    def __init__(self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, kor, eng, math

n = int(input())
scores = []

while True:
    if n <= len(scores):
        break
    name, kor, eng, math = tuple(input().split())
    scores.append(Score(name, int(kor), int(eng), int(math)))

scores.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for score in scores:
    print(score.name, score.kor, score.eng, score.math)