"""
The code in this project is inspired by the Love Sandwiches project,
https://github.com/Pelikantapeten/p3-dad-jokes/blob/main/run.py,
https://hackr.io/blog/python-projects Number Guessing
"""

import random

quote_list = [
    'Life does not end when we die, it ends when we give up',
    'All our dreams can come true, if we have the courage to pursue them',
    'Happiness is not something ready made. It comes from your own actions',
    'The secret of getting ahead is getting started',
    'Whatever you are, be a good one',
    'Impossible is just an opinion',
    'Your passion is waiting for your courage to catch up',
    'Hold the vision, trust the process',
    'Do not be afraid to give up the good to go for the great',
    'Keep your eyes on the stars, and your feet on the ground'
]


def welcome_quote_of_the_day():
    print('Welcome to Quote of the Day!\n')


def check_input(user_input):
    inputs_list = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday', 'Sunday'
    ]

    if user_input in inputs_list:
        random_quote = display_random_quote()
        print(random_quote)
        return True
    else:
        print('Please enter a valid weekday')
        return False


def display_random_quote():
    random_quote = random.choice(quote_list)
    return random_quote


def game_end():
    print('Thank you for playing!')


def main():
    welcome_quote_of_the_day()

    while True:
        day_name = input("Enter the name of today:\n")
        if check_input(day_name):
            break

    game_end()


if __name__ == "__main__":
    main()
