import random

with open('allwords.txt') as f:
	words = list(f)
str_word = random.choice(words).strip()
word = list(str_word)
guessed = list('_' * len(word))
wrong_guessed = []
tries = 0
max_tries = 8

print(f'Welcome to hangman. Type "exit" or "stop" to stop the game. You have {max_tries} tries to guess this word: \n{" ".join(guessed)}')

while True:
	if tries == max_tries:
		print(f'You have reached the maximum number of tries. The word was {str_word} but you only got {"".join(guessed)}')
		break
	letter = input('What letter would you like to guess? You can also try to guess the word. ')
	if not letter.isalpha():
		print('Please guess only one letter (no numbers, spaces, symbols, etc.) unless you try the word.')
		continue
	elif len(letter) > 1 and letter.isalpha():
		if letter.lower() == 'exit' or letter.lower() == 'stop':
			print(f'The word was {str_word} but you only got {"".join(guessed)}')
			break
		elif letter.upper() in wrong_guessed:
			print('You already tried this word!')
		elif letter.upper() == str_word:
			print("You got the word!")
			break
		elif len(letter) != len(str_word):
			print('If you are trying to guess the word, make sure you spelled it correctly. Otherwise please guess only one letter (no numbers, spaces, symbols, etc.).')
			continue
		else:
			tries += 1
			print(f'You did not get the word. You have {max_tries - tries} tries left.')
			wrong_guessed.append(letter.upper())
	elif len(letter) > 1:
		print('Please guess only one letter (no numbers, spaces, symbols, etc.) unless you try the word.')
		continue
	elif letter.upper() in wrong_guessed or letter.upper() in guessed:
		letter = ''
		print('You already guessed this letter!')
	elif letter.upper() in word:
		while letter.upper() in word:
			index_of_letter = word.index(letter.upper())
			guessed[index_of_letter] = letter.upper()
			word[index_of_letter] = '_'
		print(' '.join(guessed))
	else:
		if letter != '':
			wrong_guessed.append(letter.upper())
		tries += 1
		print(f'That letter is not in the word, you have {max_tries - tries} tries left.')

	if '_' not in guessed:
		print("You got the word!")
		break
