import random #პითონის ჩაშენებული მოდული, რომლის გამოიყენებაც შეგვიძლია random რიცხვების შესაქმნელად.

class HangmanGame: # კლასის შექმნა Hangman თამაშისთვის
    def __init__(self):
        self.words = ["python", "hangman", "developer", "computer", "programming"] # გამოსაცნობი სიტყვები
        self.word = random.choice(self.words) # ირჩევს სიტყვას სიიდან
        self.guesses = [] # აქამდე გამოცნობილი ასოებისთვის
        self.max_attempts = 8 # ასოს შეყვანის მაქსიმალური რაოდენობა
        self.attempts = 0 # აქამდე არასწორად გაკეთებულის რაოდენობა
        self.correct_guesses = ["_"] * len(self.word) # შეყვანილი ასოების რაოდენობისთვის

    def display_word(self):
        print("Current word: " + " ".join(self.correct_guesses)) # ბეჭდავს სწორად გამოცნობილი ასოების სიას

# უკვე გამოცნობილი ასოს შემთხვევაში
    def guess_letter(self, letter):
        if letter in self.guesses:
            print(f"You already guessed '{letter}'. Try again.")
            return False

# დაამატეთ გამოცნობილი ასო უკვე გამოცნობილების სიას
        self.guesses.append(letter)

# თუ მომხმარებლის მიერ მითითებული ასო სიტყვაშია, განაახლეთ  სია ყველა პოზიციაზე, სადაც ასო გამოჩნდება
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.correct_guesses[i] = letter
            print(f"Good guess! The letter '{letter}' is in the word.")

# ასოს სიტყვაში არ არსებობის შემთხვევაში
        else:
            self.attempts += 1
            print(f"Oops! The letter '{letter}' is not in the word.")
        
        return True

    def check_win(self):
        # მთლიანი სიტყვა დაბრუნდება იმ შემთხვევაში თუ სწორად გამოიცნო 
        return "".join(self.correct_guesses) == self.word

    def check_game_over(self):
        # true-ს დასაბრუნებლად იმ შემთხვევაში თუ მცდელობების რაოდენობა არ აღემატება ან ტოლია max_attempts
        return self.attempts >= self.max_attempts

    def get_remaining_attempts(self): 
        # დარჩენილი მცდელობების რაოდენობისთვის
        return self.max_attempts - self.attempts

def main():
    # მისალმებისთვის
    print("Welcome to Hangman!")
    game = HangmanGame()

    while True: # თამაშის გასაგრძელებლად დასრულებამდე
        game.display_word() # სიტყვის ამ მომენტის მდგომარეობის საჩვენებლად

        if game.check_win():
            # შესამოწმებლად მოგებული აქვს თუ არა თამაში მოთამაშეს
            print("Congratulations! You guessed the word correctly!") 
            break
        if game.check_game_over():
            # შესამოწმებლად დაასრულა თუ არა მოთამაშემ თამაში მოთამაშეების მიერ ყველა მცდელობის გამოყენების შემდეგ
            print(f"Game over! The word was '{game.word}'.")
            break # ციკლის შესაწყვეტად

        print(f"You have {game.get_remaining_attempts()} attempts remaining.") # საჩვენებლად კიდევ რამდენის ცდის უფლება აქვს
        guess = input("Enter a letter to guess: ").lower()

        if len(guess) != 1 or not guess.isalpha(): # ამოწმებს ასოს თუ შეიცავს ასოს გარდა სხვა სიმბოლოებს
            print("Invalid input. Please enter a single letter.") 
            continue # დასასრულებლად 

        game.guess_letter(guess) # არის თუ არა მომხმარებლის მიერ მითითებული ასოები არის სიტყვაში

main()