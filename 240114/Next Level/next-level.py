class User:
    def __init__(self, user_id, level):
        self.user_id = user_id
        self.level = level
    
    def print_out(self):
        print(f"user {self.user_id} lv {self.level}")

user_01 = User("codetree", "10")
user_name, user_level = tuple(input().split())
user_02 = User(user_name, user_level)

user_01.print_out()
user_02.print_out()