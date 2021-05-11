from random import choice


def get_random_word():
   with open('fruits.txt') as f:
      fruits = f.readlines()
   fruit = choice(fruits)
   return fruit.strip()


def print_masked_word(word, open_letters):
   for letter in word:
      print(letter.upper() if letter in open_letters else "_", end=" ")
   print()


def check_word(word, open_letters):
   return open_letters.issuperset(set(word))


random_word = get_random_word()
guessed_letters = set()

lives_left = 5

while lives_left > 0:
   print(f"Guess the word. {lives_left} mistakes left.")
   print_masked_word(random_word, guessed_letters)
   letter_to_check = input("Guess a letter: ").lower()

   if letter_to_check in random_word:
      guessed_letters.add(letter_to_check)
      if check_word(random_word, guessed_letters):
         print_masked_word(random_word, guessed_letters)
         print("You won the game.")
         break
   elif letter_to_check not in guessed_letters:
      lives_left -= 1
      guessed_letters.add(letter_to_check)
else:
   print_masked_word(random_word, set(random_word))
   print("You lost the game.")
