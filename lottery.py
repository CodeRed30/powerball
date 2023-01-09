import random

white_possibles = list(range(1, 70))
red_possibles = list(range(1,27))

tickets_per_draw = 1
num_draws = 1

total_spent = 0
earnings = 0

times_won = {
    "5 Balls + Powerball": 0,
    "5 Balls": 0,
    "4 Balls + Powerball": 0,
    "4 Balls": 0,
    "3 Balls + Powerball": 0,
    "3 Balls": 0,
    "2 Balls + Powerball": 0,
    "1 Ball + Powerball": 0,
    "0 Balls + Powerball": 0,
    "0 Balls": 0,
}

def winning_calc(my_numbers, winning_numbers):
    win_amount = 0
    white_matches = len(my_numbers["whites"].intersection(winning_numbers["whites"]))
    power_match = my_numbers["red"] == winning_numbers["red"]

    return win_amount

for draw in range(num_draws):
    white_draw = set(random.sample(white_possibles, k=5))
    red_draw = random.choice(red_possibles)

    winning_numbers = {
        "whites": white_draw, "red": red_draw
        }
    for ticket in range(tickets_per_draw):
        total_spent += 2
        white_choices = set(random.sample(white_possibles, k=5))
        red_choice = random.choice(red_possibles)
        my_numbers = {
        "whites": white_choices, "red": red_choice
        }
    
    # winning_calc(my_numbers)

