# 윤년을 처리하기 위한 함수 추가 (옵션)
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 입력 유효성 검사를 별도의 함수로 분리
def validate_input(m, d):
    if m < 1 or m > 12 or d < 1 or d > 31:
        print("잘못된 날짜 입력입니다.")
        return False
    return True

# get_num_of_day 함수를 더 간결하게 수정
def get_num_of_day(m, d):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days[:m-1]) + d

# 주 함수 solution에서는 유효성 검사 후 날짜 계산 수행
def solution(m1, d1, m2, d2):
    if not (validate_input(m1, d1) and validate_input(m2, d2)):
        return
    
    # 수정된 get_num_of_day 함수 사용
    start = get_num_of_day(m1, d1)
    end = get_num_of_day(m2, d2)
    
    between = end - start
    index = between % 7

    # 'between'을 직접 매핑할 경우 맵핑 테이블 수정
    mapping_day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    print(mapping_day[index])

# input 받기 전에 유효성 검사를 포함하여 solution 호출
m1, d1, m2, d2 = map(int, input().split())
solution(m1, d1, m2, d2)