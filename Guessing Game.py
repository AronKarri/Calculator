secret_word = "shark"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("The secret word is an apex predator that lives in the sea. Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if not out_of_guesses:
    print("You Win!")
else:
    print("Out of guesses, better luck next time!")
