
import random

with open("fortune.txt", "r") as file:
    content = file.read()
    quotes = content.split('%')
    random_quote = random.choice(quotes).strip()
print(random_quote)
