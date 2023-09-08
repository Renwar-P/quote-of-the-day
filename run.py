import random


def welcome_quote_of_the_day():
    """
    Function to greet and start the game
    """
    print('Welcome to Quote of the Day!\n')
    print('Please enter the name of the current day')


def check_input(user_input):
    """
    Function to check if input is valid
    """
    inputs_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 
    'Saturday', 'Sunday']

    if user_input in inputs_list:
        print(random_quote) 
    else:
        print('Please enter a valid weekday')


def display_random_quote():
    """
    Function to get a random quote
    """
    random_quote = random.choice(quote_list)
    return random_quote


a = 'Life does not end when we die, it ends when we give up'
b = 'All our dreams can come true, if we have the courage to pursue them'
c = 'Happiness is not something ready made. It comes from your own actions'
d = 'The secret of getting ahead is getting started'
e = 'Whatever you are, be a good one'
f = 'Impossible is just an opinion'
g = 'Your passion is waiting for your courage to catch up'
h = 'Hold the vision, trust the process'
i = 'Do not be afraid to give up the good to go for the great'
j = 'Keep your eyes on the stars, and your feet on the ground'

quote_list = [a, b, c, d, e, f, g, h, i, j]


def game_end():
    """
    Function to run when the game ends
    """


def main():
    """
    Function to run all 
    """
    welcome_quote_of_the_day()