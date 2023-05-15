from rich.prompt import Prompt
from rich.console import Console
from random import choice
from words import word_list

SQUARES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

WELCOME_MESSAGE = f'\n[white on blue] WITAJ W PROGRAMORDLE [/]\n'
PLAYER_INSTRUCTIONS = "Możesz zacząć zgadywać\n"
ALLOWED_GUESSES = 6

def correct_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'


def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += correct_place(letter)
            wordle_pattern.append(SQUARES['correct_place'])
        elif letter in answer:
            guessed += correct_letter(letter)
            wordle_pattern.append(SQUARES['correct_letter'])
        else:
            guessed += incorrect_letter(letter)
            wordle_pattern.append(SQUARES['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern)


def game(console, chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    word_length = len(chosen_word)

    GUESS_STATEMENT = f"\nWpisz swoją {word_length}-literową odpowiedź"

    while not end_of_game:
        guess = Prompt.ask(GUESS_STATEMENT).upper()
        while len(guess) != word_length or guess in already_guessed:
            if guess in already_guessed:
                console.print("[red]Już dałeś taką odpowiedź!!\n[/]")
            else:
                console.print(f'[red]Wprowadź {word_length}-literowe slowo!!\n[/]')
            guess = Prompt.ask(GUESS_STATEMENT).upper()
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        console.print(*all_words_guessed, sep="\n")
        console.print(f"\n[yellow]Próby {len(already_guessed)}/{ALLOWED_GUESSES}[/]\n")
        console.print("[yellow]Próbuj dalej!!\n[/]")
        if guess == chosen_word or len(already_guessed) == ALLOWED_GUESSES:
            end_of_game = True
    if len(already_guessed) == ALLOWED_GUESSES and guess != chosen_word:
        console.print(f"\n[red]Próby {len(already_guessed)}/{ALLOWED_GUESSES}[/]")
        console.print(f'\n[red]Niestety nie udało ci się [/]')
        console.print(f'\n[green]Poprawne słowo: {chosen_word}[/]')
        console.print(f'\n[green]Twój postęp z każdym słowem: [/]')
    else:
        console.print(f"\n[green]Próby {len(already_guessed)}/{ALLOWED_GUESSES}[/]\n")
        console.print(f'\n[green]Wygrałeś! Podałeś poprawną odpowiedź!! [/]')
        console.print(f'\n[green]Poprawne słowo: {chosen_word}[/]')
        console.print(f'\n[green]Twój postęp z każdym słowem: [/]')
    console.print(*full_wordle_pattern, sep="\n")
    

if __name__ == '__main__':
    console = Console()
    chosen_word = choice(word_list)
    console.print(WELCOME_MESSAGE)
    console.print(PLAYER_INSTRUCTIONS)
    game(console, chosen_word)