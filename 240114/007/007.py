# input: "비밀코드" "접선 장소" "시간"

class Message:
    def __init__(self, code, space, time):
        self.code = code
        self.space = space
        self.time = time

code, point, time = tuple(input().split())
message = Message(code, point, time)
print(f"secret code : {message.code}")
print(f"meeting point : {message.space}")
print(f"time : {message.time}")