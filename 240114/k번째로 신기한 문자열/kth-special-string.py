# input
n, k, t = tuple(input().split())
n = int(n)
k = int(k)

# pattern을 가진 단어인지 확인한다.
def star_with(word: str, pattern: str) -> bool:
	# 단어 길이가 애초에 pattern보다 작으면 안된다.
	if len(word) < len(pattern): return False

	# word를 pattern의 길이만큼 슬라이싱해서 확인한다.
	return word[:len(pattern)] == pattern

# input: n 개의 단어를 받는다. 조건을 확인한다.
words: [str] = []
for _ in range(n):
	word = input()
	if star_with(word, t):
		words.append(word)

words.sort()
print(words[k-1])