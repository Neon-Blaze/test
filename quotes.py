import random

def get_inspirational_quote():
    quotes = [
        "The best way to predict the future is to invent it.",
        "You miss 100% of the shots you don’t take.",
        "The only way to do great work is to love what you do.",
        "Success is not how high you have climbed, but how you make a positive difference to the world.",
        "Your time is limited, don't waste it living someone else's life.",
        "The only limit to our realization of tomorrow is our doubts of today.",
        "Don't watch the clock; do what it does. Keep going.",
        "You are never too old to set another goal or to dream a new dream.",
        "Act as if what you do makes a difference. It does.",
        "Success is not the key to happiness. Happiness is the key to success."
    ]
    return random.choice(quotes)

def main():
    print("Here is your awesome inspirational quote:")
    print(get_inspirational_quote())

if __name__ == "__main__":
    main()
