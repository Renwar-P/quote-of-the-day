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
    """
    Function to greet and start the game
    """
    print('Welcome to Quote of the Day!\n')


def check_input(user_input):
    """
    Function to check if input is valid
    """
    inputs_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if user_input in inputs_list:
        random_quote = display_random_quote()
        print(f"\nHere's a random quote for {user_input}:")
        print(random_quote)
    
    else:
        print('Please enter a valid weekday')
        

def display_random_quote():
    """
    Function to get a random quote
    """
    random_quote = random.choice(quote_list)
    return random_quote


def game_end():
    """
    Function to run when the game ends
    """
    print('Thank you for playing!')


def main():
    """
    Function to run the entire program
    """
    welcome_quote_of_the_day()
    day_name = input("Enter the name of today: ")
    check_input(day_name)
    game_end()


if __name__ == "__main__":
    main()
