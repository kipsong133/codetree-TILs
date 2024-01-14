class Weather:
    def __init__(self, date, day, condition):
        self.date = date
        self.day = day
        self.condition = condition
    
    @classmethod
    def filter_rain(cls, arr):
        temp = []
        for weather in arr:
            if weather.condition == "Rain":
                temp.append(weather)
        return temp

    def __lt__(self, other):
        return self.date < other.date

n = int(input())
weathers = []  # : [Weather] type hint를 이곳에 둘 필요는 없습니다.

while True:
    if len(weathers) >= n:
        break
    date, day , condition = tuple(input().split())
    weathers.append(Weather(date, day, condition))

filtered_weathers = Weather.filter_rain(weathers)
filtered_weathers.sort()

# 리스트 내 객체를 출력하려면, 객체의 문자열 표현을 정의해야 합니다.
# __repr__를 추가해서 객체의 정보를 문자열로 깔끔하게 출력할 수 있게 하겠습니다.
print(f"{filtered_weathers[0].date} {filtered_weathers[0].day} {filtered_weathers[0].condition}")