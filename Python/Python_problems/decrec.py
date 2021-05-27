def check_Key(words, S, key):
	for word in S:
		decrypted_word = decrypt(word, key)
		if not decrypted_word in words:
			return False
	return True

def decrypt(word, key):
	decrypted_word = ""
	for letter in word:
		decrypted_word += key.get(letter, letter)
	return decrypted_word

def decrypt_message(S, key):
	decrypted_message = []
	for word in S:
		decrypted_message.append(decrypt(word, key))
	return decrypted_message

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
keys = []

w = int(input())
letter = set(letters)
words = set()

for i in range(w):
	word = input()
	words.add(word)

S = input().split()

for a in letters:
	if a == "a":
		continue

	for b in letters:
		if b == "b" or b == a:
			continue

		for c in letters:
			if c == "c" or c == b or c == a:
				continue

			for d in letters:
				if d == "d" or d == c or d == b or d == a:
					continue

				for e in letters:
					if e == "e" or e == d or e == c or e == b or e == a:
						continue

					for f in letters:
						if f == "f" or f == e or f == d or f == c or f == b or f == a:
							continue

						for g in letters:
							if g == "g" or g == f or g == e or g == d or g == c or g == b or g == a:
								continue

							for h in letters:
								if h == "h" or h == g or h ==f or h == e or h == d or h ==c or h == b or h == a:
									continue

								key = {"a" : a, "b" : b, "c" : c, "d" : d, "e" : e, "f" : f, "g" : g, "h" : h}

								if check_Key(words, S, key):
									print(*decrypt_message(S, key))

									exit()

