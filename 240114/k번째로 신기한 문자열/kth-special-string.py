# n: n개의 줄로 텍스트가 주어진다.
# k: k 번째 텍스트를 출력을 해야한다.
# T: T로 시작하는 문자열로 정렬한다.
n, k, T = input().split()

# 문자열을 입력받는다.
word_list = [ input() for _ in range(int(n)) ]


def check_text(word: str) -> bool:
    if len(word) < len(T): return False
    for i in range(0, len(T)):
        if word[i] != T[i]:
            return False
    return True

def solution():
    satisfied_word_list: [str] = ['0']
    # T로 시작하는 텍스트만 남긴다.
    # 1. cotain으로 거르기
    # 2. T만큼 순회하면서, 조회하기
    for word in word_list:
        if check_text(word):
            satisfied_word_list.append(word)
    
    # sort() 한다.
    satisfied_word_list.sort()
    print(satisfied_word_list[int(k)])

solution()