import random
import time
import threading

class HangmanGame:

    def __init__(self, words, max_attempts=6):

        self.words = words

        self.max_attempts = max_attempts

        self.word_to_guess = ""

        self.guesses = []

        self.attempts_left = self.max_attempts

        self.time_limit = 30

        self.timer = None

    def select_word(self):

        self.word_to_guess = random.choice(self.words).upper()

    def display_word(self):

        displayed_word = ""

        for letter in self.word_to_guess:

            if letter in self.guesses:

                displayed_word += letter

            else:

                displayed_word += "_"

        return displayed_word

    def start_timer(self):

        self.timer = threading.Timer(self.time_limit, self.timeout)

        self.timer.start()

    def stop_timer(self):

        if self.timer and self.timer.is_alive():

            self.timer.cancel()

    def make_guess(self, guess):

        guess = guess.upper()

        if guess in self.guesses:

            print("You already guessed that letter. Try again.")

            return

        self.guesses.append(guess)

        if guess not in self.word_to_guess:

            self.attempts_left -= 1

            print("Incorrect guess! Attempts left:", self.attempts_left)

        else:

            print("Correct guess!")

    def is_game_over(self):

        if "_" not in self.display_word():

            print("Congratulations! You guessed the word:", self.word_to_guess)

            return True

        elif self.attempts_left <= 0:

            print("Game over! The word was:", self.word_to_guess)

            return True

        return False

    def timeout(self):

        print("\nTime's up! Game over.")

        print("The word was:", self.word_to_guess)

        self.play_again()

    def play_again(self):

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again == 'yes':

            self.reset_game()

            self.run_game()

        else:

            exit()

    def reset_game(self):

        self.guesses = []

        self.attempts_left = self.max_attempts

        self.stop_timer()

    def run_game(self):

        while True:

            self.select_word()

            print("\nWelcome to Hangman!")

            print("Word to guess:", self.display_word())

            self.start_timer()

            while not self.is_game_over():

                guess = input("Enter your guess (single letter): ")

                if len(guess) != 1 or not guess.isalpha():

                    print("Invalid input. Please enter a single letter.")

                    continue

                self.stop_timer()

                self.make_guess(guess)

                print("Current status:", self.display_word())

            self.play_again()

def main():

    words_to_guess = ["PYTHON", "JAVA", "HTML", "CSS", "JAVASCRIPT", "PYTHONIC"]

    hangman = HangmanGame(words_to_guess)

    hangman.run_game()

if __name__ == "__main__":
    main()
