class Mission:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec
    
    def print_out(self):
        print(f"code : {self.code}\ncolor : {self.color}\nsecond : {self.sec}")

code, color, sec = tuple(input().split())
mission = Mission(code, color, int(sec))
mission.print_out()