word = input(" Input any word you like ")

if not word:
    print("Sorry, you forgot input any word")
    exit()

rev_word = "".join(reversed(word))

if word == rev_word:
    print("YES")
else:
    print("NO")
