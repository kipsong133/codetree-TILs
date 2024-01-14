# input: "비밀코드" "접선 장소" "시간"

class Message:
    def __init__(self, code, space, time):
        self.code = code
        self.space = space
        self.time = time

input_data = tuple(input().split())
message = Message(input_data[0], input_data[1], input_data[2])
print(f"secret code : {message.code}")
print(f"meeting point : {message.space}")
print(f"time : {message.time}")